import json
import sys
from pathlib import Path

import pandas as pd
from pyspark.sql import SparkSession

# TODO: that is a workaround because I'm a newbie in py-proto;
# The problem is in relative-imports.
proj_root = Path(__file__).parent.parent.parent
sys.path.append(proj_root.absolute().__str__())
sys.path.append(proj_root.joinpath("tsumugi").joinpath("proto").absolute().__str__())
from tsumugi.proto import analyzers_pb2 as analyzers  # noqa: E402
from tsumugi.proto import strategies_pb2 as strategies  # noqa: E402, F401
from tsumugi.proto import suite_pb2 as base  # noqa: E402

if __name__ == "__main__":
    # TODO: This example fails because org.apache.sparkproject base classes are not in CP
    # See the proposal in Spark Mailing List; will be fixed soon by moving SparkConnect to main Spark Distribution
    spark: SparkSession = (
        SparkSession.builder.master("local[1]")
        .config(
            "spark.jars",
            proj_root.parent.joinpath("tsumugi-server")
            .joinpath("target")
            .joinpath("tsumugi-server-1.0-SNAPSHOT.jar")
            .absolute()
            .__str__(),
        )
        .getOrCreate()
    )
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

    deequ_JVM_builder = spark._jvm.com.ssinchenko.DeequSuiteBuilder
    result = deequ_JVM_builder.protoToVerificationSuite(data._jdf, suite).run()

    checks = json.loads(
        spark._jvm.com.amazon.deequ.VerificationResult.checkResultsAsJson(result)
    )
    metrics = json.loads(
        spark._jvm.com.amazon.deequ.VerificationResult.successMetricsAsJson(result)
    )

    print(json.dumps(checks, indent=1))
    print(json.dumps(metrics, indent=1))
