.PHONY: all generate_code

all: help

generate_code:
	rm -r tsumugi_golang/tsumugi/proto/* || true
	rm -r tsumugi_python/proto/* || true
	buf generate

help:
	@echo '-------- Tsumugi Spark --------'
	@echo 'generate_code         - generate python code from protobuf'
