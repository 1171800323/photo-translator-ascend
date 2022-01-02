export PATH=/usr/local/python3.7.5/bin:$PATH

export PATH=/home/HwHiAiUser/Ascend/ascend-toolkit/latest/atc/ccec_compiler/bin:/home/HwHiAiUser/Ascend/ascend-toolkit/latest/atc/bin:$PATH

export ASCEND_OPP_PATH=/home/HwHiAiUser/Ascend/ascend-toolkit/latest/opp

export ASCEND_AICPU_PATH=/home/HwHiAiUser/Ascend/ascend-toolkit/latest

export ASCEND_SLOG_PRINT_TO_STDOUT=1

atc \
--input_shape="i_t:1,3,-1,-1;i_s:1,3,-1,-1" \
--dynamic_image_size="64,128;64,256" \
--input_format=NCHW \
--model=/home/HwHiAiUser/photo-translator/generator.air \
--framework=1 \
--output=/home/HwHiAiUser/photo-translator/out \
--soc_version=Ascend310 \
--log=info > log.txt
