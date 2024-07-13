import json
import sys
from pathlib import Path

import pandas as pd
from pyspark.sql.connect.client import SparkConnectClient
from pyspark.sql.connect.dataframe import DataFrame
from pyspark.sql.connect.plan import LogicalPlan
from pyspark.sql.connect.proto import Relation
from pyspark.sql.connect.session import SparkSession

# TODO: that is a workaround because I'm a newbie in py-proto;
# The problem is in relative-imports.
proj_root = Path(__file__).parent.parent.parent
print(proj_root)
sys.path.append(proj_root.absolute().__str__())
sys.path.append(proj_root.joinpath("tsumugi").joinpath("proto").absolute().__str__())
from tsumugi.proto import analyzers_pb2 as analyzers  # noqa: E402
from tsumugi.proto import strategies_pb2 as strategies  # noqa: E402, F401
from tsumugi.proto import suite_pb2 as base  # noqa: E402

if __name__ == "__main__":
    spark: SparkSession = SparkSession.builder.remote(
        "sc://localhost:15002"
    ).getOrCreate()
    # Data from https://github.com/awslabs/deequ/blob/master/src/main/scala/com/amazon/deequ/examples/BasicExample.scala
    test_rows = [
        {
            "id": 1,
            "productName": "Thingy A",
            "description": "awesome thing.",
            "priority": "high",
            "numViews": 0,
        },
        {
            "id": 2,
            "productName": "Thingy B",
            "description": "available",
            "priority": None,
            "numViews": 0,
        },
        {
            "id": 3,
            "productName": None,
            "description": None,
            "priority": "low",
            "numViews": 5,
        },
        {
            "id": 4,
            "productName": "Thingy D",
            "description": "checkout",
            "priority": "low",
            "numViews": 10,
        },
        {
            "id": 5,
            "productName": "Thingy E",
            "description": None,
            "priority": "high",
            "numViews": 12,
        },
    ]
    data = spark.createDataFrame(pd.DataFrame.from_records(test_rows))
    data.printSchema()
    data.show()
    suite = base.VerificationSuite()
    suite.data = data._plan.to_proto(spark.client).SerializeToString()
    check = suite.checks.add()
    check.checkLevel = base.CheckLevel.Warning
    check.description = "integrity checks"

    # Add required analyzer
    req_analyzer = suite.required_analyzers.add()
    req_analyzer.size.CopyFrom(analyzers.Size())

    # First constraint
    ct = check.constraints.add()
    ct.analyzer.size.CopyFrom(analyzers.Size())
    ct.long_expectation = 5
    ct.sign = base.Check.ComparisonSign.EQ
    # Second constraint
    ct = check.constraints.add()
    ct.analyzer.completeness.CopyFrom(analyzers.Completeness(column="id"))
    ct.double_expectation = 1.0
    ct.sign = base.Check.ComparisonSign.EQ

    assert suite.IsInitialized()

    class DeequVerification(LogicalPlan):
        def __init__(self, suite: base.VerificationSuite) -> None:
            super().__init__(None)
            self._suite = suite

        def plan(self, session: SparkConnectClient) -> Relation:
            plan = self._create_proto_relation()
            plan.extension.Pack(self._suite)
            return plan

    tdf = DataFrame.withPlan(DeequVerification(suite=suite), spark)
    results = tdf.toPandas()

    checks = json.loads(results.loc[0, "results"])
    metrics = json.loads(results.loc[1, "results"])

    print(json.dumps(checks, indent=1))
    print(json.dumps(metrics, indent=1))
