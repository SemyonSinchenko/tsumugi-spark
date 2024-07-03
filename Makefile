.PHONY: all generate_code

all: help

generate_code:
	rm -r tsumugi_python/proto/*
	buf generate

help:
	@echo '-------- Tsumugi Spark --------'
	@echo 'generate_code         - generate python code from protobuf'
