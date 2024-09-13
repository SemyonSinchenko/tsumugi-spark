from dataclasses import dataclass
from typing_extensions import Self

from pyspark.sql import DataFrame, SparkSession, SQLContext
from pyspark.sql import functions as F
from pyspark.sql.connect.client import SparkConnectClient
from pyspark.sql.connect.dataframe import DataFrame as ConnectDataFrame
from pyspark.sql.connect.plan import LogicalPlan
from pyspark.sql.connect.proto import Relation
from pyspark.sql.connect.session import SparkSession as ConnectSession
from pyspark.sql.types import StructType

from tsumugi.analyzers import AbstractAnalyzer
from tsumugi.utils import (
    CHECK_RESULTS_SUB_DF,
    CHECKS_SUB_DF,
    METRICS_SUB_DF,
    ROW_LEVEL_RESULTS_SUB_DF,
    CheckResult,
    MetricAndCheckResult,
    MetricResult,
)

from .proto import suite_pb2 as suite


@dataclass
class VerificationResult:
    """Results of verification."""

    def __init__(self, df: DataFrame | ConnectDataFrame) -> None:
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
            metrics.append(MetricResult._from_row(sub_row))

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


class VerificationRunBuilder:
    def __init__(self, df: DataFrame | ConnectDataFrame) -> None:
        self._data = df
        self._checks: list[suite.Check] = list()
        self._required_analyzers: list[AbstractAnalyzer] = list()
        self._path: str | None = None
        self._table_name: str | None = None
        self._dataset_date: int | None = None
        self._dataset_tags: dict[str, str] = dict()
        self._anomaly_detectons: list[suite.AnomalyDetection] = list()

    def add_required_analyzer(self, analyzer: AbstractAnalyzer) -> Self:
        self._required_analyzers.append(analyzer)
        return self

    def add_required_analyzers(self, analyzers: list[AbstractAnalyzer]) -> Self:
        self._required_analyzers = analyzers
        return self

    def add_check(self, check: suite.Check) -> Self:
        self._checks.append(check)
        return self

    def add_checks(self, checks: list[suite.Check]) -> Self:
        self._checks = checks
        return self

    def with_fs_repository_and_key(
        self,
        filepath: str,
        dataset_date: int,
        dataset_tags: dict[str, str] | None = None,
    ) -> Self:
        self._table_name = None
        self._path = filepath
        self._dataset_date = dataset_date
        self._dataset_tags = dataset_tags if dataset_tags is not None else dict()
        return self

    def with_table_repository_and_key(
        self,
        table_name: str,
        dataset_date: int,
        dateset_tags: dict[str, str] | None = None,
    ) -> Self:
        self._path = None
        self._table_name = table_name
        self._dataset_date = dataset_date
        self._dataset_tags = dateset_tags if dateset_tags is not None else dict()
        return self

    def add_anomaly_detection(self, ad: suite.AnomalyDetection) -> Self:
        self._anomaly_detectons.append(ad)
        return self

    def add_anomaly_detections(self, ads: list[suite.AnomalyDetection]) -> Self:
        self._anomaly_detectons = ads
        return self

    def _validate(self) -> None:
        if len(self._anomaly_detectons) > 0:
            if not (self._path or self._table_name):
                raise ValueError("Anomaly detection requires repository and key")

    def _build(self) -> suite.VerificationSuite:
        self._validate()

        pb_suite = suite.VerificationSuite(
            checks=self._checks,
            required_analyzers=[al._to_proto() for al in self._required_analyzers],
        )

        if self._path:
            pb_suite.file_system_repository = (
                suite.VerificationSuite.FileSystemRepository(path=self._path)
            )

        if self._table_name:
            pb_suite.spark_table_repository = (
                suite.VerificationSuite.SparkTableRepository(
                    table_name=self._table_name
                )
            )

        if self._path or self._table_name:
            pb_suite.result_key = suite.VerificationSuite.ResultKey(
                dataset_date=self._dataset_date, tags=self._dataset_tags
            )
            for ad in self._anomaly_detectons:
                _ad = pb_suite.anomaly_detections.append(ad)

        return pb_suite

    def run_with_spark_session(
        self, spark: SparkSession | ConnectSession
    ) -> VerificationResult:
        pb_suite = self._build()
        if isinstance(spark, SparkSession):
            assert isinstance(self._data, DataFrame)
            jvm = spark._jvm
            jdf = self._data._jdf
            result_jdf = jvm.com.ssinchenko.tsumugi.DeequSuiteBuilder(jdf, pb_suite)
            return VerificationResult(
                DataFrame(result_jdf, SQLContext(spark.sparkContext))
            )
        else:
            assert isinstance(self._data, ConnectDataFrame)
            data_plan = self._data._plan
            assert data_plan is not None
            pb_suite.data = data_plan.to_proto(spark.client).SerializeToString()

            class DeequSuite(LogicalPlan):
                def __init__(self, pb_suite: suite.VerificationSuite) -> None:
                    super().__init__(None)
                    self._pb_suite = pb_suite

                def plan(self, session: SparkConnectClient) -> Relation:
                    plan = self._create_proto_relation()
                    plan.extension.Pack(self._pb_suite)
                    return plan

            return VerificationResult(
                ConnectDataFrame.withPlan(DeequSuite(pb_suite=pb_suite), spark)
            )


class VerificationSuite:
    @staticmethod
    def on_data(data: DataFrame | ConnectDataFrame) -> VerificationRunBuilder:
        return VerificationRunBuilder(data)
