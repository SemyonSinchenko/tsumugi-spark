import analyzers_pb2 as _analyzers_pb2
import strategies_pb2 as _strategies_pb2
import repository_pb2 as _repository_pb2
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

class CheckLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Error: _ClassVar[CheckLevel]
    Warning: _ClassVar[CheckLevel]

Error: CheckLevel
Warning: CheckLevel

class Check(_message.Message):
    __slots__ = ("checkLevel", "description", "constraints")
    class ComparisonSign(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GT: _ClassVar[Check.ComparisonSign]
        GET: _ClassVar[Check.ComparisonSign]
        EQ: _ClassVar[Check.ComparisonSign]
        LT: _ClassVar[Check.ComparisonSign]
        LET: _ClassVar[Check.ComparisonSign]

    GT: Check.ComparisonSign
    GET: Check.ComparisonSign
    EQ: Check.ComparisonSign
    LT: Check.ComparisonSign
    LET: Check.ComparisonSign
    class Constraint(_message.Message):
        __slots__ = (
            "analyzer",
            "long_expectation",
            "double_expectation",
            "sign",
            "hint",
            "name",
        )
        ANALYZER_FIELD_NUMBER: _ClassVar[int]
        LONG_EXPECTATION_FIELD_NUMBER: _ClassVar[int]
        DOUBLE_EXPECTATION_FIELD_NUMBER: _ClassVar[int]
        SIGN_FIELD_NUMBER: _ClassVar[int]
        HINT_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        analyzer: _analyzers_pb2.Analyzer
        long_expectation: int
        double_expectation: float
        sign: Check.ComparisonSign
        hint: str
        name: str
        def __init__(
            self,
            analyzer: _Optional[_Union[_analyzers_pb2.Analyzer, _Mapping]] = ...,
            long_expectation: _Optional[int] = ...,
            double_expectation: _Optional[float] = ...,
            sign: _Optional[_Union[Check.ComparisonSign, str]] = ...,
            hint: _Optional[str] = ...,
            name: _Optional[str] = ...,
        ) -> None: ...

    CHECKLEVEL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    checkLevel: CheckLevel
    description: str
    constraints: _containers.RepeatedCompositeFieldContainer[Check.Constraint]
    def __init__(
        self,
        checkLevel: _Optional[_Union[CheckLevel, str]] = ...,
        description: _Optional[str] = ...,
        constraints: _Optional[_Iterable[_Union[Check.Constraint, _Mapping]]] = ...,
    ) -> None: ...

class AnomalyDetection(_message.Message):
    __slots__ = ("anomaly_detection_strategy", "analyzer", "config")
    class AnomalyCheckConfig(_message.Message):
        __slots__ = (
            "level",
            "description",
            "with_tag_values",
            "after_date",
            "before_date",
        )
        class WithTagValuesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(
                self, key: _Optional[str] = ..., value: _Optional[str] = ...
            ) -> None: ...

        LEVEL_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        WITH_TAG_VALUES_FIELD_NUMBER: _ClassVar[int]
        AFTER_DATE_FIELD_NUMBER: _ClassVar[int]
        BEFORE_DATE_FIELD_NUMBER: _ClassVar[int]
        level: CheckLevel
        description: str
        with_tag_values: _containers.ScalarMap[str, str]
        after_date: int
        before_date: int
        def __init__(
            self,
            level: _Optional[_Union[CheckLevel, str]] = ...,
            description: _Optional[str] = ...,
            with_tag_values: _Optional[_Mapping[str, str]] = ...,
            after_date: _Optional[int] = ...,
            before_date: _Optional[int] = ...,
        ) -> None: ...

    ANOMALY_DETECTION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    ANALYZER_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    anomaly_detection_strategy: _strategies_pb2.AnomalyDetectionStrategy
    analyzer: _analyzers_pb2.Analyzer
    config: AnomalyDetection.AnomalyCheckConfig
    def __init__(
        self,
        anomaly_detection_strategy: _Optional[
            _Union[_strategies_pb2.AnomalyDetectionStrategy, _Mapping]
        ] = ...,
        analyzer: _Optional[_Union[_analyzers_pb2.Analyzer, _Mapping]] = ...,
        config: _Optional[_Union[AnomalyDetection.AnomalyCheckConfig, _Mapping]] = ...,
    ) -> None: ...

class VerificationSuite(_message.Message):
    __slots__ = (
        "data",
        "checks",
        "required_analyzers",
        "repository",
        "result_key",
        "anomaly_detections",
        "compute_row_level_results",
    )
    DATA_FIELD_NUMBER: _ClassVar[int]
    CHECKS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ANALYZERS_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    RESULT_KEY_FIELD_NUMBER: _ClassVar[int]
    ANOMALY_DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_ROW_LEVEL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    checks: _containers.RepeatedCompositeFieldContainer[Check]
    required_analyzers: _containers.RepeatedCompositeFieldContainer[
        _analyzers_pb2.Analyzer
    ]
    repository: _repository_pb2.Repository
    result_key: _repository_pb2.ResultKey
    anomaly_detections: _containers.RepeatedCompositeFieldContainer[AnomalyDetection]
    compute_row_level_results: bool
    def __init__(
        self,
        data: _Optional[bytes] = ...,
        checks: _Optional[_Iterable[_Union[Check, _Mapping]]] = ...,
        required_analyzers: _Optional[
            _Iterable[_Union[_analyzers_pb2.Analyzer, _Mapping]]
        ] = ...,
        repository: _Optional[_Union[_repository_pb2.Repository, _Mapping]] = ...,
        result_key: _Optional[_Union[_repository_pb2.ResultKey, _Mapping]] = ...,
        anomaly_detections: _Optional[
            _Iterable[_Union[AnomalyDetection, _Mapping]]
        ] = ...,
        compute_row_level_results: bool = ...,
    ) -> None: ...
