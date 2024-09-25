# Docstring of classes were heavily inspired by the
# docstring from https://github.com/awslabs/python-deequ/blob/master/pydeequ/analyzers.py

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from functools import singledispatchmethod

from typing_extensions import Self

from .proto import analyzers_pb2 as proto

# Is it a protobuf-python bug? Why should I import all the dependencies manually?
from .proto import strategies_pb2 as strategies  # noqa: F401
from .proto import suite_pb2 as suite


class AbstractAnalyzer(ABC):
    """Abstract class for all analyzers in tsumugi."""

    @abstractmethod
    def _to_proto(self) -> proto.Analyzer: ...


class NullBehaviour(Enum):
    IGNORE = proto.AnalyzerOptions.NullBehaviour.Ignore
    EMPTY_STRING = proto.AnalyzerOptions.NullBehaviour.EmptyString
    FAIL = proto.AnalyzerOptions.NullBehaviour.Fail


class FilteredRowOutcome(Enum):
    NULL = proto.AnalyzerOptions.FilteredRowOutcome.NULL
    TRUE = proto.AnalyzerOptions.FilteredRowOutcome.TRUE


class AbstractAggregateFunction(ABC):
    """Abstract class Histogram aggregation functions."""

    @abstractmethod
    def _to_proto(self) -> proto.Histogram.AggregateFunction: ...


@dataclass
class SumAggregate(AbstractAggregateFunction):
    """Computes Histogram Sum Aggregation"""

    agg_column: str

    def _to_proto(self) -> proto.Analyzer:
        return proto.Histogram.AggregateFunction.Sum(agg_column=self.agg_column)


@dataclass
class CountAggregate(AbstractAggregateFunction):
    """Computes Histogram Count Aggregation"""

    def _to_proto(self) -> proto.Analyzer:
        return proto.Histogram.AggregateFunction.Count()


@dataclass
class KLLParameters:
    """Parameters for KLLSketch."""

    sketch_size: int
    shrinking_factor: float
    number_of_buckets: int

    def _to_proto(self) -> proto.KLLSketch.KLLParameters:
        return proto.KLLSketch.KLLParameters(
            sketch_size=self.sketch_size,
            shrinking_factor=self.shrinking_factor,
            number_of_buckets=self.number_of_buckets,
        )


@dataclass
class AnalyzerOptions:
    """Container for Analyzer Options."""

    null_behaviour: NullBehaviour
    filtered_row_outcome: FilteredRowOutcome

    @staticmethod
    def default() -> "AnalyzerOptions":
        return AnalyzerOptions(NullBehaviour.IGNORE, FilteredRowOutcome.NULL)

    def _to_proto(self) -> proto.AnalyzerOptions:
        return proto.AnalyzerOptions(
            null_behaviour=self.null_behaviour.value,
            filtered_row_outcome=self.filtered_row_outcome.value,
        )


@dataclass
class ApproxCountDistinct(AbstractAnalyzer):
    """Computes the approximate count distinctness of a column with HyperLogLogPlusPlus."""

    column: str
    where: str | None = None

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            approx_count_distinct=proto.ApproxCountDistinct(
                column=self.column, where=self.where
            )
        )


@dataclass
class ApproxQuantile(AbstractAnalyzer):
    """Computes the Approximate Quantile of a column.

    The allowed relative error compared to the exact quantile can be configured with the
    `relativeError` parameter.
    """

    column: str
    quantile: float
    relative_error: float | None = None
    where: str | None = None

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            approx_quantile=proto.ApproxQuantile(
                column=self.column,
                quantile=self.quantile,
                relative_error=self.relative_error,
                where=self.where,
            )
        )


@dataclass
class ApproxQuantiles(AbstractAnalyzer):
    """Computes the approximate quantiles of a column.

    The allowed relative error compared to the exact quantile can be configured with
    `relativeError` parameter.
    """

    column: str
    quantiles: list[float]
    relative_error: float | None = None

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            approx_quantiles=proto.ApproxQuantiles(
                column=self.column,
                quantiles=self.quantiles,
                relative_error=self.relative_error,
            )
        )


@dataclass
class ColumnCount(AbstractAnalyzer):
    """Computes the count of columns."""

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(column_count=proto.ColumnCount())


