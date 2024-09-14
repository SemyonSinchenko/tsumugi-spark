.PHONY: all clean generate_code lint_python get_spark_server run_spark_server

all: help

generate_code:
	@rm -r tsumugi-python/tsumugi/proto/* || true
	@buf generate
	@$(MAKE) lint_python

lint_python:
	@cd tsumugi-python && \
		poetry run ruff format tsumugi && \
		poetry run ruff check --fix tsumugi && \
		cd ..

clean:
	@rm -r tmp/* || true

run_spark_server:
	@python dev/run-connect.py

help:
	@echo '------------------------------ Tsumugi Spark ------------------------------'
	@echo 'clean                 - delete temporay assets like spark distro'
	@echo 'generate_code         - generate language bindings from protobuf'
	@echo 'lint_python           - apply linter/fromatter to all the python code'
	@echo 'run_spark_server      - download Spark, build Tsumugi Plugin and start Spark Connect Server'
