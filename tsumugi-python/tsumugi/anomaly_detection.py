from abc import ABC, abstractmethod
from dataclasses import dataclass

from typing_extensions import Self

from .analyzers import AbstractAnalyzer
from .enums import CheckLevel
from .proto import strategies_pb2 as strategies
from .proto import suite_pb2 as suite


class AbstractStrategy(ABC):
    @abstractmethod
    def _to_proto(self) -> strategies.AnomalyDetectionStrategy: ...


@dataclass
class AbsoluteChangeStrategt(AbstractStrategy):
    max_rate_decrease: float
    max_rate_increase: float
    order: int | None = None

    def _to_proto(self) -> strategies.AnomalyDetectionStrategy:
        return strategies.AnomalyDetectionStrategy(
            absolute_change_strategy=strategies.AbsoluteChangeStrategy(
                max_rate_decrease=self.max_rate_decrease,
                max_rate_increase=self.max_rate_increase,
                order=self.order,
            )
        )


@dataclass
class BatchNormalStrategy(AbstractStrategy):
    lower_deviation_factor: float
    upper_deviation_factor: float
    include_interval: bool = False

    def _to_proto(self) -> strategies.AnomalyDetectionStrategy:
        return strategies.AnomalyDetectionStrategy(
            batch_normal_strategy=strategies.BatchNormalStrategy(
                lower_deviation_factor=self.lower_deviation_factor,
                upper_deviation_factor=self.upper_deviation_factor,
                include_interval=self.include_interval,
            )
        )


@dataclass
class OnlineNormalStrategy(AbstractStrategy):
    lower_deviation_factor: float
    upper_deviation_factor: float
    ignore_start_percentage: float | None = None
    ignore_anomalies: bool = True

    def _to_proto(self) -> strategies.AnomalyDetectionStrategy:
        return strategies.AnomalyDetectionStrategy(
            online_normal_strategy=strategies.OnlineNormalStrategy(
                lower_deviation_factor=self.lower_deviation_factor,
                upper_deviation_factor=self.upper_deviation_factor,
                ignore_start_percentage=self.ignore_start_percentage,
                ignore_anomalies=self.ignore_anomalies,
            )
        )


@dataclass
class RelativeRateOfChange(AbstractStrategy):
    max_rate_decrease: float
    max_rate_increase: float
    order: int | None = None

    def _to_proto(self) -> strategies.AnomalyDetectionStrategy:
        return strategies.AnomalyDetectionStrategy(
            relative_rate_of_change_strategy=strategies.RelativeRateOfChangeStrategy(
                max_rate_decrease=self.max_rate_decrease,
                max_rate_increase=self.max_rate_increase,
                order=self.order,
            )
        )


@dataclass
class SimpleThresholdsStrategy(AbstractStrategy):
    lower_bound: float
    upper_bound: float

    def _to_proto(self) -> strategies.AnomalyDetectionStrategy:
        return strategies.AnomalyDetectionStrategy(
            simple_thresholds_strategy=strategies.SimpleThresholdStrategy(
                lower_bound=self.lower_bound,
                upper_bound=self.upper_bound,
            )
        )


class AnomalyDetectionBuilder:
    """Helper object to build AnomalyDetection check."""

    def __init__(self) -> None:
        self._strategy: AbstractStrategy | None = None
        self._analyzer: AbstractAnalyzer | None = None
        self._check_level: CheckLevel = CheckLevel.Warning
        self._description: str = ""
        self._with_tag_values: dict[str, str] = dict()
        self._after_date: int | None = None
        self._before_date: int | None = None

    def for_analyzer(self, analyzer: AbstractAnalyzer) -> Self:
        """Add an analyzer."""

        self._analyzer = analyzer
        return self

    def with_strategy(self, strategy: AbstractStrategy) -> Self:
        """Add a strategy."""

        self._strategy = strategy
        return self

    def with_check_level(self, level: CheckLevel) -> Self:
        """Set a severity level."""

        self._check_level = level
        return self

    def with_description(self, description: str) -> Self:
        """Add a description."""

        self._description = description
        return self

    def with_tags(self, tags: dict[str, str]) -> Self:
        """Add tags."""

        self._with_tag_values = tags
        return self

    def after_date(self, dt: int) -> Self:
        """Set a minimal dataset date value

        This value will be used to filter out part of
        the timeseries of metrics.
        """
        self._after_date = dt
        return self

    def before_date(self, dt: int) -> Self:
        """Set a maximal dataset date value

        This value will be used to filter out part of
        the timeseries of metrics.
        """

        self._before_date = dt
        return self

    def _validate(self) -> None:
        if self._analyzer is None:
            raise ValueError("Analyzer is not set")
        if self._strategy is None:
            raise ValueError("Strategy is not set")

    def build(self) -> suite.AnomalyDetection:
        self._validate()

        # for mypy
        assert self._strategy is not None
        assert self._analyzer is not None

        return suite.AnomalyDetection(
            anomaly_detection_strategy=self._strategy._to_proto(),
            analyzer=self._analyzer._to_proto(),
            config=suite.AnomalyDetection.AnomalyCheckConfig(
                level=self._check_level._to_proto(),
                description=self._description,
                with_tag_values=self._with_tag_values,
                after_date=self._after_date,
                before_date=self._before_date,
            ),
        )
