from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class Analyzer(_message.Message):
    __slots__ = (
        "approx_count_distinct",
        "approx_quantile",
        "approx_quantiles",
        "column_count",
        "completeness",
        "compliance",
        "correlation",
        "count_distinct",
        "custom_sql",
        "data_type",
        "distinctness",
        "entropy",
        "exact_quantile",
        "histogram",
        "kll_sketch",
        "max_length",
        "maximum",
        "mean",
        "min_length",
        "minimum",
        "mutual_information",
        "pattern_match",
        "ratio_of_sums",
        "size",
        "standard_deviation",
        "sum",
        "unique_value_ratio",
        "uniqueness",
    )
    APPROX_COUNT_DISTINCT_FIELD_NUMBER: _ClassVar[int]
    APPROX_QUANTILE_FIELD_NUMBER: _ClassVar[int]
    APPROX_QUANTILES_FIELD_NUMBER: _ClassVar[int]
    COLUMN_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMPLETENESS_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_FIELD_NUMBER: _ClassVar[int]
    COUNT_DISTINCT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SQL_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISTINCTNESS_FIELD_NUMBER: _ClassVar[int]
    ENTROPY_FIELD_NUMBER: _ClassVar[int]
    EXACT_QUANTILE_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    KLL_SKETCH_FIELD_NUMBER: _ClassVar[int]
    MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    MEAN_FIELD_NUMBER: _ClassVar[int]
    MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MUTUAL_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    PATTERN_MATCH_FIELD_NUMBER: _ClassVar[int]
    RATIO_OF_SUMS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    STANDARD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_VALUE_RATIO_FIELD_NUMBER: _ClassVar[int]
    UNIQUENESS_FIELD_NUMBER: _ClassVar[int]
    approx_count_distinct: ApproxCountDistinct
    approx_quantile: ApproxQuantile
    approx_quantiles: ApproxQuantiles
    column_count: ColumnCount
    completeness: Completeness
    compliance: Compliance
    correlation: Correlation
    count_distinct: CountDistinct
    custom_sql: CustomSql
    data_type: DataType
    distinctness: Distinctness
    entropy: Entropy
    exact_quantile: ExactQuantile
    histogram: Histogram
    kll_sketch: KLLSketch
    max_length: MaxLength
    maximum: Maximum
    mean: Mean
    min_length: MinLength
    minimum: Minimum
    mutual_information: MutualInformation
    pattern_match: PatternMatch
    ratio_of_sums: RatioOfSums
    size: Size
    standard_deviation: StandardDeviation
    sum: Sum
    unique_value_ratio: UniqueValueRatio
    uniqueness: Uniqueness
    def __init__(
        self,
        approx_count_distinct: _Optional[_Union[ApproxCountDistinct, _Mapping]] = ...,
        approx_quantile: _Optional[_Union[ApproxQuantile, _Mapping]] = ...,
        approx_quantiles: _Optional[_Union[ApproxQuantiles, _Mapping]] = ...,
        column_count: _Optional[_Union[ColumnCount, _Mapping]] = ...,
        completeness: _Optional[_Union[Completeness, _Mapping]] = ...,
        compliance: _Optional[_Union[Compliance, _Mapping]] = ...,
        correlation: _Optional[_Union[Correlation, _Mapping]] = ...,
        count_distinct: _Optional[_Union[CountDistinct, _Mapping]] = ...,
        custom_sql: _Optional[_Union[CustomSql, _Mapping]] = ...,
        data_type: _Optional[_Union[DataType, _Mapping]] = ...,
        distinctness: _Optional[_Union[Distinctness, _Mapping]] = ...,
        entropy: _Optional[_Union[Entropy, _Mapping]] = ...,
        exact_quantile: _Optional[_Union[ExactQuantile, _Mapping]] = ...,
        histogram: _Optional[_Union[Histogram, _Mapping]] = ...,
        kll_sketch: _Optional[_Union[KLLSketch, _Mapping]] = ...,
        max_length: _Optional[_Union[MaxLength, _Mapping]] = ...,
        maximum: _Optional[_Union[Maximum, _Mapping]] = ...,
        mean: _Optional[_Union[Mean, _Mapping]] = ...,
        min_length: _Optional[_Union[MinLength, _Mapping]] = ...,
        minimum: _Optional[_Union[Minimum, _Mapping]] = ...,
        mutual_information: _Optional[_Union[MutualInformation, _Mapping]] = ...,
        pattern_match: _Optional[_Union[PatternMatch, _Mapping]] = ...,
        ratio_of_sums: _Optional[_Union[RatioOfSums, _Mapping]] = ...,
        size: _Optional[_Union[Size, _Mapping]] = ...,
        standard_deviation: _Optional[_Union[StandardDeviation, _Mapping]] = ...,
        sum: _Optional[_Union[Sum, _Mapping]] = ...,
        unique_value_ratio: _Optional[_Union[UniqueValueRatio, _Mapping]] = ...,
        uniqueness: _Optional[_Union[Uniqueness, _Mapping]] = ...,
    ) -> None: ...

