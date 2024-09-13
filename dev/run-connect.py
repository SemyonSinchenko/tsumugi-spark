#!/usr/bin/python
import os
import shutil
import subprocess
import sys
from pathlib import Path

SBT_BUILD_COMMAND = ["sbt", "clean", "package"]
SPARK_VERSION = "3.5.2"
DEEQU_VERSION = "2.0.7-spark-3.5"
PROTOBUF_VERSION = "3.25.1"
SCALA_VERSION = "2.12"
TSUMUGI_VERSION = "1.0-SNAPSHOT"


if __name__ == "__main__":
    prj_root = Path(__file__).parent.parent
    scala_root = prj_root.joinpath("tsumugi-server")

    print("Build Tsumugi...")
    os.chdir(scala_root)
    build_sbt = subprocess.run(
        SBT_BUILD_COMMAND,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )

    if build_sbt.returncode == 0:
        print("Done.")
    else:
        print(f"SBT build return an error: {build_sbt.returncode}")
        print("stdout: ", build_sbt.stdout)
        print("stderr: ", build_sbt.stderr)
        sys.exit(1)

    tmp_dir = prj_root.joinpath("tmp")
    tmp_dir.mkdir(exist_ok=True)
    os.chdir(tmp_dir)

    unpackaed_spark_binary = f"spark-{SPARK_VERSION}-bin-hadoop3"
    if not tmp_dir.joinpath(unpackaed_spark_binary).exists():
        print(f"Download spark {SPARK_VERSION}...")
        if tmp_dir.joinpath(f"spark-{SPARK_VERSION}-bin-hadoop3.tgz").exists():
            shutil.rmtree(
                tmp_dir.joinpath(f"spark-{SPARK_VERSION}-bin-hadoop3.tgz"),
                ignore_errors=True,
            )

        get_spark = subprocess.run(
            [
                "wget",
                f"https://archive.apache.org/dist/spark/spark-{SPARK_VERSION}/spark-{SPARK_VERSION}-bin-hadoop3.tgz",
            ],
            stdout=subprocess.PIPE,
            universal_newlines=True,
        )
        if get_spark.returncode == 0:
            print("Done.")
        else:
            print("Downlad failed.")
            print("stdout: ", get_spark.stdout)
            print("stdeerr: ", get_spark.stderr)
            sys.exit(1)

        print("Unpack Spark...")
        unpack_spark = subprocess.run(
            [
                "tar",
                "-xzf",
                f"spark-{SPARK_VERSION}-bin-hadoop3.tgz",
            ],
            stdout=subprocess.PIPE,
            universal_newlines=True,
        )
        if unpack_spark.returncode == 0:
            print("Done.")
        else:
            print("Unpacking failed.")
            print("stdout: ", unpack_spark.stdout)
            print("stdeerr: ", unpack_spark.stderr)
            sys.exit(1)

    spark_home = tmp_dir.joinpath(unpackaed_spark_binary)
    os.chdir(spark_home)

    if not spark_home.joinpath(f"deequ-{DEEQU_VERSION}.jar").exists():
        print(f"Download Deequ {DEEQU_VERSION}...")
        get_deequ = subprocess.run(
            [
                "wget",
                f"https://repo1.maven.org/maven2/com/amazon/deequ/deequ/{DEEQU_VERSION}/deequ-{DEEQU_VERSION}.jar",
            ]
        )
        if get_deequ.returncode == 0:
            print("Done.")
        else:
            print("Downlad failed.")
            print("stdout: ", get_deequ.stdout)
            print("stdeerr: ", get_deequ.stderr)
            sys.exit(1)

    if not spark_home.joinpath(f"protobuf-java-{PROTOBUF_VERSION}.jar").exists():
        print(f"Download Protobuf {PROTOBUF_VERSION}...")
        get_proto = subprocess.run(
            [
                "wget",
                f"https://repo1.maven.org/maven2/com/google/protobuf/protobuf-java/{PROTOBUF_VERSION}/protobuf-java-{PROTOBUF_VERSION}.jar",
            ]
        )
        if get_proto.returncode == 0:
            print("Done.")
        else:
            print("Downlad failed.")
            print("stdout: ", get_proto.stdout)
            print("stdeerr: ", get_proto.stderr)
            sys.exit(1)

    tsumugi_jar = (
        scala_root.joinpath("target")
        .joinpath(f"scala-{SCALA_VERSION}")
        .joinpath(f"tsumugi-server_{SCALA_VERSION}-{TSUMUGI_VERSION}.jar")
    )
    shutil.copyfile(tsumugi_jar, spark_home.joinpath(tsumugi_jar.name))

    run_connect_command = [
        "./sbin/start-connect-server.sh",
        "--wait",
        "--jars",
        f"{tsumugi_jar},protobuf-java-{PROTOBUF_VERSION}.jar,deequ-{DEEQU_VERSION}.jar",
        "--conf",
        "spark.connect.extensions.relation.classes=org.apache.spark.sql.tsumugi.DeequConnectPlugin",
        "--packages",
        f"org.apache.spark:spark-connect_{SCALA_VERSION}:{SPARK_VERSION}",
    ]
    print("Starting SparkConnect Server...")
    spark_connect = subprocess.run(
        run_connect_command,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )

    if spark_connect.returncode == 0:
        print("Done.")
