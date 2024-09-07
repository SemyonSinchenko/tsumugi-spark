from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional
from pyspark.sql import functions as F
from pyspark.sql.types import StructType

from tsumugi.utils import (
    CHECK_RESULTS_SUB_DF,
    CHECKS_SUB_DF,
    METRICS_SUB_DF,
    ROW_LEVEL_RESULTS_SUB_DF,
    CheckResult,
    MetricAndCheckResult,
    MetricResult,
)

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
    """Results of verification."""
    def __init__(self, df: DataFrame) -> None:
        """This constructor is internal and is not recommended to use."""
        self._has_row_results = ROW_LEVEL_RESULTS_SUB_DF in df.columns
        self._checks = self._get_checks(df)
        self._metrics = self._get_metrics(df)
        self._check_results = self._get_check_results(df)
        if self._has_row_results:
            self._row_level_results = self._get_row_level_results(df)

    @property
    def checks(self) -> tuple[CheckResult]:
        """Results of checks."""
        return self._checks

    @property
    def metrics(self) -> tuple[MetricResult]:
        """Computed metrics."""
        return self._metrics

    @property
    def check_results(self) -> tuple[MetricAndCheckResult]:
        """Results of checks with values of the corresponded metric and constraint."""
        return self._check_results

    @property
    def row_level_results(self) -> DataFrame | None:
        """Row-level results as it would be returned by Deequ."""
        if self._has_row_results:
            return self._row_level_results
        else:
            return None

    def _get_checks(self, df: DataFrame) -> tuple[CheckResult]:
        sub_df = df.select(F.explode(F.col(CHECKS_SUB_DF)).alias("sub_col"))
        collected = sub_df.collect()
        checks = []
        for row in collected:
            sub_row = row.sub_col
            checks.append(CheckResult._from_row(sub_row))

        return tuple(c for c in checks)

    def _get_metrics(self, df: DataFrame) -> tuple[MetricResult]:
        sub_df = df.select(F.explode(F.col(METRICS_SUB_DF)).alias("sub_col"))
        collected = sub_df.collect()
        metrics = []
        for row in collected:
            sub_row = row.sub_col
            metrics.append(CheckResult._from_row(sub_row))

        return tuple(m for m in metrics)

    def _get_check_results(self, df: DataFrame) -> tuple[MetricAndCheckResult]:
        sub_df = df.select(F.explode(F.col(CHECK_RESULTS_SUB_DF)).alias("sub_col"))
        collected = sub_df.collect()
        metrics_and_checks = []
        for row in collected:
            sub_row = row.sub_col
            metrics_and_checks.append(MetricAndCheckResult._from_row(sub_row))

        return tuple(mc for mc in metrics_and_checks)

    def _get_row_level_results(self, df: DataFrame) -> DataFrame:
        sub_df = df.select(F.explode(F.col(ROW_LEVEL_RESULTS_SUB_DF)).alias("sub_col"))
        sub_schema = sub_df.schema.fields[0]
        assert isinstance(sub_schema, StructType)
        columns_to_select = {
            cc.name: F.col(f"sub_col.{cc.name}") for cc in sub_schema.fields
        }

        return sub_df.withColumns(columns_to_select).drop("sub_col")
