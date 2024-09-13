from enum import Enum

from .proto import suite_pb2 as suite


class CheckLevel(str, Enum):
    Error = "Error"
    Warning = "Warning"

    def _to_proto(self) -> suite.CheckLevel:
        if self is CheckLevel.Error:
            return suite.CheckLevel.Error
        else:
            return suite.CheckLevel.Warning


