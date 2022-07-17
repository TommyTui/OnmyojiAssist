# Onmyoji Assistant

------

![](https://github.com/TommyTui/OnmyojiAssist/blob/master/resources/icn.png?raw=true)

[中文README](README.md)

Project still under development...

An assistant for [Onmyoji](https://en.onmyojigame.com/) based on CV

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

`python version == 3.8`

Install [CUDA toolkit v11.2]([CUDA Toolkit 11.2 Downloads | NVIDIA Developer](https://developer.nvidia.com/cuda-11.2.0-download-archive)) + [cudnn v8.1.1](https://developer.nvidia.com/compute/machine-learning/cudnn/secure/8.1.1.33/11.2_20210301/cudnn-11.2-windows-x64-v8.1.1.33.zip) (installing cudnn may require a free Nvidia developer account) first.

To install `paddle`:

`conda install paddlepaddle-gpu==2.3.1 cudatoolkit=11.2 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/ -c conda-forge `

To install the rest of packages:

`pip install paddleocr pygetwindow`

`conda install -c conda-forge pyautogui`

`conda install -c anaconda pyqt`

To run the program:

`python src/main.py`

## Notes

1. Only tested on the Chinese version + Windows + Intel chip + RTX gpu. Cannot guarantee any performance on other platforms.
2. Game language must be **Chinese** to use this app.
3. Only supports the PC version. Supports both iOS and Android accounts.
4. Please make sure Onmyoji is on foreground. 
5. If you have multiple monitors, please make sure Onmyoji is on your main monitor.
6. If the program freezes, please move Onmyoji's window.
7. If the program finishes all its tasks, it will automatically turn off buffs. If the user stops the program (by hitting the stop button), the buff will not be turned of automatically. Please manually turn those off.
8. The `.exe` file will not be released until `paddle` and `paddleocr` fix their bugs. 