import os
import sys

from PyQt5.QtWidgets import QApplication

from view import Window


def init_tmp():
    if os.path.exists('tmp'):
        for file in os.listdir('tmp'):
            os.remove('tmp/' + file)
    else:
        os.mkdir('tmp')


if __name__ == '__main__':
    init_tmp()
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
