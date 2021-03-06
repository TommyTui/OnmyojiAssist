# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 901)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 901))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 901))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 10, 371, 571))
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(2)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 371, 571))
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.verticalLayoutWidget_2.setFont(font)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.enter_game = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.enter_game.setFont(font)
        self.enter_game.setObjectName("enter_game")
        self.verticalLayout_2.addWidget(self.enter_game)
        self.soul = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.soul.setFont(font)
        self.soul.setObjectName("soul")
        self.verticalLayout_2.addWidget(self.soul)
        self.kirin = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.kirin.setFont(font)
        self.kirin.setObjectName("kirin")
        self.verticalLayout_2.addWidget(self.kirin)
        self.realm = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.realm.setFont(font)
        self.realm.setObjectName("realm")
        self.verticalLayout_2.addWidget(self.realm)
        self.exp = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.exp.setFont(font)
        self.exp.setObjectName("exp")
        self.verticalLayout_2.addWidget(self.exp)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(420, 100, 461, 381))
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 0, 10, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.soul_count = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.soul_count.setFont(font)
        self.soul_count.setMinimum(-1)
        self.soul_count.setObjectName("soul_count")
        self.gridLayout.addWidget(self.soul_count, 0, 2, 1, 1)
        self.kirin_select = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.kirin_select.setFont(font)
        self.kirin_select.setEditable(False)
        self.kirin_select.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.kirin_select.setObjectName("kirin_select")
        self.kirin_select.addItem("")
        self.kirin_select.addItem("")
        self.kirin_select.addItem("")
        self.kirin_select.addItem("")
        self.gridLayout.addWidget(self.kirin_select, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.kirin_count = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.kirin_count.setFont(font)
        self.kirin_count.setMinimum(-1)
        self.kirin_count.setObjectName("kirin_count")
        self.gridLayout.addWidget(self.kirin_count, 1, 2, 1, 1)
        self.soul_select = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.soul_select.setFont(font)
        self.soul_select.setEditable(False)
        self.soul_select.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.soul_select.setObjectName("soul_select")
        self.soul_select.addItem("")
        self.soul_select.addItem("")
        self.soul_select.addItem("")
        self.soul_select.addItem("")
        self.gridLayout.addWidget(self.soul_select, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.realm_count = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.realm_count.setFont(font)
        self.realm_count.setMinimum(-1)
        self.realm_count.setObjectName("realm_count")
        self.gridLayout.addWidget(self.realm_count, 2, 2, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 690, 371, 221))
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(50, 20, 50, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.start = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.start.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.verticalLayout.addWidget(self.start)
        self.stop = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.stop.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.stop.setFont(font)
        self.stop.setObjectName("stop")
        self.verticalLayout.addWidget(self.stop)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 580, 371, 113))
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(15, 0, 15, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.select_all = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_all.sizePolicy().hasHeightForWidth())
        self.select_all.setSizePolicy(sizePolicy)
        self.select_all.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.select_all.setFont(font)
        self.select_all.setObjectName("select_all")
        self.horizontalLayout.addWidget(self.select_all)
        self.clear_all = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_all.sizePolicy().hasHeightForWidth())
        self.clear_all.setSizePolicy(sizePolicy)
        self.clear_all.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(12)
        self.clear_all.setFont(font)
        self.clear_all.setObjectName("clear_all")
        self.horizontalLayout.addWidget(self.clear_all)
        self.logger = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.logger.setGeometry(QtCore.QRect(900, 0, 381, 901))
        font = QtGui.QFont()
        font.setFamily("SF Pro Regular")
        font.setPointSize(10)
        self.logger.setFont(font)
        self.logger.setAutoFillBackground(False)
        self.logger.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.logger.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logger.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logger.setDocumentTitle("")
        self.logger.setReadOnly(False)
        self.logger.setBackgroundVisible(True)
        self.logger.setObjectName("logger")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.kirin_select.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Onmyoji Assistant"))
        self.enter_game.setText(_translate("MainWindow", "????????????"))
        self.soul.setText(_translate("MainWindow", "?????????"))
        self.kirin.setText(_translate("MainWindow", "?????????"))
        self.realm.setText(_translate("MainWindow", "???????????????"))
        self.exp.setText(_translate("MainWindow", "??????28"))
        self.label_2.setText(_translate("MainWindow", "??????????????????"))
        self.soul_count.setToolTip(_translate("MainWindow", "???????????????-1"))
        self.soul_count.setSuffix(_translate("MainWindow", "???"))
        self.kirin_select.setItemText(0, _translate("MainWindow", "???"))
        self.kirin_select.setItemText(1, _translate("MainWindow", "???"))
        self.kirin_select.setItemText(2, _translate("MainWindow", "???"))
        self.kirin_select.setItemText(3, _translate("MainWindow", "???"))
        self.label_3.setText(_translate("MainWindow", "??????????????????"))
        self.kirin_count.setToolTip(_translate("MainWindow", "???????????????-1"))
        self.kirin_count.setSuffix(_translate("MainWindow", "???"))
        self.soul_select.setItemText(0, _translate("MainWindow", "????????????"))
        self.soul_select.setItemText(1, _translate("MainWindow", "?????????"))
        self.soul_select.setItemText(2, _translate("MainWindow", "????????????"))
        self.soul_select.setItemText(3, _translate("MainWindow", "????????????"))
        self.label_4.setText(_translate("MainWindow", "??????????????????"))
        self.realm_count.setToolTip(_translate("MainWindow", "???????????????-1"))
        self.realm_count.setSuffix(_translate("MainWindow", "???"))
        self.start.setText(_translate("MainWindow", "?????????"))
        self.stop.setText(_translate("MainWindow", "??????"))
        self.select_all.setText(_translate("MainWindow", "??????"))
        self.clear_all.setText(_translate("MainWindow", "??????"))
