from dataclasses import dataclass

from pyspark.sql import Row

STATUS_COL = "status"
METRICS_SUB_DF = "metrics"
CHECKS_SUB_DF = "checks"
CHECK_RESULTS_SUB_DF = "checkResults"
ROW_LEVEL_RESULTS_SUB_DF = "rowLevelResults"


@dataclass
class MetricAndCheckResult:
    level: str
    check_description: str
    constraint_message: str
    metric_name: str
    metric_instance: str
    metric_entity: str
    metric_value: float
    status: str
    constraint: str

    @staticmethod
    def _from_row(row: Row) -> "MetricAndCheckResult":
        """Create an instance from PySpark Row obejct."""

        return MetricAndCheckResult(
            level=row.level,
            check_description=row.checkDescription,
            constraint_message=row.constraintMessage,
            metric_name=row.metricName,
            metric_instance=row.metricInstance,
            metric_entity=row.metricEntity,
            metric_value=row.metricValue,
            status=row.status,
            constraint=row.constraint,
        )


@dataclass
class MetricResult:
    entity: str
    instance: str
    name: str
    value: float

    @staticmethod
    def _from_row(row: Row) -> "MetricResult":
        """Create an instance from PySpark Row object."""
        return MetricResult(
            entity=row.entity,
            instance=row.instance,
            name=row.name,
            value=row.value,
        )


@dataclass
class CheckResult:
    check: str
    check_level: str
    check_status: str
    constraint: str
    constraint_status: str
    constraint_message: str

    @staticmethod
    def _from_row(row: Row) -> "CheckResult":
        """Create an instance from PySpark Row object."""
        return CheckResult(
            check=row.check,
            check_level=row.check_level,
            check_status=row.check_status,
            constraint=row.constraint,
            constraint_status=row.constraint_status,
            constraint_message=row.constraint_message,
        )