@dataclass
class Completeness(AbstractAnalyzer):
    """Completeness is the fraction of non-null values in a column."""

    column: str
    where: str | None = None
    options: AnalyzerOptions = AnalyzerOptions.default()

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            completeness=proto.Completeness(
                column=self.column, where=self.where, options=self.options._to_proto()
            )
        )


@dataclass
class Compliance(AbstractAnalyzer):
    """Compliance measures the fraction of rows that complies with the given column constraint.

    E.g if the constraint is "att1>3" and data frame has 5 rows with att1 column value greater
    than 3 and 10 rows under 3; a DoubleMetric would be returned with 0.33 value.
    """

    instance: str
    predicate: str
    where: str | None = None
    columns: list[str] = field(default_factory=list)
    options: AnalyzerOptions = AnalyzerOptions.default()

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            compliance=proto.Compliance(
                instance=self.instance,
                predicate=self.predicate,
                where=self.where,
                columns=self.columns,
                options=self.options._to_proto(),
            )
        )


@dataclass
class Correlation(AbstractAnalyzer):
    """Computes the pearson correlation coefficient between the two given columns."""

    first_column: str
    second_column: str
    where: str | None = None

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            correlation=proto.Correlation(
                first_column=self.first_column,
                second_column=self.second_column,
                where=self.where,
            )
        )


@dataclass
class CountDistinct(AbstractAnalyzer):
    """Counts the distinct elements in the column(s)."""

    columns: list[str] = field(default_factory=list)

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(count_distinct=proto.CountDistinct(columns=self.columns))


@dataclass
class CustomSql(AbstractAnalyzer):
    """Compute the number of rows that match the custom SQL expression."""

    expressions: str

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(custom_sql=proto.CustomSql(expressions=self.expressions))


@dataclass
class DataType(AbstractAnalyzer):
    """Data Type Analyzer. Returns the datatypes of column."""

    column: str
    where: str | None = None

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            data_type=proto.DataType(column=self.column, where=self.where)
        )


@dataclass
class Distinctness(AbstractAnalyzer):
    """Count the distinctness of elements in column(s).

    Distinctness is the fraction of distinct values of a column(s).
    """

    columns: list[str] = field(default_factory=list)
    where: str | None = None

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            distinctness=proto.Distinctness(columns=self.columns, where=self.where)
        )


@dataclass
class Entropy(AbstractAnalyzer):
    """Entropy is a measure of the level of information contained in a message.

    Given the probability distribution over values in a column, it describes
    how many bits are required to identify a value.
    """

    column: str
    where: str | None = None

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            entropy=proto.Entropy(column=self.column, where=self.where)
        )


@dataclass
class ExactQuantile(AbstractAnalyzer):
    """Compute an exact quantile of the given column."""

    column: str
    quantile: float
    where: str | None

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            exact_quantile=proto.ExactQuantile(
                column=self.column, quantile=self.quantile, where=self.where
            )
        )


@dataclass
class Histogram(AbstractAnalyzer):
    """Histogram is the summary of values in a column of a DataFrame.

    It groups the column's values then calculates the number of rows with
    that specific value and the fraction of the value.
    """

    column: str
    max_detail_bin: int | None = None
    where: str | None = None
    compute_frequencies_as_ratio: bool = True
    aggregate_function: AbstractAggregateFunction = CountAggregate()

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            histogram=proto.Histogram(
                column=self.column,
                max_detail_bins=self.max_detail_bin,
                where=self.where,
                compute_frequencies_as_ratio=self.compute_frequencies_as_ratio,
                aggregate_function=self.aggregate_function._to_proto(),
            )
        )


@dataclass
class KLLSketch(AbstractAnalyzer):
    """The KLL Sketch analyzer."""

    column: str
    kll_parameters: KLLParameters | None = None

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            kll_sketch=proto.KLLSketch(
                column=self.column,
                kll_parameters=(
                    self.kll_parameters._to_proto() if self.kll_parameters else None
                ),
            )
        )


@dataclass
class MaxLength(AbstractAnalyzer):
    """MaxLength Analyzer. Get Max length of a str type column."""

    column: str
    where: str | None = None
    options: AnalyzerOptions = AnalyzerOptions.default()

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            max_length=proto.MaxLength(
                column=self.column,
                where=self.where,
                options=self.options._to_proto(),
            )
        )


