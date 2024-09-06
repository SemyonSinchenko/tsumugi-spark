package com.ssinchenko

import com.amazon.deequ.VerificationSuite
import com.amazon.deequ.analyzers
import com.amazon.deequ.checks.CheckStatus
import com.ssinchenko.tsumugi.DeequSuiteBuilder
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

  test("testProtoToSign") {
    assert(DeequSuiteBuilder.parseSign(5L, proto.Check.ComparisonSign.GET).apply(5L))
    assert(DeequSuiteBuilder.parseSign(5.0, proto.Check.ComparisonSign.GT).apply(6.0))
    assert(DeequSuiteBuilder.parseSign(5.0, proto.Check.ComparisonSign.EQ).apply(5.0))
    assert(DeequSuiteBuilder.parseSign(5.0, proto.Check.ComparisonSign.LT).apply(4.0))
    assert(DeequSuiteBuilder.parseSign(5.0, proto.Check.ComparisonSign.LET).apply(5.0))
  }

  test("testProtoToAnalyzer") {
    val sparkSession = SparkSession.getActiveSession.get
    val data = createData(sparkSession)

    val approxCountDistinct = DeequSuiteBuilder.parseAnalyzer(
      proto.Analyzer
        .newBuilder()
        .setApproxCountDistinct(proto.ApproxCountDistinct.newBuilder().setColumn("id").build())
        .build()
    )
    val approxQuantile = DeequSuiteBuilder.parseAnalyzer(
      proto.Analyzer
        .newBuilder()
        .setApproxQuantile(
          proto.ApproxQuantile.newBuilder().setColumn("numViews").setQuantile(0.5).build()
        )
        .build()
    )
    val columnCount = DeequSuiteBuilder.parseAnalyzer(
      proto.Analyzer
        .newBuilder()
        .setColumnCount(
          proto.ColumnCount.newBuilder().build()
        )
        .build()
    )
    val completeness =
      DeequSuiteBuilder.parseAnalyzer(
        proto.Analyzer.newBuilder().setCompleteness(proto.Completeness.newBuilder().setColumn("id").build()).build()
      )
    val compliance = DeequSuiteBuilder.parseAnalyzer(
      proto.Analyzer
        .newBuilder()
        .setCompliance(
          proto.Compliance.newBuilder().setInstance("Thingy A occ").setPredicate("productName = 'Thingy A'").build()
        )
        .build()
    )
    val correlation = DeequSuiteBuilder.parseAnalyzer(
      proto.Analyzer
        .newBuilder()
        .setCorrelation(
          proto.Correlation
            .newBuilder()
            .setFirstColumn("id")
            .setSecondColumn("numViews")
            .build()
        )
        .build()
    )
    val countDistinct = DeequSuiteBuilder.parseAnalyzer(
      proto.Analyzer
        .newBuilder()
        .setCountDistinct(
          proto.CountDistinct.newBuilder().addColumns("id").build()
        )
        .build()
    )
    val distinctness = DeequSuiteBuilder.parseAnalyzer(
      proto.Analyzer
        .newBuilder()
        .setDistinctness(
          proto.Distinctness
            .newBuilder()
            .addColumns("id")
            .build()
        )
        .build()
    )
    val entropy = DeequSuiteBuilder.parseAnalyzer(
      proto.Analyzer
        .newBuilder()
        .setEntropy(
          proto.Entropy
            .newBuilder()
            .setColumn("productName")
            .build()
        )
        .build()
    )
    val maxLength = DeequSuiteBuilder.parseAnalyzer(
      proto.Analyzer
        .newBuilder()
        .setMaxLength(
          proto.MaxLength.newBuilder().setColumn("description").build()
        )
        .build()
    )
    val size =
      DeequSuiteBuilder.parseAnalyzer(proto.Analyzer.newBuilder().setSize(proto.Size.newBuilder().build()).build())
    val sum = DeequSuiteBuilder.parseAnalyzer(
      proto.Analyzer
        .newBuilder()
        .setSum(
          proto.Sum.newBuilder().setColumn("numViews").build()
        )
        .build()
    )
    val uniqueValueRatio = DeequSuiteBuilder.parseAnalyzer(
      proto.Analyzer
        .newBuilder()
        .setUniqueValueRatio(
          proto.UniqueValueRatio.newBuilder().addColumns("id").build()
        )
        .build()
    )

    val metrics = VerificationSuite()
      .onData(data)
      .addRequiredAnalyzers(
        Seq(
          approxCountDistinct,
          approxQuantile,
          columnCount,
          completeness,
          compliance,
          correlation,
          countDistinct,
          distinctness,
          entropy,
          size,
          sum,
          maxLength,
          uniqueValueRatio
        )
      )
      .run()
      .metrics

    assert(
      metrics.forall(p =>
        p._1 match {
          case _: analyzers.ApproxCountDistinct => p._2.value.get == 5.0
          case _: analyzers.ApproxQuantile      => p._2.value.get == 5.0
          case _: analyzers.ColumnCount         => p._2.value.get == 5.0
          case _: analyzers.Completeness        => p._2.value.get == 1.0
          case _: analyzers.Compliance          => p._2.value.get == 0.2
          case _: analyzers.Correlation         => p._2.value.get.asInstanceOf[Double] > 0.9
          case _: analyzers.CountDistinct       => p._2.value.get == 5.0
          case _: analyzers.Distinctness        => p._2.value.get == 1.0
          case _: analyzers.Entropy             => p._2.value.get.asInstanceOf[Double] > 0.85
          case _: analyzers.Size                => p._2.value.get == 5.0
          case _: analyzers.Sum                 => p._2.value.get == 27.0
          case _: analyzers.MaxLength           => p._2.value.get == 30.0
          case _: analyzers.UniqueValueRatio    => p._2.value.get == 1.0
        }
      )
    )
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
    protoSuiteBuilder.setFileSystemRepository(
      proto.VerificationSuite.FileSystemRepository
        .newBuilder()
        .setPath("test-file.json")
    )
    protoSuiteBuilder.addAnomalyDetections(
      proto.AnomalyDetection
        .newBuilder()
        .setAnalyzer(
          proto.Analyzer.newBuilder().setSize(proto.Size.newBuilder().build())
        )
        .setAnomalyDetectionStrategy(
          proto.AnomalyDetectionStrategy
            .newBuilder()
            .setRelativeRateOfChangeStrategy(
              proto.RelativeRateOfChangeStrategy
                .newBuilder()
                .setMaxRateIncrease(1.2)
                .setMaxRateDecrease(0.8)
                .setOrder(1)
            )
        )
        .setConfig(
          proto.AnomalyDetection.AnomalyCheckConfig
            .newBuilder()
            .setLevel(proto.CheckLevel.Warning)
            .setDescription("My best description")
            .setBeforeDate(1000)
            .setAfterDate(0)
        )
    )

    val deequSuite = DeequSuiteBuilder.protoToVerificationSuite(data, protoSuiteBuilder.build())
    val checkResults = deequSuite.run().checkResults
    assert(checkResults.forall(_._2.status == CheckStatus.Success))
  }
}
