# Docstring of classes were heavily inspired by the
# docstring from https://github.com/awslabs/python-deequ/blob/master/pydeequ/analyzers.py

from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass
from .proto import analyzers_pb2 as proto


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


@dataclass
class AnalyzerOptions:
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
