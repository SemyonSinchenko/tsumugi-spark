package com.ssinchenko.tsumugi

import com.amazon.deequ.checks.{Check, CheckResult}
import com.amazon.deequ.metrics.{DoubleMetric, HistogramMetric}
import com.amazon.deequ.{VerificationResult, VerificationRunBuilder}
import com.ssinchenko.tsumugi.exceptions.DataFrameIsRequiredException
import org.apache.spark.sql.{Column, DataFrame, SparkSession, functions => F}

private[ssinchenko] case class MetricsAndChecks(
    level: String,
    checkDescription: String,
    constraintMessage: String,
    metricName: String,
    metricInstance: String,
    metricEntity: String,
    metricValue: Double,
    status: String,
    constraint: String
)

object DeequUtils {
  private def checkResultToCaseClass(pair: (Check, CheckResult)): Seq[MetricsAndChecks] = {
    val checkLevel = pair._1.level
    val checkDescription = pair._1.description
    val constraintResult = pair._2.constraintResults

    constraintResult.map(constraint => {
      MetricsAndChecks(
        level = checkLevel.toString,
        checkDescription = checkDescription,
        constraintMessage = constraint.message.getOrElse(""),
        metricName = constraint.metric.map(_.name).getOrElse(""),
        metricInstance = constraint.metric.map(_.instance).getOrElse(""),
        metricEntity = constraint.metric.map(_.entity.toString).getOrElse(""),
        metricValue = constraint.metric
          .map {
            case DoubleMetric(_, _, _, value, _) => value.getOrElse(-999.0)
            case HistogramMetric(_, value)       => value.map(_.numberOfBins).getOrElse(-999.0)
            case _                               => -999.0 // TODO: fix it in the future
          }
          .getOrElse(-999.0),
        status = constraint.status.toString,
        constraint = constraint.constraint.toString
      )
    })
  }

  private def dataFrameToCol(df: DataFrame): Column = {
    df.withColumn("_c_struct", F.struct(df.columns.map(F.col): _*))
      .agg(F.collect_list("_c_struct").alias("_c_array"))("_c_array")
  }

  /**
   * Collect results of all the Check and combine with metrics
   * @param deequSuite
   *   results of verification
   * @return
   *   DataFrame with a schema < level: string, checkDescription: string, constraintMessage: string, metricName: string,
   *   metricInstance: string, metricEntity: string, metricValue: string, status: string, constraint: string >
   */
  private[ssinchenko] def checkResultAsDataFramePatched(
      deequSuite: VerificationResult,
      sparkSession: Option[SparkSession]
  ): DataFrame = {
    val spark = sparkSession.getOrElse(SparkSession.getActiveSession.get)
    spark.createDataFrame(deequSuite.checkResults.flatMap(checkResultToCaseClass).toSeq).toDF()
  }

  /**
   * Collect all the results to a single DataFrame object
   * @param deequSuite
   *   results of verification
   * @param returnRows
   *   should row-level results be returned?
   * @param sparkSession
   *   spark session or None
   * @param dataFrame
   *   data for computing row-level results
   * @return
   */
  private[ssinchenko] def allResultsAsDataFrame(
      deequSuite: VerificationResult,
      returnRows: Boolean = false,
      sparkSession: Option[SparkSession],
      dataFrame: Option[DataFrame] = None
  ): DataFrame = {
    val spark = sparkSession.getOrElse(SparkSession.getActiveSession.get)
    val metrics = VerificationResult.successMetricsAsDataFrame(sparkSession = spark, verificationResult = deequSuite)
    val checks = VerificationResult.checkResultsAsDataFrame(sparkSession = spark, verificationResult = deequSuite)
    val checkResults = checkResultAsDataFramePatched(deequSuite = deequSuite, sparkSession = sparkSession)

    val baseDf = spark.emptyDataFrame.withColumns(
      Map.apply(
        "metrics" -> dataFrameToCol(metrics),
        "checks" -> dataFrameToCol(checks),
        "checkResults" -> dataFrameToCol(checkResults)
      )
    )
    if (returnRows) {
      val data = dataFrame match {
        case Some(df) => df
        case None     => throw DataFrameIsRequiredException("DataFrame is require to generate row-level results!")
      }
      val rowResults = VerificationResult.rowLevelResultsAsDataFrame(
        sparkSession = spark,
        verificationResult = deequSuite,
        data = data
      )
      baseDf.withColumn("rowLevelResults", dataFrameToCol(rowResults))
    } else {
      baseDf
    }
  }

  /**
   * Run the suite and return all the results as a DataFrame object
   * @param suite
   *   Deequ suite (builder
   * @param sparkSession
   *   optional SparkSession
   * @param returnRows
   *   should row-level results be returned?
   * @param dataFrame
   *   data to compute row-level results
   * @return
   */
  def runAndCollectResults(
      suite: VerificationRunBuilder,
      sparkSession: Option[SparkSession] = None,
      returnRows: Boolean = false,
      dataFrame: Option[DataFrame] = None
  ): DataFrame = {
    val results = suite.run()
    allResultsAsDataFrame(results, returnRows, sparkSession, dataFrame)
  }
}