@dataclass
class Maximum(AbstractAnalyzer):
    """Get the maximum of a numeric column."""

    column: str
    where: str | None = None
    options: AnalyzerOptions = AnalyzerOptions.default()

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            maximum=proto.Maximum(
                column=self.column,
                where=self.where,
                options=self.options._to_proto(),
            )
        )


@dataclass
class Mean(AbstractAnalyzer):
    """Mean Analyzer. Get mean of a column."""

    column: str
    where: str | None = None

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            mean=proto.Mean(
                column=self.column,
                where=self.where,
            )
        )


@dataclass
class MinLength(AbstractAnalyzer):
    """Get the minimum length of a column."""

    column: str
    where: str | None = None
    options: AnalyzerOptions = AnalyzerOptions.default()

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            min_length=proto.MinLength(
                column=self.column,
                where=self.where,
                options=self.options._to_proto(),
            )
        )


@dataclass
class Minimum(AbstractAnalyzer):
    """Get the minimum of a numeric column."""

    column: str
    where: str | None = None
    options: AnalyzerOptions = AnalyzerOptions.default()

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            minimum=proto.Minimum(
                column=self.column,
                where=self.where,
                options=self.options._to_proto(),
            )
        )


@dataclass
class MutualInformation(AbstractAnalyzer):
    """Describes how much information about one column can be inferred from another column."""

    columns: list[str] = field(default_factory=list)
    where: str | None = None

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            mutual_information=proto.MutualInformation(
                columns=self.columns,
                where=self.where,
            )
        )


@dataclass
class PatternMatch(AbstractAnalyzer):
    """PatternMatch is a measure of the fraction of rows that complies with a
    given column regex constraint."""

    column: str
    pattern: str
    where: str | None = None
    options: AnalyzerOptions = AnalyzerOptions.default()

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            pattern_match=proto.PatternMatch(
                column=self.column,
                pattern=self.pattern,
                where=self.where,
                options=self.options._to_proto(),
            )
        )


@dataclass
class RatioOfSums(AbstractAnalyzer):
    """Compute ratio of sums between two columns."""

    numerator: str
    denominator: str
    where: str | None = None

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            ratio_of_sums=proto.RatioOfSums(
                numerator=self.numerator,
                denominator=self.denominator,
                where=self.where,
            )
        )


@dataclass
class Size(AbstractAnalyzer):
    """Size is the number of rows in a DataFrame."""

    where: str | None = None

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(size=proto.Size(where=self.where))


@dataclass
class StandardDeviation(AbstractAnalyzer):
    """Calculates the Standard Deviation of column."""

    column: str
    where: str | None = None

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            standard_deviation=proto.StandardDeviation(
                column=self.column,
                where=self.where,
            )
        )


@dataclass
class Sum(AbstractAnalyzer):
    """Calculates the sum of a column."""

    column: str
    where: str | None = None

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            sum=proto.Sum(
                column=self.column,
                where=self.where,
            )
        )


@dataclass
class UniqueValueRatio(AbstractAnalyzer):
    """Compute the ratio of uniqu values for columns."""

    columns: list[str] = field(default_factory=list)
    where: str | None = None
    options: AnalyzerOptions = AnalyzerOptions.default()

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            unique_value_ratio=proto.UniqueValueRatio(
                columns=self.columns,
                where=self.where,
                options=self.options._to_proto(),
            )
        )


@dataclass
class Uniqueness(AbstractAnalyzer):
    """Compute the uniqueness of the columns."""

    columns: list[str] = field(default_factory=list)
    where: str | None = None
    options: AnalyzerOptions = AnalyzerOptions.default()

    def _to_proto(self) -> proto.Analyzer:
        return proto.Analyzer(
            uniqueness=proto.Uniqueness(
                columns=self.columns,
                where=self.where,
                options=self.options._to_proto(),
            )
        )


