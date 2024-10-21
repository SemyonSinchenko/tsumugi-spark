from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class Repository(_message.Message):
    __slots__ = ("file_system", "spark_table")
    FILE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    SPARK_TABLE_FIELD_NUMBER: _ClassVar[int]
    file_system: FileSystemRepository
    spark_table: SparkTableRepository
    def __init__(
        self,
        file_system: _Optional[_Union[FileSystemRepository, _Mapping]] = ...,
        spark_table: _Optional[_Union[SparkTableRepository, _Mapping]] = ...,
    ) -> None: ...

class FileSystemRepository(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class SparkTableRepository(_message.Message):
    __slots__ = ("table_name",)
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    def __init__(self, table_name: _Optional[str] = ...) -> None: ...

class ResultKey(_message.Message):
    __slots__ = ("dataset_date", "tags")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    DATASET_DATE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    dataset_date: int
    tags: _containers.ScalarMap[str, str]
    def __init__(
        self,
        dataset_date: _Optional[int] = ...,
        tags: _Optional[_Mapping[str, str]] = ...,
    ) -> None: ...
