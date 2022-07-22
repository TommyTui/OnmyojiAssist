# Onmyoji Assistant



------

![](https://github.com/TommyTui/OnmyojiAssist/blob/master/resources/icn.png?raw=true)

[README in English](README_en.md)

项目正在开发中。。。

一款阴阳师小助手

基于[OpenCV](https://opencv.org/)和[PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)，自动无限刷御魂

灵感来源于[MaaAssistantArknights](https://github.com/MaaAssistantArknights/MaaAssistantArknights)

------

## 基本功能

一键登录

自动锁定队伍

自动开关加成

无限刷御魂

刷觉醒材料

刷结界突破

## 以后会加的功能

刷困28

御魂/觉醒材料/困28与结界突破轮替刷，以防突破券溢出

领取日常奖励

------

## 使用方法

现在打包`paddle`和`paddleocr`有问题，一直报错，所以要运行只能新建一个python环境来运行

首先确保已安装[Anaconda](https://www.anaconda.com/)

如果你的电脑有CUDA GPU, 那么你需要安装[CUDA toolkit v11.2](https://developer.nvidia.com/cuda-11.2.0-download-archive) + [cuDNN v8.1.1](https://developer.nvidia.com/compute/machine-learning/cudnn/secure/8.1.1.33/11.2_20210301/cudnn-11.2-windows-x64-v8.1.1.33.zip) (cuDNN可能需要Nvidia developer账号)
然后你可以通过运行`setup_gpu.bat`来一键安装虚拟环境以及所有依赖

如果你的电脑不支持CUDA, 那么你可以直接运行`setup_cpu.bat`

或者你可以通过下面的方式手动安装

`conda create -n OnmyojiAssist python=3.8`

安装`paddle (gpu)`：

```
conda install paddlepaddle-gpu==2.3.1 cudatoolkit=11.2 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/ -c conda-forge
```
或`paddle (cpu)`：

```
conda install paddlepaddle==2.3.1 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/
```

安装其余：

`pip install paddleocr pygetwindow`

`conda install -c conda-forge pyautogui`

`conda install -c anaconda pyqt`

你还需要去`venv\Lib\site-packages\paddle\libs\`手动删除`libiomp5md.dll`



运行程序：

如果你通过` setup.bat`安装了虚拟环境, 或者你严格按照上面的步骤安装了虚拟环境，你可以运行`start.bat`来启动程序

你也可以通过在虚拟环境中运行`python src/main.py`来启动程序

## 使用说明

1. 项目刚开始做，可能会有不少bug
2. 仅在国服+Windows系统+英特尔处理器+RTX显卡上测试过，无法保证程序在其他平台上也能跑
3. 仅支持阴阳师桌面客户端，ios安卓号皆支持
4. 请保证阴阳师客户端在前台运行（在后台/最小化会导致程序无法截图）
5. 如果有使用多个显示器，请保证阴阳师在主显示器上
6. 如果程序卡住可能是识别出现问题，请将窗口拖到其他位置
7. 如果程序正常运行结束，加成会自动关闭。如果用户中断了程序（点了停止按钮），加成不会关闭，请手动关闭加成
8. `.exe`要以后等`paddle`和`paddleocr`修一修他们的bug才会有了

