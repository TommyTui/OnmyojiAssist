# Onmyoji Assistant

------

![](https://github.com/TommyTui/OnmyojiAssist/blob/master/resources/icn.png?raw=true)

[中文README](README.md)

Project still under development...

An assistant for [Onmyoji](https://en.onmyojigame.com/) based on [OpenCV](https://opencv.org/) and [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)

Inspired by [MaaAssistantArknights](https://github.com/MaaAssistantArknights/MaaAssistantArknights)

------

## Basic functionalities

Login on the fly

Auto lock team

Auto turn on/off buffs

Infinite soul/kirin/realm farming

## Functionalities to be added

Exp farming

Periodically switch between soul/kirin and realm to prevent excessive realm raid tickets

Receiving daily awards

------

## How to use

Currently I am having trouble packaging `paddle` and `paddleocr` (will get piles of errors with `PyInstaller` or `cx_Freeze`). The only way to run this is by creating a new python venv and installing all the required packages.

First you need to install [Anaconda](https://www.anaconda.com/) and [CUDA toolkit v11.2]([CUDA Toolkit 11.2 Downloads | NVIDIA Developer](https://developer.nvidia.com/cuda-11.2.0-download-archive)) + [cuDNN v8.1.1](https://developer.nvidia.com/compute/machine-learning/cudnn/secure/8.1.1.33/11.2_20210301/cudnn-11.2-windows-x64-v8.1.1.33.zip) (installing cuDNN may require a free Nvidia developer account).

Then you can setup the venv by running `setup.bat`.



Or you can do the following to manually set up your venv:

`conda create -n OnmyojiAssist python=3.8`

To install `paddle`:

````
conda install paddlepaddle-gpu==2.3.1 cudatoolkit=11.2 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/ -c conda-forge
````

To install the rest of packages:

`pip install paddleocr pygetwindow`

`conda install -c conda-forge pyautogui`

`conda install -c anaconda pyqt`

Then you will have to manually delete `libiomp5md.dll` located under `venv\Lib\site-packages\paddle\libs\`



To run the program:

If you setup your venv via `setup.bat`, or if you strictly follow the steps above to set up your venv, then you can run the program by running `start.bat`. 

Alternatively, you can use `python src/main.py` in your venv to run the program.

## Notes

1. Only tested on the Chinese version + Windows + Intel chip + RTX gpu. Cannot guarantee any performance on other platforms.
2. Game language must be **Chinese** to use this app.
3. Only supports the PC version. Supports both iOS and Android accounts.
4. Please make sure Onmyoji is on foreground. 
5. If you have multiple monitors, please make sure Onmyoji is on your main monitor.
6. If the program freezes, please move Onmyoji's window.
7. If the program finishes all its tasks, it will automatically turn off buffs. If the user stops the program (by hitting the stop button), the buff will not be turned of automatically. Please manually turn those off.
8. The `.exe` file will not be released until `paddle` and `paddleocr` fix their bugs. 