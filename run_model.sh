tools_path="/home/HwHiAiUser/tools"
app_path="/home/HwHiAiUser/photo-translator"

rm -rf tmp/output1

$tools_path/msame/out/msame \
--model $app_path/model_weights/generator-240.om \
--input $app_path/tmp/bin/i_t.bin,$app_path/tmp/bin/i_s.bin \
--output $app_path/tmp/output1 \
--outfmt BIN --loop 1
