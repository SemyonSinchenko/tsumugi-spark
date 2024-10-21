from abc import ABC, abstractmethod
from dataclasses import dataclass


from .proto import repository_pb2 as proto


class MetricRepository(ABC):
    """Abstract class for all metric repository in tsumugi."""

    @abstractmethod
    def _to_proto(self) -> proto.Repository: ...


@dataclass
class FileSystemRepository(MetricRepository):
    """Represents a FileSystem metric Repository in tsumugi."""

    path: str

    def _to_proto(self) -> proto.Repository:
        return proto.Repository(
            file_system=proto.FileSystemRepository(
                path=self.path,
            )
        )


@dataclass
class SparkTableRepository(MetricRepository):
    """Represents a spark table metric repository in tsumugi."""

    table_name: str

    def _to_proto(self) -> proto.Repository:
        return proto.Repository(
            spark_table=proto.SparkTableRepository(
                table_name=self.table_name,
            )
        )
