import os
import sys

from PyQt5.QtWidgets import QApplication

from view import Window


def clean_tmp():
    for file in os.listdir('tmp'):
        os.remove('tmp/' + file)


if __name__ == '__main__':
    clean_tmp()
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
