##  简介

- 关于昇腾相关的技术可参考我写的飞书文档：[文档1](https://kqybjxvfo3.feishu.cn/docs/doccnlj0XdgsUdQNA1KGWpKOSJg#)，[文档2](https://kqybjxvfo3.feishu.cn/docs/doccn6sbQsQ3dpsEMRDhXiWaEJb#jT6u7m)，涉及环境搭建、模型转换、AscendCL开发、交叉编译、部署等

- 这是参加互联网+产业赛道的项目，推理部分运行在昇腾310上。
    - 首先使用atc命令进行模型转换：将MindSpore框架导出的air格式转换为昇腾处理器支持的om格式
    - 然后加载om模型在昇腾310执行推理：主要依靠msame工具进行推理（没有编写ascendcl代码）

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
