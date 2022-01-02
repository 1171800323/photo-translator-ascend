export PATH=/usr/local/python3.7.5/bin:$PATH

export PATH=/home/HwHiAiUser/Ascend/ascend-toolkit/latest/atc/ccec_compiler/bin:/home/HwHiAiUser/Ascend/ascend-toolkit/latest/atc/bin:$PATH

export ASCEND_OPP_PATH=/home/HwHiAiUser/Ascend/ascend-toolkit/latest/opp

export ASCEND_AICPU_PATH=/home/HwHiAiUser/Ascend/ascend-toolkit/latest

export ASCEND_SLOG_PRINT_TO_STDOUT=1

atc \
--input_shape="i_t:1,3,64,208;i_s:1,3,64,208" \
--input_format=NCHW \
--model=/home/HwHiAiUser/photo-translator/model_weights/generator-208.air \
--framework=1 \
--output=/home/HwHiAiUser/photo-translator/out \
--soc_version=Ascend310
