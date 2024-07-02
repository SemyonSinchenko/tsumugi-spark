package org.apache.spark.sql
// Dataset.ofRows is private[sql] because Dataset itself is private[sql]
// Is there any way to create a DataFrame from LogicalPlan except using spark package?

import com.amazon.deequ.VerificationResult
import com.google.protobuf.Any
import com.ssinchenko.DeequSuiteBuilder
import com.ssinchenko.proto.VerificationSuite
import org.apache.spark.sql.catalyst.plans.logical.LogicalPlan
import org.apache.spark.sql.connect.planner.SparkConnectPlanner
import org.apache.spark.sql.connect.plugin.RelationPlugin
import org.apache.spark.sql.types.{StringType, StructField, StructType}

class DeequConnectPlugin extends RelationPlugin {
  override def transform(relation: Any, planner: SparkConnectPlanner): Option[LogicalPlan] = {
    if (relation.is(classOf[VerificationSuite])) {
      val protoSuite = relation.unpack(classOf[VerificationSuite])
      val spark = planner.sessionHolder.session
      // TODO: Workaround, see suite.proto comments
      val protoPlan = org.apache.spark.connect.proto.Plan.parseFrom(protoSuite.getData.toByteArray)
      val data = Dataset.ofRows(spark, planner.transformRelation(protoPlan.getRoot))
      val result = DeequSuiteBuilder
        .protoToVerificationSuite(
          data,
          protoSuite
        )
        .run()

      val checkResults = VerificationResult.checkResultsAsJson(result)
      val metricsResult = VerificationResult.successMetricsAsJson(result)

      Option(
        spark
          .createDataFrame(
            java.util.List.of(
              Row(checkResults),
              Row(metricsResult)
            ),
            schema = StructType(Seq(StructField("results", StringType)))
          )
          .logicalPlan
      )
    } else {
      Option.empty
    }
  }

  // 4.0-preview version
  // override def transform(bytes: Array[Byte], sparkConnectPlanner: SparkConnectPlanner): Optional[LogicalPlan] = {
  //  try {
  //    val relationProto = Any.parseFrom(bytes)
  //    if (relationProto.is(classOf[VerificationSuite])) {
  //      val protoSuite = relationProto.unpack(classOf[VerificationSuite])
  //      val spark = sparkConnectPlanner.sessionHolder.session
  //      // TODO: Workaround, see suite.proto comments
  //      val protoPlan = org.apache.spark.connect.proto.Plan.parseFrom(protoSuite.getData.toByteArray)
  //      val data = Dataset.ofRows(spark, sparkConnectPlanner.transformRelation(protoPlan.getRoot))
  //      val result = DeequSuiteBuilder
  //        .protoToVerificationSuite(
  //          data,
  //          protoSuite
  //        )
  //        .run()

  //      val checkResults = VerificationResult.checkResultsAsJson(result)
  //      val metricsResult = VerificationResult.successMetricsAsJson(result)

  //      Optional.of(
  //        spark
  //          .createDataFrame(
  //            java.util.List.of(
  //              Row(checkResults),
  //              Row(metricsResult)
  //            ),
  //            schema = StructType(Seq(StructField("results", StringType)))
  //          )
  //          .logicalPlan
  //      )
  //    } else {
  //      Optional.empty
  //    }
  //  } catch {
  //    case e: InvalidProtocolBufferException => throw new RuntimeException(e)
  //  }
  // }
}
