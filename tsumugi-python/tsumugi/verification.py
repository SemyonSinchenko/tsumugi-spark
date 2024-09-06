import json
from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .checks import CheckLevel

if TYPE_CHECKING:
    from pyspark.sql import DataFrame

from .proto import suite_pb2 as suite


@dataclass
class AnomalyChekConfig:
    check_level: CheckLevel
    description: str
    tag_values: dict[str, str]
    after_date: Optional[int] = None
    before_date: Optional[int] = None

    def _to_proto(self) -> suite.AnomalyDetection.AnomalyCheckConfig:
        return suite.AnomalyDetection.AnomalyCheckConfig(
            self.check_level,
            self.description,
            self.tag_values,
            self.after_date,
            self.before_date,
        )


@dataclass
class VerificationResult:
    def __init__(self, df: DataFrame) -> None:
        collected_rows = df.collect()
        if len(collected_rows) < 2:
            raise ValueError(
                f"Expected a DataFrame with two rows but got {len(collected_rows)} rows"
            )
        self._checks_json = json.loads(collected_rows[0]["results"])
        self._metrics_json = json.loads(collected_rows[1]["results"])
