package com.ssinchenko

import com.amazon.deequ.VerificationSuite
import com.amazon.deequ.checks.CheckStatus
import org.apache.spark.sql.{DataFrame, Row, SparkSession}
import org.apache.spark.sql.types.{LongType, StringType, StructField, StructType}
import org.scalatest.BeforeAndAfterAll
import org.scalatest.funsuite.AnyFunSuiteLike

class DeequSuiteBuilderTest extends AnyFunSuiteLike with BeforeAndAfterAll {
  override def beforeAll(): Unit = {
    super.beforeAll()
    SparkSession.builder().master("local[1]").getOrCreate()
  }

  def createData(sparkSession: SparkSession): DataFrame = {
    sparkSession.createDataFrame(
      sparkSession.sparkContext.parallelize(
        List(
          Row(1L, "Thingy A", "awesome thing.", "high", 0L),
          Row(2L, "Thingy B", "available at http://thingb.com", null, 0L),
          Row(3L, null, null, "low", 5L),
          Row(4L, "Thingy D", "checkout https://thingd.ca", "low", 10L),
          Row(5L, "Thingy E", null, "high", 12L)
        )
      ),
      StructType(
        List(
          StructField("id", LongType),
          StructField("productName", StringType),
          StructField("description", StringType),
          StructField("priority", StringType),
          StructField("numViews", LongType)
        )
      )
    )
  }

  test("testProtoToAnalyzer") {
    val sparkSession = SparkSession.getActiveSession.get
    val data = createData(sparkSession)

    val size =
      DeequSuiteBuilder.parseAnalyzer(proto.Analyzer.newBuilder().setSize(proto.Size.newBuilder().build()).build())
    val sizeMetric = VerificationSuite().onData(data).addRequiredAnalyzer(size).run().metrics
    assert(sizeMetric.head._2.value.get == 5.0)

    val completeness =
      DeequSuiteBuilder.parseAnalyzer(
        proto.Analyzer.newBuilder().setCompleteness(proto.Completeness.newBuilder().setColumn("id").build()).build()
      )
    val completenessMetric = VerificationSuite().onData(data).addRequiredAnalyzer(completeness).run().metrics
    assert(completenessMetric.head._2.value.get == 1.0)
  }

  test("testProtoToVerificationSuite") {
    val spark = SparkSession.getActiveSession.get
    val data = createData(spark)

    val protoSuiteBuilder = proto.VerificationSuite.newBuilder()
    protoSuiteBuilder.addRequiredAnalyzers(proto.Analyzer.newBuilder().setSize(proto.Size.newBuilder().build()))
    protoSuiteBuilder.addChecks(
      proto.Check
        .newBuilder()
        .setCheckLevel(proto.CheckLevel.Error)
        .setDescription("integrity checks")
        .addConstraints(
          proto.Check.Constraint
            .newBuilder()
            .setAnalyzer(proto.Analyzer.newBuilder().setSize(proto.Size.newBuilder().build()))
            .setSign(proto.Check.ComparisonSign.EQ)
            .setLongExpectation(5L)
        )
        .addConstraints(
          proto.Check.Constraint
            .newBuilder()
            .setAnalyzer(proto.Analyzer.newBuilder().setCompleteness(proto.Completeness.newBuilder().setColumn("id")))
            .setSign(proto.Check.ComparisonSign.EQ)
            .setDoubleExpectation(1.0)
        )
    )

    val deequSuite = DeequSuiteBuilder.protoToVerificationSuite(data, protoSuiteBuilder.build())
    val checkResults = deequSuite.run().checkResults
    assert(checkResults.forall(_._2.status == CheckStatus.Success))
  }
}
