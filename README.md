##  简介

- 这是参加互联网+产业赛道的项目，推理部分运行在昇腾310上。首先使用atc命令将SRNet模型从air模型转换为om模型，然后利用om模型进行推理。

- CANN版本：

    - ascend-toolkit 5.0.3.alpha001
    - nnrt: 5.0.3.alpha001

- 模型文件地址：

    - 百度网盘：https://pan.baidu.com/s/1pPu1evDi-7rKjvSxgvTxKA
    - 提取码：asfb


- 加载om模型执行推理：

```
# python3 npu_inference.py
```