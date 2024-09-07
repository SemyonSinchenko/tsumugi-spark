from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass
from .proto import analyzers_pb2 as proto


class AbstractAnalyzer(ABC):
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

    def _to_proto(self) -> proto.AnalyzerOptions:
        return proto.AnalyzerOptions(
            null_behaviour=self.null_behaviour.value,
            filtered_row_outcome=self.filtered_row_outcome.value,
        )


@dataclass
class ApproxCountDistinct(AbstractAnalyzer):
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
