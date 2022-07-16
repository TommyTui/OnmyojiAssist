from PyQt5.QtWidgets import QLabel


class Logger:
    def __init__(self, label: QLabel):
        self.log = []
        self.label = label

    def log(self, msg):
        self.log.append(msg)

    def get_log(self):
        return '\n'.join(self.log)