# Concepts

Since the project is primarily about creating a wrapper, it adheres to the same concepts and ideas that underpin the original Deequ library.

You can read more about that in the publications by the authors.

- _Schelter, Sebastian, et al. "Unit testing data with deequ." Proceedings of the 2019 International Conference on Management of Data. 2019._, [link](https://www.amazon.science/publications/unit-testing-data-with-deequ);
- _Schelter, Sebastian, et al. "Deequ-data quality validation for machine learning pipelines." (2018)._, [link](https://www.amazon.science/publications/deequ-data-quality-validation-for-machine-learning-pipelines);

## Analyzers

Analyzers in Deequ are similar to data metrics. Some of them are quite simple and can actually be computed using the Spark SQL API, such as `Size`, which is simply the number of rows in a `DataFrame`. However, some analyzers, like `Entropy` or `KLLSketch`, are more complex to compute. Behind the scenes, Deequ combines all the analyzers into custom accumulators and computes results at scale using low-level Apache Spark APIs. End users shouldn't need to worry about the execution model, but they should understand the range of metrics that can be computed.


At the moment this library supports the following analyzers:

<!-- Documnetation is inspired by docstring of the Deequ code:
https://github.com/awslabs/deequ/tree/master/src/main/scala/com/amazon/deequ/analyzers 
-->

- `ApproxCountDistinct`: Computes the approximate count of distinct values in the data; recommended over `CountDistinct` for large datasets.
- `ApproxQuantile`: Computes the approximate quantile of a given numeric column.
- `ApproxQuantiles`: Computes quantiles for a set of columns.
- `ColumnCount`: Returns the number of columns in the data.
- `Completeness`: Calculates the fraction of non-null values in a column.
- `Compliance`: Calculates the fraction of rows that satisfy a given predicate.
- `Correlation`: Computes the correlation between two columns.
- `CountDistinct`: Calculates the exact count of distinct values for a given set of columns.
- `CustomSql`: Computes a metric based on a provided custom SQL snippet.
- `Distinctness`: Calculates the fraction of distinct values in a column.
- `Entropy`: Measures the level of information contained in a message. Given the probability distribution of values in a column, it describes how many bits are required to identify a value.
- `ExactQuantile`: Computes the exact value of a given quantile for a specific column.
- `Histogram`: Summarizes values in a DataFrame column. Groups the column's values and calculates either the number of rows with a specific value or the fraction of this value, or sums values in another column.
- `KLLSketch`: Computes quantiles sketch (see [_Zohar Karnin, Kevin Lang, Edo Liberty, arXiv 2016_](https://arxiv.org/abs/1603.05346v2) for details).
- `MaxLength`: Calculates the maximum length of values in a given column.
- `Maximum`: Computes the maximum value.
- `Mean`: Calculates the average.
- `MinLength`: Determines the minimum length of values in a given column.
- `Minimum`: Computes the minimum value.
- `MutualInformation`: Calculates the Mutual Information (MI) metric, which describes how much information about one column can be inferred from another. MI is zero for independent columns and equals the entropy of each column for functionally dependent columns.
- `PatternMatch`: Counts the number of rows that match a given regular expression pattern.
- `RatioOfSums`: Computes the ratio of sums between two columns.
- `Size`: Calculates the number of rows.
- `StandardDeviation`: Computes the standard deviation of a given numeric column.
- `Sum`: Calculates the sum.
- `UniqueValueRatio`: Computes the ratio of unique values (number of unique values divided by the total number of rows).
- `Uniqueness`: Same as `UniqueValueRatio`.

Most of analyzers also accept an optional parameter `where` that allows to compute metrics using predicate.

## Checks

Each thing in Deequ is `Check`. Check is a named set of data quality rules that should be applyed on data. Check can contain name, description, required analyzers and one or more constraints.

### Required analyzers

Required analyzers are those that will be computed regardless of other factors. This feature can be useful when one does not need to use constraints and wants to utilize Deequ solely as a data profiler.

### Constraints

A constraint in Deequ is a combination of an analyzer and an assertion about an expected value. While Deequ allows users to pass a function `metric -> boolean` as an assertion, Tsumugi does not provide this feature due to problems with serializing lambda functions. Instead, constraints in Tsumugi contain the following information:

- analyzer itslef;
- an expected value of the metric;
- a comparison sign (`<`, `<=`, `==`, `>`, `>=`);

I found that method of building assertions to be the most robust, and it is entirely sufficient for all my own use cases. However, if you're interested in more advanced assertions, please feel free to open an issue describing your specific use case, and I will try to implement it.

## Anomaly Detection

Deequ not only supports computing static constraints with pre-defined assertions and analyzers but also offers anomaly detection capabilities. Under the hood, Deequ can store all computed metrics in a repository. This feature allows users to define constraints such as "the average value of my column should not change by more than ±5% between different data batches."

Under the hood, Deequ uses a chosen comparison strategy to analyze historical data of computed metrics to determine if new data is anomalous. This is especially important in Machine Learning (ML) applications because it's quite challenging to define static constraints for ML models. These models often have non-trivial underlying logic, such as normalization and standardization. It's crucial to run ML models on data that is similar to the data on which they were trained.

### Analyzers that can be used with AD

At present, only analyzers that compute `Double` or `Long` metrics can be used with Anomaly Detection. Most analyzers fit these requirements, except for `Histogram`, `KLLSketch`, and a few others.

### Anomaly Check Config

One can use `AnomalyCheckConfig` object that provides the following available options:

- `level`: Severity level of the AD Check, the same as in Checks;
- `description`: A string description of the AD Check;
- `tags`: A map of `string -> string` that may contain any tags you want to add to the repository;
- `after_date`: A `Long` (or `int` in Python) value that filters out all keys before it when determining if the case is an anomaly or not;
- `before_date`: A `Long` (or `int` in Python) value that filters out all keys after it when determining if the case is an anomaly or not;

**_NOTE_**: Due to the internal implementation details of upstream Deequ, running your AD suite twice on the same data with the same `ResultKey` will cause it to compare the latest run with the previous run, rather than with a run using a different key. To avoid this, simply pass a value lower than the current `result_key` to your configuration.

### Repositories

At the moment the following Metric Repositories are supported:

- `FileSystemMetricRepository` that stores historical data about metrics in JSON files in any supported by `Hadoop` file system (Local FS, S3, MinIO, HDFS, etc.);
- `SparkTableMetricRepository` that stores historical data in the spark table, registered in the current-session Catalog;

### Result Key

`ResultKey` is an object that defines the key and tags of the run. The most straightforward solution would be to use a timestamp derived from either the execution date or the date corresponding to the checked data. For example, an excellent choice would be to use the timestamp value of the partition for data that is partitioned by load date.

### Strategies

The following strategies are supported at the moment:

<!-- Descriptions are inspired by Deequ docstrings 
https://github.com/awslabs/deequ/blob/master/src/main/scala/com/amazon/deequ/anomalydetection/OnlineNormalStrategy.scala
-->

- `AbsoluteChangeStrategy`: Uses static constraints on top of absulute changes of the metrics;
- `BatchNormalStrategy`: Detects anomalies based on the mean and standard deviation of all available values. Assumes that the data is normally distributed;
- `OnlineNormalStrategy`: Detects anomalies based on the running mean and standard deviation. Anomalies can be excluded from the computation to not affect the calculated mean/ standard deviation. Assumes that the data is normally distributed;
- `RelativeRateOfChangeStrategy`: Detects anomalies based on the values' rate of change. The order of the difference can be set manually. If it is set to 0, this strategy acts like the `SimpleThresholdStrategy`;
- `SimpleThresholdStrategy`: A simple anomaly detection method that checks if values are in a specified range;

## Verification Suite

The suite in Deequ consists of:

- Checks;
- Anomaly Detection cases;
- Required analyzers;
- Repository;

It serves as the main entry point for creating a Deequ job.
