.PHONY: all clean generate_code lint_python get_spark_server run_spark_server

all: help

SPARK_VERSION ?= "3.5.1"
PROTOBUF_VERSION ?= "3.25.1"
DEEQU_VERSION ?= "2.0.7-spark-3.5"

generate_code:
	@rm -r tsumugi_golang/tsumugi/proto/* || true
	@rm -r tsumugi_python/tsumugi/proto/* || true
	@buf generate
	@$(MAKE) lint_python

lint_python:
	@cd tsumugi_python && \
		poetry run ruff format tsumugi && \
		poetry run ruff check --fix tsumugi && \
		cd ..

clean:
	@rm -r dev/spark-* || true

get_spark_server:
	@$(MAKE) clean
	@cd dev && \
		wget "https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz" && \
		tar -xvf spark-${SPARK_VERSION}-bin-hadoop3.tgz && \
		cp run-connect.sh spark-${SPARK_VERSION}-bin-hadoop3/ && \
		cd spark-${SPARK_VERSION}-bin-hadoop3/ && \
		cp ../run-connect.sh ./ && \
		wget "https://repo1.maven.org/maven2/com/amazon/deequ/deequ/${DEEQU_VERSION}/deequ-${DEEQU_VERSION}.jar" && \
		wget "https://repo1.maven.org/maven2/com/google/protobuf/protobuf-java/${PROTOBUF_VERSION}/protobuf-java-${PROTOBUF_VERSION}.jar"

run_spark_server:
	@cd tsumugi-server && \
		mvn clean package -DskipTests && \
		cd ../dev/spark-${SPARK_VERSION}-bin-hadoop3/ && \
		sh ./run-connect.sh

help:
	@echo '------------------------------ Tsumugi Spark ------------------------------'
	@echo 'clean                 - delete temporay assets like spark distro'
	@echo 'generate_code         - generate language bindings from protobuf'
	@echo 'lint_python           - apply linter/fromatter to all the python code'
	@echo 'get_spark_server      - download Spark Server and configure it'
	@echo 'run_spark_server      - build Tsumugi Plugin and start Spark Connect Server'
