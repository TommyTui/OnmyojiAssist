CALL conda.bat create -n OnmyojiAssist python=3.8
CALL conda.bat activate OnmyojiAssist
CALL conda.bat install paddlepaddle-gpu==2.3.1 cudatoolkit=11.2 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/ -c conda-forge
pip install paddleocr pygetwindow
CALL conda.bat install -c conda-forge pyautogui
CALL conda.bat install -c anaconda pyqt
python -c "import os; import sys; env_path = os.path.dirname(sys.executable); libiomp5md_path = os.sep.join([env_path, 'Lib', 'site-packages', 'paddle', 'libs', 'libiomp5md.dll']); os.remove(libiomp5md_path)"