class AnalyzerOptions(_message.Message):
    __slots__ = ("null_behaviour", "filtered_row_outcome")
    class NullBehaviour(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Ignore: _ClassVar[AnalyzerOptions.NullBehaviour]
        EmptyString: _ClassVar[AnalyzerOptions.NullBehaviour]
        Fail: _ClassVar[AnalyzerOptions.NullBehaviour]

    Ignore: AnalyzerOptions.NullBehaviour
    EmptyString: AnalyzerOptions.NullBehaviour
    Fail: AnalyzerOptions.NullBehaviour
    class FilteredRowOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NULL: _ClassVar[AnalyzerOptions.FilteredRowOutcome]
        TRUE: _ClassVar[AnalyzerOptions.FilteredRowOutcome]

    NULL: AnalyzerOptions.FilteredRowOutcome
    TRUE: AnalyzerOptions.FilteredRowOutcome
    NULL_BEHAVIOUR_FIELD_NUMBER: _ClassVar[int]
    FILTERED_ROW_OUTCOME_FIELD_NUMBER: _ClassVar[int]
    null_behaviour: AnalyzerOptions.NullBehaviour
    filtered_row_outcome: AnalyzerOptions.FilteredRowOutcome
    def __init__(
        self,
        null_behaviour: _Optional[_Union[AnalyzerOptions.NullBehaviour, str]] = ...,
        filtered_row_outcome: _Optional[
            _Union[AnalyzerOptions.FilteredRowOutcome, str]
        ] = ...,
    ) -> None: ...

class ApproxCountDistinct(_message.Message):
    __slots__ = ("column", "where")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    column: str
    where: str
    def __init__(
        self, column: _Optional[str] = ..., where: _Optional[str] = ...
    ) -> None: ...

class ApproxQuantile(_message.Message):
    __slots__ = ("column", "quantile", "relative_error", "where")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    QUANTILE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ERROR_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    column: str
    quantile: float
    relative_error: float
    where: str
    def __init__(
        self,
        column: _Optional[str] = ...,
        quantile: _Optional[float] = ...,
        relative_error: _Optional[float] = ...,
        where: _Optional[str] = ...,
    ) -> None: ...

class ApproxQuantiles(_message.Message):
    __slots__ = ("column", "quantiles", "relative_error")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    QUANTILES_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ERROR_FIELD_NUMBER: _ClassVar[int]
    column: str
    quantiles: _containers.RepeatedScalarFieldContainer[float]
    relative_error: float
    def __init__(
        self,
        column: _Optional[str] = ...,
        quantiles: _Optional[_Iterable[float]] = ...,
        relative_error: _Optional[float] = ...,
    ) -> None: ...

class ColumnCount(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Completeness(_message.Message):
    __slots__ = ("column", "where", "options")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    column: str
    where: str
    options: AnalyzerOptions
    def __init__(
        self,
        column: _Optional[str] = ...,
        where: _Optional[str] = ...,
        options: _Optional[_Union[AnalyzerOptions, _Mapping]] = ...,
    ) -> None: ...

class Compliance(_message.Message):
    __slots__ = ("instance", "predicate", "where", "columns", "options")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PREDICATE_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    instance: str
    predicate: str
    where: str
    columns: _containers.RepeatedScalarFieldContainer[str]
    options: AnalyzerOptions
    def __init__(
        self,
        instance: _Optional[str] = ...,
        predicate: _Optional[str] = ...,
        where: _Optional[str] = ...,
        columns: _Optional[_Iterable[str]] = ...,
        options: _Optional[_Union[AnalyzerOptions, _Mapping]] = ...,
    ) -> None: ...

class Correlation(_message.Message):
    __slots__ = ("first_column", "second_column", "where")
    FIRST_COLUMN_FIELD_NUMBER: _ClassVar[int]
    SECOND_COLUMN_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    first_column: str
    second_column: str
    where: str
    def __init__(
        self,
        first_column: _Optional[str] = ...,
        second_column: _Optional[str] = ...,
        where: _Optional[str] = ...,
    ) -> None: ...

class CountDistinct(_message.Message):
    __slots__ = ("columns",)
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, columns: _Optional[_Iterable[str]] = ...) -> None: ...

class CustomSql(_message.Message):
    __slots__ = ("expressions",)
    EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    expressions: str
    def __init__(self, expressions: _Optional[str] = ...) -> None: ...

class DataType(_message.Message):
    __slots__ = ("column", "where")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    column: str
    where: str
    def __init__(
        self, column: _Optional[str] = ..., where: _Optional[str] = ...
    ) -> None: ...

class Distinctness(_message.Message):
    __slots__ = ("columns", "where")
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedScalarFieldContainer[str]
    where: str
    def __init__(
        self, columns: _Optional[_Iterable[str]] = ..., where: _Optional[str] = ...
    ) -> None: ...

class Entropy(_message.Message):
    __slots__ = ("column", "where")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    column: str
    where: str
    def __init__(
        self, column: _Optional[str] = ..., where: _Optional[str] = ...
    ) -> None: ...

class ExactQuantile(_message.Message):
    __slots__ = ("column", "quantile", "where")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    QUANTILE_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    column: str
    quantile: float
    where: str
    def __init__(
        self,
        column: _Optional[str] = ...,
        quantile: _Optional[float] = ...,
        where: _Optional[str] = ...,
    ) -> None: ...

class Histogram(_message.Message):
    __slots__ = (
        "column",
        "max_detail_bins",
        "where",
        "compute_frequencies_as_ratio",
        "aggregate_function",
    )
    class AggregateFunction(_message.Message):
        __slots__ = ("count_aggregate", "sum_aggregate")
        class Count(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class Sum(_message.Message):
            __slots__ = ("agg_column",)
            AGG_COLUMN_FIELD_NUMBER: _ClassVar[int]
            agg_column: str
            def __init__(self, agg_column: _Optional[str] = ...) -> None: ...

        COUNT_AGGREGATE_FIELD_NUMBER: _ClassVar[int]
        SUM_AGGREGATE_FIELD_NUMBER: _ClassVar[int]
        count_aggregate: Histogram.AggregateFunction.Count
        sum_aggregate: Histogram.AggregateFunction.Sum
        def __init__(
            self,
            count_aggregate: _Optional[
                _Union[Histogram.AggregateFunction.Count, _Mapping]
            ] = ...,
            sum_aggregate: _Optional[
                _Union[Histogram.AggregateFunction.Sum, _Mapping]
            ] = ...,
        ) -> None: ...

    COLUMN_FIELD_NUMBER: _ClassVar[int]
    MAX_DETAIL_BINS_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_FREQUENCIES_AS_RATIO_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    column: str
    max_detail_bins: int
    where: str
    compute_frequencies_as_ratio: bool
    aggregate_function: Histogram.AggregateFunction
    def __init__(
        self,
        column: _Optional[str] = ...,
        max_detail_bins: _Optional[int] = ...,
        where: _Optional[str] = ...,
        compute_frequencies_as_ratio: bool = ...,
        aggregate_function: _Optional[
            _Union[Histogram.AggregateFunction, _Mapping]
        ] = ...,
    ) -> None: ...

class KLLSketch(_message.Message):
    __slots__ = ("column", "kll_parameters")
    class KLLParameters(_message.Message):
        __slots__ = ("sketch_size", "shrinking_factor", "number_of_buckets")
        SKETCH_SIZE_FIELD_NUMBER: _ClassVar[int]
        SHRINKING_FACTOR_FIELD_NUMBER: _ClassVar[int]
        NUMBER_OF_BUCKETS_FIELD_NUMBER: _ClassVar[int]
        sketch_size: int
        shrinking_factor: float
        number_of_buckets: int
        def __init__(
            self,
            sketch_size: _Optional[int] = ...,
            shrinking_factor: _Optional[float] = ...,
            number_of_buckets: _Optional[int] = ...,
        ) -> None: ...

    COLUMN_FIELD_NUMBER: _ClassVar[int]
    KLL_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    column: str
    kll_parameters: KLLSketch.KLLParameters
    def __init__(
        self,
        column: _Optional[str] = ...,
        kll_parameters: _Optional[_Union[KLLSketch.KLLParameters, _Mapping]] = ...,
    ) -> None: ...

class MaxLength(_message.Message):
    __slots__ = ("column", "where", "options")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    column: str
    where: str
    options: AnalyzerOptions
    def __init__(
        self,
        column: _Optional[str] = ...,
        where: _Optional[str] = ...,
        options: _Optional[_Union[AnalyzerOptions, _Mapping]] = ...,
    ) -> None: ...

class Maximum(_message.Message):
    __slots__ = ("column", "where", "options")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    column: str
    where: str
    options: AnalyzerOptions
    def __init__(
        self,
        column: _Optional[str] = ...,
        where: _Optional[str] = ...,
        options: _Optional[_Union[AnalyzerOptions, _Mapping]] = ...,
    ) -> None: ...

class Mean(_message.Message):
    __slots__ = ("column", "where")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    column: str
    where: str
    def __init__(
        self, column: _Optional[str] = ..., where: _Optional[str] = ...
    ) -> None: ...

class MinLength(_message.Message):
    __slots__ = ("column", "where", "options")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    column: str
    where: str
    options: AnalyzerOptions
    def __init__(
        self,
        column: _Optional[str] = ...,
        where: _Optional[str] = ...,
        options: _Optional[_Union[AnalyzerOptions, _Mapping]] = ...,
    ) -> None: ...

class Minimum(_message.Message):
    __slots__ = ("column", "where", "options")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    column: str
    where: str
    options: AnalyzerOptions
    def __init__(
        self,
        column: _Optional[str] = ...,
        where: _Optional[str] = ...,
        options: _Optional[_Union[AnalyzerOptions, _Mapping]] = ...,
    ) -> None: ...

class MutualInformation(_message.Message):
    __slots__ = ("columns", "where")
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedScalarFieldContainer[str]
    where: str
    def __init__(
        self, columns: _Optional[_Iterable[str]] = ..., where: _Optional[str] = ...
    ) -> None: ...

class PatternMatch(_message.Message):
    __slots__ = ("column", "pattern", "where", "options")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    column: str
    pattern: str
    where: str
    options: AnalyzerOptions
    def __init__(
        self,
        column: _Optional[str] = ...,
        pattern: _Optional[str] = ...,
        where: _Optional[str] = ...,
        options: _Optional[_Union[AnalyzerOptions, _Mapping]] = ...,
    ) -> None: ...

class RatioOfSums(_message.Message):
    __slots__ = ("numerator", "denominator", "where")
    NUMERATOR_FIELD_NUMBER: _ClassVar[int]
    DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    numerator: str
    denominator: str
    where: str
    def __init__(
        self,
        numerator: _Optional[str] = ...,
        denominator: _Optional[str] = ...,
        where: _Optional[str] = ...,
    ) -> None: ...

class Size(_message.Message):
    __slots__ = ("where",)
    WHERE_FIELD_NUMBER: _ClassVar[int]
    where: str
    def __init__(self, where: _Optional[str] = ...) -> None: ...

class StandardDeviation(_message.Message):
    __slots__ = ("column", "where")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    column: str
    where: str
    def __init__(
        self, column: _Optional[str] = ..., where: _Optional[str] = ...
    ) -> None: ...

class Sum(_message.Message):
    __slots__ = ("column", "where")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    column: str
    where: str
    def __init__(
        self, column: _Optional[str] = ..., where: _Optional[str] = ...
    ) -> None: ...

class UniqueValueRatio(_message.Message):
    __slots__ = ("columns", "where", "options")
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedScalarFieldContainer[str]
    where: str
    options: AnalyzerOptions
    def __init__(
        self,
        columns: _Optional[_Iterable[str]] = ...,
        where: _Optional[str] = ...,
        options: _Optional[_Union[AnalyzerOptions, _Mapping]] = ...,
    ) -> None: ...

class Uniqueness(_message.Message):
    __slots__ = ("columns", "where", "options")
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedScalarFieldContainer[str]
    where: str
    options: AnalyzerOptions
    def __init__(
        self,
        columns: _Optional[_Iterable[str]] = ...,
        where: _Optional[str] = ...,
        options: _Optional[_Union[AnalyzerOptions, _Mapping]] = ...,
    ) -> None: ...
