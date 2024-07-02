from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnomalyDetectionStrategy(_message.Message):
    __slots__ = ("absolute_change_strategy", "batch_normal_strategy", "online_normal_strategy", "relative_rate_of_change_strategy", "simple_thresholds_strategy")
    ABSOLUTE_CHANGE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    BATCH_NORMAL_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    ONLINE_NORMAL_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_RATE_OF_CHANGE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_THRESHOLDS_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    absolute_change_strategy: AbsoluteChangeStrategy
    batch_normal_strategy: BatchNormalStrategy
    online_normal_strategy: OnlineNormalStrategy
    relative_rate_of_change_strategy: RelativeRateOfChangeStrategy
    simple_thresholds_strategy: SimpleThresholdStrategy
    def __init__(self, absolute_change_strategy: _Optional[_Union[AbsoluteChangeStrategy, _Mapping]] = ..., batch_normal_strategy: _Optional[_Union[BatchNormalStrategy, _Mapping]] = ..., online_normal_strategy: _Optional[_Union[OnlineNormalStrategy, _Mapping]] = ..., relative_rate_of_change_strategy: _Optional[_Union[RelativeRateOfChangeStrategy, _Mapping]] = ..., simple_thresholds_strategy: _Optional[_Union[SimpleThresholdStrategy, _Mapping]] = ...) -> None: ...

class AbsoluteChangeStrategy(_message.Message):
    __slots__ = ("max_rate_decrease", "max_rate_increase", "order")
    MAX_RATE_DECREASE_FIELD_NUMBER: _ClassVar[int]
    MAX_RATE_INCREASE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    max_rate_decrease: float
    max_rate_increase: float
    order: int
    def __init__(self, max_rate_decrease: _Optional[float] = ..., max_rate_increase: _Optional[float] = ..., order: _Optional[int] = ...) -> None: ...

class BatchNormalStrategy(_message.Message):
    __slots__ = ("lower_deviation_factor", "upper_deviation_factor", "include_interval")
    LOWER_DEVIATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    UPPER_DEVIATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    lower_deviation_factor: float
    upper_deviation_factor: float
    include_interval: bool
    def __init__(self, lower_deviation_factor: _Optional[float] = ..., upper_deviation_factor: _Optional[float] = ..., include_interval: bool = ...) -> None: ...

class OnlineNormalStrategy(_message.Message):
    __slots__ = ("lower_deviation_factor", "upper_deviation_factor", "ignore_start_percentage", "ignore_anomalies")
    LOWER_DEVIATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    UPPER_DEVIATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    IGNORE_START_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ANOMALIES_FIELD_NUMBER: _ClassVar[int]
    lower_deviation_factor: float
    upper_deviation_factor: float
    ignore_start_percentage: float
    ignore_anomalies: bool
    def __init__(self, lower_deviation_factor: _Optional[float] = ..., upper_deviation_factor: _Optional[float] = ..., ignore_start_percentage: _Optional[float] = ..., ignore_anomalies: bool = ...) -> None: ...

class RelativeRateOfChangeStrategy(_message.Message):
    __slots__ = ("max_rate_decrease", "max_rate_increase", "order")
    MAX_RATE_DECREASE_FIELD_NUMBER: _ClassVar[int]
    MAX_RATE_INCREASE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    max_rate_decrease: float
    max_rate_increase: float
    order: int
    def __init__(self, max_rate_decrease: _Optional[float] = ..., max_rate_increase: _Optional[float] = ..., order: _Optional[int] = ...) -> None: ...

class SimpleThresholdStrategy(_message.Message):
    __slots__ = ("lower_bound", "upper_bound")
    LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    lower_bound: float
    upper_bound: float
    def __init__(self, lower_bound: _Optional[float] = ..., upper_bound: _Optional[float] = ...) -> None: ...
