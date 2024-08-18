import sbt._

name := "tsumugi-server"
organization := "com.ssinchenko"
version := "1.0-SNAPSHOT"
description := "SparkConnect Plugin for working with Amazon Deequ"

scalaVersion := "2.12.10"

val sparkVersion = "3.5.2"
val scalaTestVersion = "3.2.19"

val protobufVersion = "3.23.4"
val grpcVersion = "1.56.0"

resolvers ++= Seq(
  "GCS Maven Central mirror" at "https://maven-central.storage-download.googleapis.com/maven2/",
  "Maven Repository" at "https://repo.maven.apache.org/maven2"
)

enablePlugins(ProtobufPlugin)

libraryDependencies ++= Seq(
  "org.scala-lang" % "scala-library" % scalaVersion.value,

  // Test dependencies
  "org.scalatest" %% "scalatest" % scalaTestVersion % Test,

  // Spark dependencies
  "org.apache.spark" %% "spark-hive" % sparkVersion % Provided,
  "org.apache.spark" %% "spark-sql" % sparkVersion % Provided,
  "org.apache.spark" %% "spark-core" % sparkVersion % Provided,
  "org.apache.spark" %% "spark-catalyst" % sparkVersion % Provided,
  "org.apache.spark" %% "spark-connect" % sparkVersion % Provided,

  "org.apache.spark" %% "spark-hive" % sparkVersion % Test classifier "tests",
  "org.apache.spark" %% "spark-sql" % sparkVersion % Test classifier "tests",
  "org.apache.spark" %% "spark-core" % sparkVersion % Test classifier "tests",
  "org.apache.spark" %% "spark-catalyst" % sparkVersion % Test classifier "tests",
  "org.apache.spark" %% "spark-connect" % sparkVersion % Test classifier "tests",

  // Deequ
  "com.amazon.deequ" % "deequ" % "2.0.7-spark-3.5",

  // Protobuf and gRPC
  "com.google.protobuf" % "protobuf-java" % protobufVersion % Provided,
  "io.grpc" % "grpc-protobuf" % grpcVersion % Provided,
  "io.grpc" % "grpc-stub" % grpcVersion % Provided,
  "javax.annotation" % "javax.annotation-api" % "1.3.2" % Provided
)

// Scala compiler options
scalacOptions ++= Seq("-encoding", "UTF-8")

// Test settings
Test / testOptions += Tests.Argument(TestFrameworks.ScalaTest, "-oD")

// Source directories
Compile / scalaSource := baseDirectory.value / "src" / "main" / "scala"
Test / scalaSource := baseDirectory.value / "src" / "test" / "scala"

// Protobuf
ProtobufConfig / version := protobufVersion

// Shade
assembly / assemblyShadeRules := Seq(
  ShadeRule.rename("com.google.protobuf.**" -> "org.sparkproject.connect.protobuf.@1").inAll,
)

// Scalafmt
scalafmtConfig := baseDirectory.value / ".scalafmt.conf"
