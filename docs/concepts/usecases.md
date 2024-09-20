# Usecases for Deequ

Compared to other data quality tools that primarily follow zero-code or low-code paradigms, Deequ is a code-first solution that provides a well-designed and stable programming API. This approach makes Deequ highly flexible, allowing you to design your own YAML-like low-code API with a structure that fits your specific domain. In essence, Deequ functions more as a data quality engine, adaptable to most possible use cases. Some of these use cases are described below.

## Data Profiling

The first and most obvious use case for Deequ is data profiling. In this scenario, one does not need to use `Check`, `Constraint`, or `AnomalyDetection` features. It would be sufficient to simply add all the analyzers to the `required_analyzers` section of the `VerificationSuite`. This approach would not produce any check results or row-level results, but instead generate a simple table with computed metrics per instance (which may be a `Column` or `Dataset`).

As a result, you will obtain a list of metrics and their corresponding values. Since both Deequ and Tsumugi are code-first (rather than YAML-first) frameworks, it will be very easy to customize your profiling based on the data types in your `DataFrame`.

## Static constraints based on the business rules

The next potential use case for Deequ is to add static constraints to your tables and use row-level results to quarantine data that fails to meet these constraints. For example, if you have a string column in one of your tables that should always contain exactly 14 characters, such as a mobile phone number, you can add a constraint specifying that both `MaxLength` and `MinLength` should be exactly 14. You can then use row-level results to identify which rows passed the constraint and which did not. These row-level results will contain your data along with one boolean column for each `Check`, indicating whether the row passed all the constraints in that `Check` or not. Another good option might be the `PatternMatch` analyzer, which could be used to check if a column contains a valid email address and quarantine the row if it doesn't.

## Detecting data-drift for ML-inference

Another excellent use case for Deequ is as a data drift detector for checking input in ML model batch inference. Imagine we have an ML-based recommender system that updates pre-computed recommendations daily for our users for the following day. This scenario is a good example of batch inference, where we have an ML model trained once on training data and run it each day offline on new data. For such a system, it is crucial to ensure that the data hasn't changed significantly compared to previous batches. If it has, it signals that our ML model should be retrained on more recent training data.

As we can see, there are no static constraints here. Rather than fitting our data into strict boundaries, we aim to ensure that data drift remains within acceptable limits.

This scenario presents a perfect use case for Deequ Anomaly Detection. Let's imagine we have an ML model trained on the following features:

1. Duration of customer relationship (numeric)
2. Paid subscription status (boolean, can be NULL)
3. Frequency of service usage (numeric)

In this case, we can apply the following Anomaly Detection checks:

- Assuming that the average, minimum, and maximum frequency of service usage should not change dramatically, we can apply a `RelativeRateOfChange` strategy. By setting maximum increase and minimum decrease values to 1.1 and 0.9 respectively, we allow for a ±10% drift. Any new batch that shows significant changes compared to the previous batch of data will be considered an anomaly in this case.
- Because our model uses a missing value imputation strategy to fill NULLs in a flag column, we need to ensure that the amount of NULLs is similar to the data on which we trained our ML model. For this case, a `SimpleThresholdStrategy` is a good choice: we can set maximum and minimum allowed drift limits, and any data that falls within this range will be considered acceptable.
Regarding the frequency of service usage, we know that the value should approximate a Normal Distribution. This means we can apply the `BatchNormalStrategy` to our batch intervals and ensure that the data is actually normally distributed by using thresholds for the mean and standard deviation of metrics.

