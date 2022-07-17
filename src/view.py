import ctypes
import logging
import threading
from threading import Thread

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QPlainTextEdit
from cv2 import error

from app import Ui_MainWindow
from game_ui_control import Control


class StopException(Exception):
    pass


class QLogger(logging.Handler, QtCore.QObject):
    appendPlainText = QtCore.pyqtSignal(str)

    def __init__(self, logger: QPlainTextEdit):
        super().__init__()
        QtCore.QObject.__init__(self)
        self.logger = logger
        self.appendPlainText.connect(self.logger.appendPlainText)
        self.setFormatter(logging.Formatter('[%(asctime)s] %(message)s', "%H:%M:%S"))

    def emit(self, record):
        msg = self.format(record)
        self.appendPlainText.emit(msg)


class Worker(Thread):

    def __init__(self, window):
        Thread.__init__(self)
        self.thread_id = None
        self.window = window
        self.control = Control()

    def run(self):
        try:
            logging.info("开始程序")
            self.thread_id = threading.get_ident()
            enter_game = self.window.enter_game.isChecked()
            soul = self.window.soul.isChecked()
            kirin = self.window.kirin.isChecked()
            realm = self.window.realm.isChecked()
            exp = self.window.exp.isChecked()

            if enter_game:
                logging.info("开始：进入游戏")
                self.control.start_game()
                logging.info("完成：进入游戏")

            self.control.home()
            if soul:
                logging.info("开始：刷御魂")
                total = int(self.window.soul_count.value())
                self.control.explore()
                self.control.start_buff('resources/soul_buff.png')
                self.control.soul()
                if self.window.soul_select.currentText() == '八岐大蛇':
                    self.control.soul_snake()
                    self.control.log_battle(total, '悲鸣', '御魂')
                elif self.window.soul_select.currentText() == '业原火':
                    self.control.soul_fire()
                    self.control.log_battle(total, '痴之阵', '御魂')
                elif self.window.soul_select.currentText() == '日轮之陨':
                    self.control.soul_sun()
                    self.control.log_battle(total, '叁层', '御魂')
                else:
                    self.control.soul_sea()
                    self.control.log_battle(total, '肆层', '御魂')
                self.control.stop_buff('resources/soul_buff.png')
                logging.info("完成：刷御魂")

            self.control.home()
            if kirin:
                logging.info("开始：刷觉醒")
                total = int(self.window.kirin_count.value())
                self.control.explore()
                self.control.start_buff('resources/kirin_buff.png')
                self.control.kirin()
                if self.window.kirin_select.currentText() == '火':
                    self.control.kirin_fire()
                    self.control.log_battle(total, '拾层', '觉醒')
                elif self.window.kirin_select.currentText() == '水':
                    self.control.kirin_water()
                    self.control.log_battle(total, '拾层', '觉醒')
                elif self.window.kirin_select.currentText() == '风':
                    self.control.kirin_wind()
                    self.control.log_battle(total, '拾层', '觉醒')
                else:
                    self.control.kirin_thunder()
                    self.control.log_battle(total, '拾层', '觉醒')
                self.control.stop_buff('resources/kirin_buff.png')
                logging.info("完成：刷觉醒")

            self.control.home()
            if realm:
                logging.info("开始：刷结界")
                total = int(self.window.realm_count.value())
                self.control.explore()
                self.control.realm()
                self.control.realm_raid(total)
                logging.info("完成：刷结界")

        except error:
            logging.error("无法截图，请确认游戏在前台运行")
        logging.info("已完成所有任务")

    def exc(self):
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(self.thread_id), ctypes.py_object(StopException))

    def get_thread_id(self):
        return self.thread_id


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowIcon(QIcon('resources/icn.png'))
        self.setupUi(self)
        self.start.clicked.connect(self.__start)
        self.stop.clicked.connect(self.__stop)
        self.worker = None
        logger = QLogger(self.logger)
        logging.getLogger().addHandler(logger)
        logging.getLogger().setLevel(logging.DEBUG)

    def __start(self):
        self.worker = Worker(self)
        self.worker.start()

    def __stop(self):
        if self.worker.get_thread_id() is not None:
            self.worker.exc()
            self.worker.join()
            logging.info("已终止")