class ConstraintBuilder:
    def __init__(self) -> None:
        self._analyzer: AbstractAnalyzer | None = None
        self._is_long: bool = False
        self._expected_value: float | int | None = None
        self._sign: suite.Check.ComparisonSign | None = None
        self._hint: str | None = None
        self._name: str | None = None

    def for_analyzer(self, analyzer: AbstractAnalyzer) -> Self:
        """Set an analyzer."""

        self._analyzer = analyzer
        return self

    def with_name(self, name: str) -> Self:
        """Set a name of the constraint."""

        self._name = name
        return self

    def with_hint(self, hint: str) -> Self:
        """Set a hint for the constraint.

        Hint can be helpful in the case when one needs
        to realize the reason of the constraint or why did it fail.
        """

        self._hint = hint
        return self

    @singledispatchmethod
    def should_be_gt_than(self, value) -> Self:
        """Add an assertion that metric > value.

        This result of this methods depends of the passed type!
        """
        ...

    @should_be_gt_than.register
    def _(self, value: int) -> Self:
        self._sign = suite.Check.ComparisonSign.GT
        self._is_long = True
        self._expected_value = value
        return self

    @should_be_gt_than.register
    def _(self, value: float) -> Self:
        self._sign = suite.Check.ComparisonSign.GT
        self._is_long = False
        self._expected_value = value
        return self

    @singledispatchmethod
    def should_be_geq_than(self, value) -> Self:
        """Add an assertion that metric >= value.

        This result of this methods depends of the passed type!
        """
        ...

    @should_be_geq_than.register
    def _(self, value: int) -> Self:
        self._sign = suite.Check.ComparisonSign.GET
        self._is_long = True
        self._expected_value = value
        return self

    @should_be_geq_than.register
    def _(self, value: float) -> Self:
        self._sign = suite.Check.ComparisonSign.GET
        self._is_long = False
        self._expected_value = value
        return self

    @singledispatchmethod
    def should_be_eq_to(self, value) -> Self:
        """Add an assertion that metric == value.

        This result of this methods depends of the passed type!
        """
        ...

    @should_be_eq_to.register
    def _(self, value: int) -> Self:
        self._sign = suite.Check.ComparisonSign.EQ
        self._is_long = True
        self._expected_value = value
        return self

    @should_be_eq_to.register
    def _(self, value: float) -> Self:
        self._sign = suite.Check.ComparisonSign.EQ
        self._is_long = False
        self._expected_value = value
        return self

    @singledispatchmethod
    def should_be_lt_than(self, value) -> Self:
        """Add an assertion that metric < value.

        This result of this methods depends of the passed type!
        """
        ...

    @should_be_lt_than.register
    def _(self, value: int) -> Self:
        self._sign = suite.Check.ComparisonSign.LT
        self._is_long = True
        self._expected_value = value
        return self

    @should_be_lt_than.register
    def _(self, value: float) -> Self:
        self._sign = suite.Check.ComparisonSign.LT
        self._is_long = False
        self._expected_value = value
        return self

    @singledispatchmethod
    def should_be_leq_than(self, value) -> Self:
        """Add an assertion that metric <= value.

        This result of this methods depends of the passed type!
        """
        ...

    @should_be_leq_than.register
    def _(self, value: int) -> Self:
        self._sign = suite.Check.ComparisonSign.LET
        self._is_long = True
        self._expected_value = value
        return self

    @should_be_leq_than.register
    def _(self, value: float) -> Self:
        self._sign = suite.Check.ComparisonSign.LET
        self._is_long = False
        self._expected_value = value
        return self

    def _validate(self) -> None:
        if self._analyzer is None:
            raise ValueError("Analyzer is not set")
        if self._expected_value is None:
            raise ValueError("Expected value is not set")

    def build(self) -> suite.Check.Constraint:
        self._validate()

        # for mypy
        assert self._analyzer is not None
        assert self._expected_value is not None

        if self._is_long:
            # for mypy
            assert isinstance(self._expected_value, int)

            return suite.Check.Constraint(
                analyzer=self._analyzer._to_proto(),
                long_expectation=self._expected_value,
                sign=self._sign,
                hint=self._hint,
                name=self._name,
            )
        else:
            # for mypy
            assert isinstance(self._expected_value, float)

            return suite.Check.Constraint(
                analyzer=self._analyzer._to_proto(),
                double_expectation=self._expected_value,
                sign=self._sign,
                hint=self._hint,
                name=self._name,
            )
