# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: analyzers.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 27, 1, "", "analyzers.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0f\x61nalyzers.proto\x12\x1c\x63om.ssinchenko.tsumugi.proto"\xaf\x11\n\x08\x41nalyzer\x12g\n\x15\x61pprox_count_distinct\x18\x01 \x01(\x0b\x32\x31.com.ssinchenko.tsumugi.proto.ApproxCountDistinctH\x00R\x13\x61pproxCountDistinct\x12W\n\x0f\x61pprox_quantile\x18\x02 \x01(\x0b\x32,.com.ssinchenko.tsumugi.proto.ApproxQuantileH\x00R\x0e\x61pproxQuantile\x12Z\n\x10\x61pprox_quantiles\x18\x03 \x01(\x0b\x32-.com.ssinchenko.tsumugi.proto.ApproxQuantilesH\x00R\x0f\x61pproxQuantiles\x12N\n\x0c\x63olumn_count\x18\x04 \x01(\x0b\x32).com.ssinchenko.tsumugi.proto.ColumnCountH\x00R\x0b\x63olumnCount\x12P\n\x0c\x63ompleteness\x18\x05 \x01(\x0b\x32*.com.ssinchenko.tsumugi.proto.CompletenessH\x00R\x0c\x63ompleteness\x12J\n\ncompliance\x18\x06 \x01(\x0b\x32(.com.ssinchenko.tsumugi.proto.ComplianceH\x00R\ncompliance\x12M\n\x0b\x63orrelation\x18\x07 \x01(\x0b\x32).com.ssinchenko.tsumugi.proto.CorrelationH\x00R\x0b\x63orrelation\x12T\n\x0e\x63ount_distinct\x18\x08 \x01(\x0b\x32+.com.ssinchenko.tsumugi.proto.CountDistinctH\x00R\rcountDistinct\x12H\n\ncustom_sql\x18\t \x01(\x0b\x32\'.com.ssinchenko.tsumugi.proto.CustomSqlH\x00R\tcustomSql\x12\x45\n\tdata_type\x18\n \x01(\x0b\x32&.com.ssinchenko.tsumugi.proto.DataTypeH\x00R\x08\x64\x61taType\x12P\n\x0c\x64istinctness\x18\x0b \x01(\x0b\x32*.com.ssinchenko.tsumugi.proto.DistinctnessH\x00R\x0c\x64istinctness\x12\x41\n\x07\x65ntropy\x18\x0c \x01(\x0b\x32%.com.ssinchenko.tsumugi.proto.EntropyH\x00R\x07\x65ntropy\x12T\n\x0e\x65xact_quantile\x18\r \x01(\x0b\x32+.com.ssinchenko.tsumugi.proto.ExactQuantileH\x00R\rexactQuantile\x12G\n\thistogram\x18\x0e \x01(\x0b\x32\'.com.ssinchenko.tsumugi.proto.HistogramH\x00R\thistogram\x12H\n\nkll_sketch\x18\x0f \x01(\x0b\x32\'.com.ssinchenko.tsumugi.proto.KLLSketchH\x00R\tkllSketch\x12H\n\nmax_length\x18\x10 \x01(\x0b\x32\'.com.ssinchenko.tsumugi.proto.MaxLengthH\x00R\tmaxLength\x12\x41\n\x07maximum\x18\x11 \x01(\x0b\x32%.com.ssinchenko.tsumugi.proto.MaximumH\x00R\x07maximum\x12\x38\n\x04mean\x18\x12 \x01(\x0b\x32".com.ssinchenko.tsumugi.proto.MeanH\x00R\x04mean\x12H\n\nmin_length\x18\x13 \x01(\x0b\x32\'.com.ssinchenko.tsumugi.proto.MinLengthH\x00R\tminLength\x12\x41\n\x07minimum\x18\x14 \x01(\x0b\x32%.com.ssinchenko.tsumugi.proto.MinimumH\x00R\x07minimum\x12`\n\x12mutual_information\x18\x15 \x01(\x0b\x32/.com.ssinchenko.tsumugi.proto.MutualInformationH\x00R\x11mutualInformation\x12Q\n\rpattern_match\x18\x16 \x01(\x0b\x32*.com.ssinchenko.tsumugi.proto.PatternMatchH\x00R\x0cpatternMatch\x12O\n\rratio_of_sums\x18\x17 \x01(\x0b\x32).com.ssinchenko.tsumugi.proto.RatioOfSumsH\x00R\x0bratioOfSums\x12\x38\n\x04size\x18\x18 \x01(\x0b\x32".com.ssinchenko.tsumugi.proto.SizeH\x00R\x04size\x12`\n\x12standard_deviation\x18\x19 \x01(\x0b\x32/.com.ssinchenko.tsumugi.proto.StandardDeviationH\x00R\x11standardDeviation\x12\x35\n\x03sum\x18\x1a \x01(\x0b\x32!.com.ssinchenko.tsumugi.proto.SumH\x00R\x03sum\x12^\n\x12unique_value_ratio\x18\x1b \x01(\x0b\x32..com.ssinchenko.tsumugi.proto.UniqueValueRatioH\x00R\x10uniqueValueRatio\x12J\n\nuniqueness\x18\x1c \x01(\x0b\x32(.com.ssinchenko.tsumugi.proto.UniquenessH\x00R\nuniquenessB\n\n\x08\x61nalyzer"\xcb\x02\n\x0f\x41nalyzerOptions\x12\x62\n\x0enull_behaviour\x18\x01 \x01(\x0e\x32;.com.ssinchenko.tsumugi.proto.AnalyzerOptions.NullBehaviourR\rnullBehaviour\x12r\n\x14\x66iltered_row_outcome\x18\x02 \x01(\x0e\x32@.com.ssinchenko.tsumugi.proto.AnalyzerOptions.FilteredRowOutcomeR\x12\x66ilteredRowOutcome"6\n\rNullBehaviour\x12\n\n\x06Ignore\x10\x00\x12\x0f\n\x0b\x45mptyString\x10\x01\x12\x08\n\x04\x46\x61il\x10\x02"(\n\x12\x46ilteredRowOutcome\x12\x08\n\x04NULL\x10\x00\x12\x08\n\x04TRUE\x10\x01"R\n\x13\x41pproxCountDistinct\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12\x19\n\x05where\x18\x02 \x01(\tH\x00R\x05where\x88\x01\x01\x42\x08\n\x06_where"\xa8\x01\n\x0e\x41pproxQuantile\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12\x1a\n\x08quantile\x18\x02 \x01(\x01R\x08quantile\x12*\n\x0erelative_error\x18\x03 \x01(\x01H\x00R\rrelativeError\x88\x01\x01\x12\x19\n\x05where\x18\x04 \x01(\tH\x01R\x05where\x88\x01\x01\x42\x11\n\x0f_relative_errorB\x08\n\x06_where"\x86\x01\n\x0f\x41pproxQuantiles\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12\x1c\n\tquantiles\x18\x02 \x03(\x01R\tquantiles\x12*\n\x0erelative_error\x18\x03 \x01(\x01H\x00R\rrelativeError\x88\x01\x01\x42\x11\n\x0f_relative_error"\r\n\x0b\x43olumnCount"\x94\x01\n\x0c\x43ompleteness\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12\x19\n\x05where\x18\x02 \x01(\tH\x00R\x05where\x88\x01\x01\x12G\n\x07options\x18\x03 \x01(\x0b\x32-.com.ssinchenko.tsumugi.proto.AnalyzerOptionsR\x07optionsB\x08\n\x06_where"\xdf\x01\n\nCompliance\x12\x1a\n\x08instance\x18\x01 \x01(\tR\x08instance\x12\x1c\n\tpredicate\x18\x02 \x01(\tR\tpredicate\x12\x19\n\x05where\x18\x03 \x01(\tH\x00R\x05where\x88\x01\x01\x12\x18\n\x07\x63olumns\x18\x04 \x03(\tR\x07\x63olumns\x12L\n\x07options\x18\x05 \x01(\x0b\x32-.com.ssinchenko.tsumugi.proto.AnalyzerOptionsH\x01R\x07options\x88\x01\x01\x42\x08\n\x06_whereB\n\n\x08_options"z\n\x0b\x43orrelation\x12!\n\x0c\x66irst_column\x18\x01 \x01(\tR\x0b\x66irstColumn\x12#\n\rsecond_column\x18\x02 \x01(\tR\x0csecondColumn\x12\x19\n\x05where\x18\x03 \x01(\tH\x00R\x05where\x88\x01\x01\x42\x08\n\x06_where")\n\rCountDistinct\x12\x18\n\x07\x63olumns\x18\x01 \x03(\tR\x07\x63olumns"-\n\tCustomSql\x12 \n\x0b\x65xpressions\x18\x01 \x01(\tR\x0b\x65xpressions"G\n\x08\x44\x61taType\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12\x19\n\x05where\x18\x02 \x01(\tH\x00R\x05where\x88\x01\x01\x42\x08\n\x06_where"M\n\x0c\x44istinctness\x12\x18\n\x07\x63olumns\x18\x01 \x03(\tR\x07\x63olumns\x12\x19\n\x05where\x18\x02 \x01(\tH\x00R\x05where\x88\x01\x01\x42\x08\n\x06_where"F\n\x07\x45ntropy\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12\x19\n\x05where\x18\x02 \x01(\tH\x00R\x05where\x88\x01\x01\x42\x08\n\x06_where"h\n\rExactQuantile\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12\x1a\n\x08quantile\x18\x02 \x01(\x01R\x08quantile\x12\x19\n\x05where\x18\x03 \x01(\tH\x00R\x05where\x88\x01\x01\x42\x08\n\x06_where"\xa3\x05\n\tHistogram\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12+\n\x0fmax_detail_bins\x18\x02 \x01(\x05H\x00R\rmaxDetailBins\x88\x01\x01\x12\x19\n\x05where\x18\x03 \x01(\tH\x01R\x05where\x88\x01\x01\x12\x44\n\x1c\x63ompute_frequencies_as_ratio\x18\x04 \x01(\x08H\x02R\x19\x63omputeFrequenciesAsRatio\x88\x01\x01\x12m\n\x12\x61ggregate_function\x18\x05 \x01(\x0b\x32\x39.com.ssinchenko.tsumugi.proto.Histogram.AggregateFunctionH\x03R\x11\x61ggregateFunction\x88\x01\x01\x1a\xaa\x02\n\x11\x41ggregateFunction\x12j\n\x0f\x63ount_aggregate\x18\x01 \x01(\x0b\x32?.com.ssinchenko.tsumugi.proto.Histogram.AggregateFunction.CountH\x00R\x0e\x63ountAggregate\x12\x64\n\rsum_aggregate\x18\x02 \x01(\x0b\x32=.com.ssinchenko.tsumugi.proto.Histogram.AggregateFunction.SumH\x00R\x0csumAggregate\x1a\x07\n\x05\x43ount\x1a$\n\x03Sum\x12\x1d\n\nagg_column\x18\x01 \x01(\tR\taggColumnB\x14\n\x12\x61ggregate_functionB\x12\n\x10_max_detail_binsB\x08\n\x06_whereB\x1f\n\x1d_compute_frequencies_as_ratioB\x15\n\x13_aggregate_function"\xa3\x02\n\tKLLSketch\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12\x61\n\x0ekll_parameters\x18\x02 \x01(\x0b\x32\x35.com.ssinchenko.tsumugi.proto.KLLSketch.KLLParametersH\x00R\rkllParameters\x88\x01\x01\x1a\x87\x01\n\rKLLParameters\x12\x1f\n\x0bsketch_size\x18\x01 \x01(\x05R\nsketchSize\x12)\n\x10shrinking_factor\x18\x02 \x01(\x01R\x0fshrinkingFactor\x12*\n\x11number_of_buckets\x18\x03 \x01(\x05R\x0fnumberOfBucketsB\x11\n\x0f_kll_parameters"\xa2\x01\n\tMaxLength\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12\x19\n\x05where\x18\x02 \x01(\tH\x00R\x05where\x88\x01\x01\x12L\n\x07options\x18\x03 \x01(\x0b\x32-.com.ssinchenko.tsumugi.proto.AnalyzerOptionsH\x01R\x07options\x88\x01\x01\x42\x08\n\x06_whereB\n\n\x08_options"\xa0\x01\n\x07Maximum\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12\x19\n\x05where\x18\x02 \x01(\tH\x00R\x05where\x88\x01\x01\x12L\n\x07options\x18\x03 \x01(\x0b\x32-.com.ssinchenko.tsumugi.proto.AnalyzerOptionsH\x01R\x07options\x88\x01\x01\x42\x08\n\x06_whereB\n\n\x08_options"C\n\x04Mean\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12\x19\n\x05where\x18\x02 \x01(\tH\x00R\x05where\x88\x01\x01\x42\x08\n\x06_where"\xa2\x01\n\tMinLength\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12\x19\n\x05where\x18\x02 \x01(\tH\x00R\x05where\x88\x01\x01\x12L\n\x07options\x18\x03 \x01(\x0b\x32-.com.ssinchenko.tsumugi.proto.AnalyzerOptionsH\x01R\x07options\x88\x01\x01\x42\x08\n\x06_whereB\n\n\x08_options"\xa0\x01\n\x07Minimum\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12\x19\n\x05where\x18\x02 \x01(\tH\x00R\x05where\x88\x01\x01\x12L\n\x07options\x18\x03 \x01(\x0b\x32-.com.ssinchenko.tsumugi.proto.AnalyzerOptionsH\x01R\x07options\x88\x01\x01\x42\x08\n\x06_whereB\n\n\x08_options"R\n\x11MutualInformation\x12\x18\n\x07\x63olumns\x18\x01 \x03(\tR\x07\x63olumns\x12\x19\n\x05where\x18\x02 \x01(\tH\x00R\x05where\x88\x01\x01\x42\x08\n\x06_where"\xbf\x01\n\x0cPatternMatch\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12\x18\n\x07pattern\x18\x02 \x01(\tR\x07pattern\x12\x19\n\x05where\x18\x03 \x01(\tH\x00R\x05where\x88\x01\x01\x12L\n\x07options\x18\x04 \x01(\x0b\x32-.com.ssinchenko.tsumugi.proto.AnalyzerOptionsH\x01R\x07options\x88\x01\x01\x42\x08\n\x06_whereB\n\n\x08_options"r\n\x0bRatioOfSums\x12\x1c\n\tnumerator\x18\x01 \x01(\tR\tnumerator\x12 \n\x0b\x64\x65nominator\x18\x02 \x01(\tR\x0b\x64\x65nominator\x12\x19\n\x05where\x18\x03 \x01(\tH\x00R\x05where\x88\x01\x01\x42\x08\n\x06_where"+\n\x04Size\x12\x19\n\x05where\x18\x01 \x01(\tH\x00R\x05where\x88\x01\x01\x42\x08\n\x06_where"P\n\x11StandardDeviation\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12\x19\n\x05where\x18\x02 \x01(\tH\x00R\x05where\x88\x01\x01\x42\x08\n\x06_where"B\n\x03Sum\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12\x19\n\x05where\x18\x02 \x01(\tH\x00R\x05where\x88\x01\x01\x42\x08\n\x06_where"\xab\x01\n\x10UniqueValueRatio\x12\x18\n\x07\x63olumns\x18\x01 \x03(\tR\x07\x63olumns\x12\x19\n\x05where\x18\x02 \x01(\tH\x00R\x05where\x88\x01\x01\x12L\n\x07options\x18\x03 \x01(\x0b\x32-.com.ssinchenko.tsumugi.proto.AnalyzerOptionsH\x01R\x07options\x88\x01\x01\x42\x08\n\x06_whereB\n\n\x08_options"\xa5\x01\n\nUniqueness\x12\x18\n\x07\x63olumns\x18\x01 \x03(\tR\x07\x63olumns\x12\x19\n\x05where\x18\x02 \x01(\tH\x00R\x05where\x88\x01\x01\x12L\n\x07options\x18\x03 \x01(\x0b\x32-.com.ssinchenko.tsumugi.proto.AnalyzerOptionsH\x01R\x07options\x88\x01\x01\x42\x08\n\x06_whereB\n\n\x08_optionsB\xd8\x01\n com.com.ssinchenko.tsumugi.protoB\x0e\x41nalyzersProtoP\x01Z\rtsumugi/proto\xa0\x01\x01\xa2\x02\x04\x43STP\xaa\x02\x1c\x43om.Ssinchenko.Tsumugi.Proto\xca\x02\x1c\x43om\\Ssinchenko\\Tsumugi\\Proto\xe2\x02(Com\\Ssinchenko\\Tsumugi\\Proto\\GPBMetadata\xea\x02\x1f\x43om::Ssinchenko::Tsumugi::Protob\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "analyzers_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n com.com.ssinchenko.tsumugi.protoB\016AnalyzersProtoP\001Z\rtsumugi/proto\240\001\001\242\002\004CSTP\252\002\034Com.Ssinchenko.Tsumugi.Proto\312\002\034Com\\Ssinchenko\\Tsumugi\\Proto\342\002(Com\\Ssinchenko\\Tsumugi\\Proto\\GPBMetadata\352\002\037Com::Ssinchenko::Tsumugi::Proto"
    _globals["_ANALYZER"]._serialized_start = 50
    _globals["_ANALYZER"]._serialized_end = 2273
    _globals["_ANALYZEROPTIONS"]._serialized_start = 2276
    _globals["_ANALYZEROPTIONS"]._serialized_end = 2607
    _globals["_ANALYZEROPTIONS_NULLBEHAVIOUR"]._serialized_start = 2511
    _globals["_ANALYZEROPTIONS_NULLBEHAVIOUR"]._serialized_end = 2565
    _globals["_ANALYZEROPTIONS_FILTEREDROWOUTCOME"]._serialized_start = 2567
    _globals["_ANALYZEROPTIONS_FILTEREDROWOUTCOME"]._serialized_end = 2607
    _globals["_APPROXCOUNTDISTINCT"]._serialized_start = 2609
    _globals["_APPROXCOUNTDISTINCT"]._serialized_end = 2691
    _globals["_APPROXQUANTILE"]._serialized_start = 2694
    _globals["_APPROXQUANTILE"]._serialized_end = 2862
    _globals["_APPROXQUANTILES"]._serialized_start = 2865
    _globals["_APPROXQUANTILES"]._serialized_end = 2999
    _globals["_COLUMNCOUNT"]._serialized_start = 3001
    _globals["_COLUMNCOUNT"]._serialized_end = 3014
    _globals["_COMPLETENESS"]._serialized_start = 3017
    _globals["_COMPLETENESS"]._serialized_end = 3165
    _globals["_COMPLIANCE"]._serialized_start = 3168
    _globals["_COMPLIANCE"]._serialized_end = 3391
    _globals["_CORRELATION"]._serialized_start = 3393
    _globals["_CORRELATION"]._serialized_end = 3515
    _globals["_COUNTDISTINCT"]._serialized_start = 3517
    _globals["_COUNTDISTINCT"]._serialized_end = 3558
    _globals["_CUSTOMSQL"]._serialized_start = 3560
    _globals["_CUSTOMSQL"]._serialized_end = 3605
    _globals["_DATATYPE"]._serialized_start = 3607
    _globals["_DATATYPE"]._serialized_end = 3678
    _globals["_DISTINCTNESS"]._serialized_start = 3680
    _globals["_DISTINCTNESS"]._serialized_end = 3757
    _globals["_ENTROPY"]._serialized_start = 3759
    _globals["_ENTROPY"]._serialized_end = 3829
    _globals["_EXACTQUANTILE"]._serialized_start = 3831
    _globals["_EXACTQUANTILE"]._serialized_end = 3935
    _globals["_HISTOGRAM"]._serialized_start = 3938
    _globals["_HISTOGRAM"]._serialized_end = 4613
    _globals["_HISTOGRAM_AGGREGATEFUNCTION"]._serialized_start = 4229
    _globals["_HISTOGRAM_AGGREGATEFUNCTION"]._serialized_end = 4527
    _globals["_HISTOGRAM_AGGREGATEFUNCTION_COUNT"]._serialized_start = 4460
    _globals["_HISTOGRAM_AGGREGATEFUNCTION_COUNT"]._serialized_end = 4467
    _globals["_HISTOGRAM_AGGREGATEFUNCTION_SUM"]._serialized_start = 4469
    _globals["_HISTOGRAM_AGGREGATEFUNCTION_SUM"]._serialized_end = 4505
    _globals["_KLLSKETCH"]._serialized_start = 4616
    _globals["_KLLSKETCH"]._serialized_end = 4907
    _globals["_KLLSKETCH_KLLPARAMETERS"]._serialized_start = 4753
    _globals["_KLLSKETCH_KLLPARAMETERS"]._serialized_end = 4888
    _globals["_MAXLENGTH"]._serialized_start = 4910
    _globals["_MAXLENGTH"]._serialized_end = 5072
    _globals["_MAXIMUM"]._serialized_start = 5075
    _globals["_MAXIMUM"]._serialized_end = 5235
    _globals["_MEAN"]._serialized_start = 5237
    _globals["_MEAN"]._serialized_end = 5304
    _globals["_MINLENGTH"]._serialized_start = 5307
    _globals["_MINLENGTH"]._serialized_end = 5469
    _globals["_MINIMUM"]._serialized_start = 5472
    _globals["_MINIMUM"]._serialized_end = 5632
    _globals["_MUTUALINFORMATION"]._serialized_start = 5634
    _globals["_MUTUALINFORMATION"]._serialized_end = 5716
    _globals["_PATTERNMATCH"]._serialized_start = 5719
    _globals["_PATTERNMATCH"]._serialized_end = 5910
    _globals["_RATIOOFSUMS"]._serialized_start = 5912
    _globals["_RATIOOFSUMS"]._serialized_end = 6026
    _globals["_SIZE"]._serialized_start = 6028
    _globals["_SIZE"]._serialized_end = 6071
    _globals["_STANDARDDEVIATION"]._serialized_start = 6073
    _globals["_STANDARDDEVIATION"]._serialized_end = 6153
    _globals["_SUM"]._serialized_start = 6155
    _globals["_SUM"]._serialized_end = 6221
    _globals["_UNIQUEVALUERATIO"]._serialized_start = 6224
    _globals["_UNIQUEVALUERATIO"]._serialized_end = 6395
    _globals["_UNIQUENESS"]._serialized_start = 6398
    _globals["_UNIQUENESS"]._serialized_end = 6563
# @@protoc_insertion_point(module_scope)
