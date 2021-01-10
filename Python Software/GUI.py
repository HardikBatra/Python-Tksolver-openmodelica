# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SCREEN1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as P
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
import numpy as N
from pyfmi import load_fmu
import win32com.client
import sqlite3
import win32com.client.combrowse as com
class Ui_MainWindow(object):
    def ex(self):
        sys.exit()

    def openwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def openwindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def openwindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow14()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 90, 1161, 591))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("background-color: rgb(76, 124, 255);\n"
"font: 28pt \"MV Boli\";\n"
"\n"
"")
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.clicked.connect(self.openwindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("background-color: rgb(39, 234, 255);\n"
"font: 28pt \"MV Boli\";\n"
"\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 28pt \"MV Boli\";\n"
"\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.openwindow2)
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("background-color: rgb(179, 255, 175);\n"
"font: 28pt \"MV Boli\";\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.ex)
        self.horizontalLayout.addWidget(self.pushButton_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_6.clicked.connect(self.openwindow1)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_6.setText(_translate("MainWindow", "ACTIVE FILTERS"))
        self.pushButton_5.setText(_translate("MainWindow", "RLC CIRCUIT ANALYSIS"))
        self.pushButton_7.setText(_translate("MainWindow", "DATABASE"))
        self.pushButton_4.setText(_translate("MainWindow", "EXIT"))
class Ui_MainWindow2(object):
    def ex(self):
        sys.exit()
    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def openwindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow12()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def openwindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow13()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300, 100)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(980, 20, 111, 41))
        self.pushButton_15.setStyleSheet("font: 20pt \"MV Boli\";\n"
"background-color: rgb(238, 255, 254);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(self.back)


        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(1280, 310, 61, 21))
        self.pushButton_16.setStyleSheet("font: 12pt \"MV Boli\";\n"
"background-color: rgb(238, 255, 254);")
        self.pushButton_16.setObjectName("pushButton_16")


        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 80, 1101, 651))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(34)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setMouseTracking(True)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_6.setStyleSheet("background-color: rgb(76, 124, 255);\n"
"font: 34pt \"MV Boli\";\n"
"\n"
"\n"
"\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("background-color: rgb(201, 255, 156);\n"
"\n"
"font: 34pt \"MV Boli\";\n"
"\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.pushButton_6.clicked.connect(self.openwindow1)
        self.pushButton_9.clicked.connect(self.openwindow2)
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(1100, 20, 121, 41))
        self.pushButton_17.setStyleSheet("font: 20pt \"MV Boli\";\n"
"background-color: rgb(238, 255, 254);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(self.ex)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_15.setText(_translate("MainWindow", "BACK"))
        self.pushButton_16.setText(_translate("MainWindow", "EXIT"))
        self.pushButton_6.setText(_translate("MainWindow", "RLC SERIES"))
        self.pushButton_9.setText(_translate("MainWindow", "RLC PARALLEL"))
        self.pushButton_17.setText(_translate("MainWindow", "EXIT"))
class Ui_MainWindow3(object):
    def ex(self):
        sys.exit()
    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def openwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow4()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def openwindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow6()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def openwindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow8()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def openwindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow5()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def openwindow4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow7()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def openwindow5(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow9()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def openwindow6(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow10()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def openwindow7(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow11()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300, 100)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 60, 1178, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setMouseTracking(True)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_6.setStyleSheet("background-color: rgb(76, 124, 255);\n"
"font: 22pt \"MV Boli\";\n"
"\n"
"\n"
"\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_6.clicked.connect(self.openwindow)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("background-color: rgb(76, 124, 255);\n"
"\n"
"font: 22pt \"MV Boli\";\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.openwindow1)
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_11 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("background-color: rgb(76, 124, 255);\n"
"font: 22pt \"MV Boli\";\n"
"")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout.addWidget(self.pushButton_11)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(80, 230, 1193, 161))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("background-color: rgb(201, 255, 156);\n"
"font: 22pt \"MV Boli\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("background-color: rgb(201, 255, 156);\n"
"\n"
"font: 22pt \"MV Boli\";\n"
"\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("background-color: rgb(201, 255, 156);\n"
"font: 22pt \"MV Boli\";\n"
"")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_2.addWidget(self.pushButton_12)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(80, 430, 1071, 141))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_13 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("background-color: rgb(88, 242, 255);\n"
"font: 20pt \"MV Boli\";\n"
"")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_3.addWidget(self.pushButton_13)
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("background-color: rgb(88, 242, 255);\n"
"font: 20pt \"MV Boli\";\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(80, 600, 1071, 131))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_14 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setStyleSheet("background-color: rgb(238, 255, 254);\n"
"font: 22pt \"MV Boli\";")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(self.back)
        self.horizontalLayout_4.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setStyleSheet("font: 22pt \"MV Boli\";\n"
"background-color: rgb(238, 255, 254);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(self.ex)
        self.horizontalLayout_4.addWidget(self.pushButton_15)
        self.pushButton_11.clicked.connect(self.openwindow2)
        self.pushButton_8.clicked.connect(self.openwindow3)
        self.pushButton_9.clicked.connect(self.openwindow4)
        self.pushButton_12.clicked.connect(self.openwindow5)
        self.pushButton_13.clicked.connect(self.openwindow6)
        self.pushButton_10.clicked.connect(self.openwindow7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_6.setText(_translate("MainWindow", "ACTIVE LOW PASS FILTER\n"
" (FIRST ORDER)"))
        self.pushButton_7.setText(_translate("MainWindow", "ACTIVE LOW PASS FILTER \n"
"(SECOND ORDER)"))
        self.pushButton_11.setText(_translate("MainWindow", "ACTIVE LOW PASS FILTER \n"
"(COMBINED)"))
        self.pushButton_8.setText(_translate("MainWindow", "ACTIVE HIGH PASS FILTER \n"
"(FIRST ORDER)"))
        self.pushButton_9.setText(_translate("MainWindow", "ACTIVE HIGH PASS FILTER\n"
" (SECOND ORDER)"))
        self.pushButton_12.setText(_translate("MainWindow", "ACTIVE HIGH PASS FILTER \n"
"(COMBINED)"))
        self.pushButton_13.setText(_translate("MainWindow", "ACTIVE BAND PASS FILTER "))
        self.pushButton_10.setText(_translate("MainWindow", " ACTIVE BAND STOP FILTER"))
        self.pushButton_14.setText(_translate("MainWindow", "BACK"))
        self.pushButton_15.setText(_translate("MainWindow", "EXIT"))
class Ui_MainWindow4(object):
    def calculate(self):
        model = load_fmu("activelowpass.fmu")
        objTKSolver = win32com.client.Dispatch("TKWX.Document")
        objTKSolver.LoadModel("r", r"C:\Users\HARDIK\UTS_PROJECT\ActiveLowPassFilter.tkwx")

        r1 =self.lineEdit_2.text()
        r2 =self.lineEdit_9.text()
        r3 =self.lineEdit_8.text()
        c1 =self.lineEdit_11.text()
        vin =self.lineEdit_10.text()
        f =self.lineEdit.text()

        model.set("R1.R", r1)
        model.set("R2.R", r2)
        model.set("R3.R", r3)
        model.set("C1.C", c1)
        model.set("sineVoltage.V", vin)
        model.set("sineVoltage.freqHz", f)

        res = model.simulate()

        objTKSolver.SetValue("R1", "i", r1)
        objTKSolver.SetValue("C", "i", c1)
        objTKSolver.SetValue("R2", "i", r2)
        objTKSolver.SetValue("R3", "i", r3)
        objTKSolver.SetValue("f", "i", f)
        objTKSolver.SetValue("vin", "i", vin)
        objTKSolver.SetValue("vout", "i", max(res['voltageSensor.v']))
        objTKSolver.Solve()
        fc = objTKSolver.GetValue("Fc", "o")
        Amax = objTKSolver.GetValue("Amax", "o")
        VoltageGain = objTKSolver.GetValue("VoltageGain", "o")
        voltage_gain = objTKSolver.GetValue("voltagegain", "o")
        gain_in_dB = objTKSolver.GetValue("gain_in_dB", "o")

        self.textBrowser.setText(fc)
        self.textBrowser_2.setText(Amax)
        self.textBrowser_3.setText(VoltageGain)
        self.textBrowser_4.setText(voltage_gain)
        self.textBrowser_5.setText(gain_in_dB)
        P.figure(figsize=(8, 6))
        P.grid(True)
        P.plot(res['sineVoltage.v'], 'r', linewidth=1.0, color="mediumvioletred", label='INPUT Voltage')
        P.plot(res['voltageSensor.v'], 'r', linewidth=1.0, color="aqua", label='OUTPUT Voltage')
        P.title("INPUT OUPUT Voltages")
        P.ylabel('Voltage (V)')
        P.xlabel('Time')
        P.legend()
        P.savefig("plot1.png")

        x1 = []
        x11 = []
        y1 = []
        y11 = []
        z1 = []
        z11 = []

        f1 = 1
        f2 = int(float(fc)) * 10
        for i in range(f1, f2, 1):
            objTKSolver.SetSubCell("l", 1, i, 1, str(i))
        objTKSolver.ListSolve()
        index = objTKSolver.GetObjIndex("p", "P1")
        prop1 = objTKSolver.GetProperty("p", index, 1)
        xlist = objTKSolver.GetSubCell("p", index, 1, 1)
        ylist = objTKSolver.GetSubCell("p", index, 1, 2)
        zlist = objTKSolver.GetSubCell("p", index, 2, 1)
        xListIndex = objTKSolver.GetObjIndex("l", xlist)
        yListIndex = objTKSolver.GetObjIndex("l", ylist)
        zListIndex = objTKSolver.GetObjIndex("l", zlist)
        for i in range(1, f2):
            x1.append(objTKSolver.GetSubCell("l", xListIndex, i, 1))
            x11.append(float(x1[i - 1]))
        for i in range(1, f2):
            y1.append(objTKSolver.GetSubCell("l", yListIndex, i, 1))
            y11.append(float(y1[i - 1]))

        for i in range(1, f2):
            z1.append(objTKSolver.GetSubCell("l", zListIndex, i, 1))
            z11.append(float(z1[i - 1]))

        P.figure(figsize=(8, 6))
        P.grid(True)
        P.xscale('log')

        P.plot(z11, y11, linewidth=1.5, color="limegreen", linestyle='dashed', label='Cut off frequency')
        P.plot(x11, y11, linewidth=2.0, color="magenta")

        P.fill_between(x11, y11, color='lavender')
        P.title("VOLTAGE GAIN IN dB VS FREQUENCY")
        P.ylabel('Voltage Gain in dB')
        P.xlabel('Frequency (Hz)')
        P.legend()
        P.savefig("plot2.png")

        conn = sqlite3.connect('mydb.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO Activelowpass1 (r1,r2,r3,c1,vin,f,fc,Amax,VoltageGain,voltage_gain,gain_in_dB) VALUES (?, ?, ?, ?,?, ?, ?, ?,?,?,?)",
            (r1, r2, r3, c1, vin, f, fc, Amax, VoltageGain, voltage_gain, gain_in_dB))

        conn.commit()
        conn.close()

        self.HandleQuestion()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 260, 461, 41))
        self.pushButton.setStyleSheet("background-color: rgb(87, 175, 0);\n"
"\n"
"font: 37pt \"MS Sans Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 312, 242))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(340, 40, 221, 231))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_2.addWidget(self.lineEdit_11)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_2.addWidget(self.lineEdit_10)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 350, 351, 391))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../UTS_PROJECT/ActiveLowPassFilter.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(570, 40, 421, 201))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_14.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(400, 330, 351, 421))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(790, 340, 381, 411))
        self.label_9.setObjectName("label_9")
        self.label_9.setScaledContents(True)
        self.label_8.setScaledContents(True)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1000, 40, 256, 41))
        self.textBrowser.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1000, 80, 256, 41))
        self.textBrowser_2.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(1000, 120, 256, 41))
        self.textBrowser_3.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(1000, 160, 256, 41))
        self.textBrowser_4.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(1000, 200, 256, 41))
        self.textBrowser_5.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "CALCULATE"))
        self.label.setText(_translate("MainWindow", "Enter value of R1"))
        self.label_2.setText(_translate("MainWindow", "Enter value of R2"))
        self.label_3.setText(_translate("MainWindow", "Enter value of R3"))
        self.label_4.setText(_translate("MainWindow", "Enter value of C1"))
        self.label_6.setText(_translate("MainWindow", "Enter value of frequency"))
        self.label_5.setText(_translate("MainWindow", "Enter value of voltage"))
        self.label_10.setText(_translate("MainWindow", "Cutoff frequency"))
        self.label_11.setText(_translate("MainWindow", "Gain of the pass band"))
        self.label_12.setText(_translate("MainWindow", "Voltage Gain (Amax / √{1+(f/fc)²"))
        self.label_13.setText(_translate("MainWindow", "Voltage Gain (Vout/Vin) "))
        self.label_14.setText(_translate("MainWindow", "The gain in dB is given is 20log (VG)"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
    def HandleQuestion(self):
        pic = self.label_8
        pic1=self.label_9
        pic.setPixmap(QtGui.QPixmap("plot1.png"))
        pic1.setPixmap(QtGui.QPixmap("plot2.png"))
        pic.show()
        pic1.show()
class Ui_MainWindow5(object):
    def calculate(self):
        model = load_fmu("activehighpass.fmu")
        objTKSolver = win32com.client.Dispatch("TKWX.Document")
        objTKSolver.LoadModel("r", r"C:\Users\HARDIK\UTS_PROJECT\activehighpass.tkwx")
        r1 =self.lineEdit_2.text()
        r2 =self.lineEdit_9.text()
        r3 =self.lineEdit_8.text()
        c1 =self.lineEdit_11.text()
        vin =self.lineEdit_10.text()
        f =self.lineEdit.text()
        model.set("r1.R", r1)
        model.set("r2.R", r2)
        model.set("r3.R", r3)
        model.set("c1.C", c1)
        model.set("sineVoltage.V", vin)
        model.set("sineVoltage.freqHz", f)
        res = model.simulate()
        objTKSolver.SetValue("R1", "i", r1)
        objTKSolver.SetValue("C", "i", c1)
        objTKSolver.SetValue("R2", "i", r2)
        objTKSolver.SetValue("R3", "i", r3)
        objTKSolver.SetValue("f", "i", f)
        objTKSolver.SetValue("vin", "i", vin)
        objTKSolver.SetValue("vout", "i", max(res['opAmp.out.v']))
        objTKSolver.Solve()
        fc = objTKSolver.GetValue("Fc", "o")
        Amax = objTKSolver.GetValue("Amax", "o")
        VoltageGain = objTKSolver.GetValue("VoltageGain", "o")
        voltage_gain = objTKSolver.GetValue("voltagegain", "o")
        gain_in_dB = objTKSolver.GetValue("gain_in_dB", "o")
        phi = objTKSolver.GetValue("phi", "o")

        self.textBrowser.setText(fc)
        self.textBrowser_2.setText(Amax)
        self.textBrowser_3.setText(VoltageGain)
        self.textBrowser_4.setText(voltage_gain)
        self.textBrowser_5.setText(gain_in_dB)

        P.figure(figsize=(8, 6))
        P.grid(True)
        P.plot(res['opAmp.out.v'], 'r', linewidth=1.0, color="aqua", label='OUTPUT Voltage')
        P.title("OUPUT Voltage")
        P.ylabel('Voltage (V)')
        P.xlabel('Time')
        P.xscale("log")
        P.legend()
        P.savefig("plot9.png")

        x1 = []
        x11 = []
        y1 = []
        y11 = []
        z1 = []
        z11 = []

        f1 = 1
        f2 = int(float(fc)) * 10
        if (f2 > 64000):
            f2 = 64000
        for i in range(f1, f2, 1):
            objTKSolver.SetSubCell("l", 1, i, 1, str(i))
        objTKSolver.ListSolve()
        index = objTKSolver.GetObjIndex("p", "P1")
        prop1 = objTKSolver.GetProperty("p", index, 1)
        xlist = objTKSolver.GetSubCell("p", index, 1, 1)
        ylist = objTKSolver.GetSubCell("p", index, 1, 2)
        zlist = objTKSolver.GetSubCell("p", index, 2, 1)
        xListIndex = objTKSolver.GetObjIndex("l", xlist)
        yListIndex = objTKSolver.GetObjIndex("l", ylist)
        zListIndex = objTKSolver.GetObjIndex("l", zlist)
        for i in range(1, f2):
            x1.append(objTKSolver.GetSubCell("l", xListIndex, i, 1))
            x11.append(float(x1[i - 1]))
        for i in range(1, f2):
            y1.append(objTKSolver.GetSubCell("l", yListIndex, i, 1))
            y11.append(float(y1[i - 1]))

        for i in range(1, f2):
            z1.append(objTKSolver.GetSubCell("l", zListIndex, i, 1))
            z11.append(float(z1[i - 1]))

        P.figure(figsize=(8, 6))
        P.grid(True)
        P.xscale('log')
        P.plot(z11, y11, linewidth=1.5, color="limegreen", linestyle='dashed', label='Cut off frequency')
        P.plot(x11, y11, linewidth=2.0, color="magenta")
        # P. fill_between(x11, y11,np.max(y11),color='lavender')
        P.title("VOLTAGE GAIN IN dB VS FREQUENCY")
        P.ylabel('Voltage Gain in dB')
        P.xlabel('Frequency (Hz)')
        P.savefig("plot10.png")
        conn = sqlite3.connect('mydb.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO Activehighpass1 (r1,r2,r3,c1,vin,f,fc,Amax,VoltageGain,voltage_gain,gain_in_dB) VALUES (?, ?, ?, ?,?, ?, ?, ?,?,?,?)",
            (r1, r2, r3, c1, vin, f, fc, Amax, VoltageGain, voltage_gain, gain_in_dB))

        conn.commit()
        conn.close()

        self.HandleQuestion()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)

        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 320, 351, 391))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../UTS_PROJECT/activehighpass.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 312, 242))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(330, 10, 221, 241))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_2.addWidget(self.lineEdit_11)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_2.addWidget(self.lineEdit_10)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(450, 320, 351, 391))
        self.label_8.setText("")
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(560, 10, 421, 231))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_14.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(980, 10, 251, 231))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_2.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_4.addWidget(self.textBrowser_2)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_3.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_4.addWidget(self.textBrowser_3)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_4.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.verticalLayout_4.addWidget(self.textBrowser_4)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_5.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_4.addWidget(self.textBrowser_5)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 260, 671, 51))
        self.pushButton.setStyleSheet("background-color: rgb(87, 175, 0);\n"
"\n"
"font: 37pt \"MS Sans Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(840, 320, 381, 401))
        self.label_9.setText("")
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter value of R1"))
        self.label_2.setText(_translate("MainWindow", "Enter value of R2"))
        self.label_3.setText(_translate("MainWindow", "Enter value of R3"))
        self.label_4.setText(_translate("MainWindow", "Enter value of C1"))
        self.label_6.setText(_translate("MainWindow", "Enter value of frequency"))
        self.label_5.setText(_translate("MainWindow", "Enter value of voltage"))
        self.label_10.setText(_translate("MainWindow", "Cutoff frequency"))
        self.label_11.setText(_translate("MainWindow", "Gain of the pass band"))
        self.label_12.setText(_translate("MainWindow", "Voltage Gain (Amax / √{1+(f/fc)²"))
        self.label_13.setText(_translate("MainWindow", "Voltage Gain (Vout/Vin) "))
        self.label_14.setText(_translate("MainWindow", "The gain in dB is given is 20log (VG)"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "CALCULATE"))
    def HandleQuestion(self):
        pic = self.label_8
        pic1=self.label_9
        pic.setPixmap(QtGui.QPixmap("plot9.png"))
        pic1.setPixmap(QtGui.QPixmap("plot10.png"))
        pic.show()
        pic1.show()
class Ui_MainWindow6(object):
    def calculate(self):
        model = load_fmu("activelowpassSecondOrder.fmu")
        objTKSolver = win32com.client.Dispatch("TKWX.Document")
        objTKSolver.LoadModel("r", r"C:\Users\HARDIK\UTS_PROJECT\activelowpassSecondOrder.tkwx")
        print("\n\n")
        R1 = self.lineEdit_2.text()
        R2 = self.lineEdit_9.text()
        R3 = self.lineEdit_8.text()
        R4 = self.lineEdit_11.text()
        C1 = self.lineEdit_12.text()
        C2 = self.lineEdit_13.text()
        f = self.lineEdit_10.text()
        vin = self.lineEdit.text()

        model.set("R1.R", R1)
        model.set("R2.R", R2)
        model.set("R3.R", R3)
        model.set("R4.R", R4)
        model.set("C1.C", C1)
        model.set("C2.C", C2)
        model.set("sineVoltage.V", vin)
        model.set("sineVoltage.freqHz", f)
        res = model.simulate()
        objTKSolver.SetValue("R1", "i", R1)
        objTKSolver.SetValue("R2", "i", R2)
        objTKSolver.SetValue("R3", "i", R3)
        objTKSolver.SetValue("R4", "i", R4)
        objTKSolver.SetValue("C1", "i", C1)
        objTKSolver.SetValue("C2", "i", C2)
        objTKSolver.SetValue("f", "i", f)
        objTKSolver.SetValue("vin", "i", vin)
        objTKSolver.SetValue("vout", "i", max(res['voltageSensor.v']))
        objTKSolver.Solve()
        fc = objTKSolver.GetValue("Fc", "o")
        Av = objTKSolver.GetValue("Av", "o")
        voltage_gain = objTKSolver.GetValue("voltagegain", "o")
        gain_in_dB = objTKSolver.GetValue("gain_in_dB", "o")
        VoltageGain = objTKSolver.GetValue("VoltageGain", "o")
        V=max(res['voltageSensor.v'])
        self.textBrowser_6.setText(str(V))
        self.textBrowser.setText(fc)
        self.textBrowser_2.setText(Av)
        self.textBrowser_3.setText(VoltageGain)
        self.textBrowser_4.setText(voltage_gain)
        self.textBrowser_5.setText(gain_in_dB)

        P.figure(figsize=(8, 6))
        P.grid(True)
        P.plot(res['sineVoltage.v'], 'r', linewidth=1.0, color="limegreen", label='INPUT Voltage')
        P.plot(res['voltageSensor.v'], 'r', linewidth=1.0, color="orange", label='OUTPUT Voltage')
        P.title("INPUT OUPUT Voltages")
        P.ylabel('Voltage (V)')
        P.xlabel('Time')
        P.legend()
        P.savefig("plot3.png")

        x1 = []
        x11 = []
        y1 = []
        y11 = []
        z1 = []
        z11 = []

        f1 = 1
        f2 = int(float(fc)) * 10
        for i in range(f1, f2, 1):
            objTKSolver.SetSubCell("l", 1, i, 1, str(i))
        objTKSolver.ListSolve()
        index = objTKSolver.GetObjIndex("p", "P1")
        prop1 = objTKSolver.GetProperty("p", index, 1)
        xlist = objTKSolver.GetSubCell("p", index, 1, 1)
        ylist = objTKSolver.GetSubCell("p", index, 1, 2)
        zlist = objTKSolver.GetSubCell("p", index, 2, 1)
        xListIndex = objTKSolver.GetObjIndex("l", xlist)
        yListIndex = objTKSolver.GetObjIndex("l", ylist)
        zListIndex = objTKSolver.GetObjIndex("l", zlist)
        for i in range(1, f2):
            x1.append(objTKSolver.GetSubCell("l", xListIndex, i, 1))
            x11.append(float(x1[i - 1]))
        for i in range(1, f2):
            y1.append(objTKSolver.GetSubCell("l", yListIndex, i, 1))
            y11.append(float(y1[i - 1]))

        for i in range(1, f2):
            z1.append(objTKSolver.GetSubCell("l", zListIndex, i, 1))
            z11.append(float(z1[i - 1]))

        P.figure(figsize=(8, 6))
        P.grid(True)
        P.xscale('log')
        P.plot(z11, y11, linewidth=1.5, color="limegreen", linestyle='dashed', label='Cut off frequency')
        P.plot(x11, y11, linewidth=2.0, color="magenta")
        P.fill_between(x11, y11, color='lavender')
        P.title("VOLTAGE GAIN IN dB VS FREQUENCY")
        P.ylabel('Voltage Gain in dB')
        P.xlabel('Frequency (Hz)')
        P.legend()
        P.savefig("plot4.png")
        conn = sqlite3.connect('mydb.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO Activelowpass2 (R1,R2,R3,R4,C1,C2,f,vin,fc,Av,voltage_gain,gain_in_dB,VoltageGain) VALUES (?, ?, ?, ?,?, ?, ?, ?,?,?,?,?,?)",
            (R1, R2, R3, R4, C1, C2, f, vin, fc, Av, voltage_gain, gain_in_dB, VoltageGain))

        conn.commit()
        conn.close()

        self.HandleQuestion()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)

        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(320, 0, 211, 321))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_2.addWidget(self.lineEdit_11)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy)
        self.lineEdit_12.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_2.addWidget(self.lineEdit_12)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy)
        self.lineEdit_13.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_2.addWidget(self.lineEdit_13)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_2.addWidget(self.lineEdit_10)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 340, 351, 391))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../UTS_PROJECT/activelowpasssecondorder.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(960, 0, 251, 231))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_6.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.verticalLayout_4.addWidget(self.textBrowser_6)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_2.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_4.addWidget(self.textBrowser_2)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_3.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_4.addWidget(self.textBrowser_3)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_4.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.verticalLayout_4.addWidget(self.textBrowser_4)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_5.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_4.addWidget(self.textBrowser_5)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(790, 340, 381, 381))
        self.label_9.setText("")
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 312, 324))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(390, 350, 351, 371))
        self.label_8.setText("")
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 250, 671, 51))
        self.pushButton.setStyleSheet("background-color: rgb(87, 175, 0);\n"
"\n"
"font: 37pt \"MS Sans Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(540, 0, 421, 231))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_14.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1265, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.calculate)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Enter value of R1"))
        self.label_2.setText(_translate("MainWindow", "Enter value of R2"))
        self.label_3.setText(_translate("MainWindow", "Enter value of R3"))
        self.label_15.setText(_translate("MainWindow", "Enter value of R4"))
        self.label_4.setText(_translate("MainWindow", "Enter value of C1"))
        self.label_16.setText(_translate("MainWindow", "Enter value of C2"))
        self.label_6.setText(_translate("MainWindow", "Enter value of frequency"))
        self.label_5.setText(_translate("MainWindow", "Enter value of voltage"))
        self.pushButton.setText(_translate("MainWindow", "CALCULATE"))
        self.label_10.setText(_translate("MainWindow", "Voltage Output"))
        self.label_17.setText(_translate("MainWindow", "Cutoff frequency"))
        self.label_11.setText(_translate("MainWindow", "Gain of the pass band"))
        self.label_12.setText(_translate("MainWindow", "Voltage Gain (Amax / √{1+(f/fc)²"))
        self.label_13.setText(_translate("MainWindow", "Voltage Gain (Vout/Vin) "))
        self.label_14.setText(_translate("MainWindow", "The gain in dB is given is 20log (VG)"))
    def HandleQuestion(self):
        pic = self.label_8
        pic1=self.label_9
        pic.setPixmap(QtGui.QPixmap("plot3.png"))
        pic1.setPixmap(QtGui.QPixmap("plot4.png"))
        pic.show()
        pic1.show()
class Ui_MainWindow7(object):
    def calculate(self):
        model = load_fmu("activehighpasssecond.fmu")
        objTKSolver = win32com.client.Dispatch("TKWX.Document")
        objTKSolver.LoadModel("r", r"C:\Users\HARDIK\UTS_PROJECT\activehighpasssecond.tkwx")
        R1 = self.lineEdit_2.text()
        R2 = self.lineEdit_9.text()
        R3 = self.lineEdit_8.text()
        R4 = self.lineEdit_11.text()
        C1 = self.lineEdit_12.text()
        C2 = self.lineEdit_13.text()
        f = self.lineEdit_10.text()
        vin = self.lineEdit.text()

        model.set("resistor1.R", R1)
        model.set("resistor2.R", R2)
        model.set("r3.R", R3)
        model.set("r4.R", R4)
        model.set("c1.C", C1)
        model.set("c2.C", C2)
        model.set("sineVoltage.V", vin)
        model.set("sineVoltage.freqHz", f)
        print("\n  SIMULATING....")
        res = model.simulate()
        objTKSolver.SetValue("R1", "i", R1)
        objTKSolver.SetValue("R2", "i", R2)
        objTKSolver.SetValue("R3", "i", R3)
        objTKSolver.SetValue("R4", "i", R4)
        objTKSolver.SetValue("C1", "i", C1)
        objTKSolver.SetValue("C2", "i", C2)
        objTKSolver.SetValue("f", "i", f)
        objTKSolver.SetValue("vin", "i", vin)
        objTKSolver.SetValue("vout", "i", max(res['opAmp.out.v']))
        objTKSolver.Solve()
        fc = objTKSolver.GetValue("Fc", "o")
        Av = objTKSolver.GetValue("Av", "o")
        voltage_gain = objTKSolver.GetValue("voltagegain", "o")
        gain_in_dB = objTKSolver.GetValue("gain_in_dB", "o")
        VoltageGain = objTKSolver.GetValue("VoltageGain", "o")
        V = max(res['opAmp.out.v'])
        self.textBrowser_6.setText(str(V))
        self.textBrowser.setText(fc)
        self.textBrowser_2.setText(Av)
        self.textBrowser_3.setText(VoltageGain)
        self.textBrowser_4.setText(voltage_gain)
        self.textBrowser_5.setText(gain_in_dB)


        P.figure(figsize=(8, 6))
        P.grid(True)
        # P.plot(res['sineVoltage.v'],'r',linewidth=1.0,color="limegreen",label='INPUT Voltage')
        P.plot(res['opAmp.out.v'], 'r', linewidth=1.0, color="orange", label='OUTPUT Voltage')
        P.title("OUPUT Voltage")
        P.ylabel('Voltage (V)')
        P.xlabel('Time')
        P.legend()
        P.savefig("plot11.png")

        x1 = []
        x11 = []
        y1 = []
        y11 = []
        z1 = []
        z11 = []

        f1 = 1
        f2 = int(float(fc)) * 10
        if (f2 > 64000):
            f2 = 64000
        for i in range(f1, f2, 1):
            objTKSolver.SetSubCell("l", 1, i, 1, str(i))
        objTKSolver.ListSolve()
        index = objTKSolver.GetObjIndex("p", "P1")
        prop1 = objTKSolver.GetProperty("p", index, 1)
        xlist = objTKSolver.GetSubCell("p", index, 1, 1)
        ylist = objTKSolver.GetSubCell("p", index, 1, 2)
        zlist = objTKSolver.GetSubCell("p", index, 2, 1)
        xListIndex = objTKSolver.GetObjIndex("l", xlist)
        yListIndex = objTKSolver.GetObjIndex("l", ylist)
        zListIndex = objTKSolver.GetObjIndex("l", zlist)
        for i in range(1, f2):
            x1.append(objTKSolver.GetSubCell("l", xListIndex, i, 1))
            x11.append(float(x1[i - 1]))
        for i in range(1, f2):
            y1.append(objTKSolver.GetSubCell("l", yListIndex, i, 1))
            y11.append(float(y1[i - 1]))

        for i in range(1, f2):
            z1.append(objTKSolver.GetSubCell("l", zListIndex, i, 1))
            z11.append(float(z1[i - 1]))

        P.figure(figsize=(8, 6))
        P.grid(True)
        P.xscale('log')
        P.plot(z11, y11, linewidth=1.5, color="limegreen", linestyle='dashed', label='Cut off frequency')
        P.plot(x11, y11, linewidth=2.0, color="magenta")
        # P. fill_between(x11, y11,np.max(x11),color='lavender')
        P.title("VOLTAGE GAIN IN dB VS FREQUENCY")
        P.ylabel('Voltage Gain in dB')
        P.xlabel('Frequency (Hz)')
        P.legend()
        P.savefig("plot12.png")
        conn = sqlite3.connect('mydb.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO Activehighpass2 (R1,R2,R3,R4,C1,C2,f,vin,fc,Av,voltage_gain,gain_in_dB,VoltageGain) VALUES (?, ?, ?, ?,?, ?, ?, ?,?,?,?,?,?)",
            (R1, R2, R3, R4, C1, C2, f, vin, fc, Av, voltage_gain, gain_in_dB, VoltageGain))

        conn.commit()
        conn.close()

        self.HandleQuestion()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)

        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(810, 340, 381, 381))
        self.label_9.setText("")
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 250, 671, 51))
        self.pushButton.setStyleSheet("background-color: rgb(87, 175, 0);\n"
"\n"
"font: 37pt \"MS Sans Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(980, 0, 251, 231))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_6.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.verticalLayout_4.addWidget(self.textBrowser_6)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_2.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_4.addWidget(self.textBrowser_2)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_3.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_4.addWidget(self.textBrowser_3)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_4.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.verticalLayout_4.addWidget(self.textBrowser_4)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_5.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_4.addWidget(self.textBrowser_5)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(560, 0, 421, 231))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_14.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(340, 0, 211, 321))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_2.addWidget(self.lineEdit_11)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy)
        self.lineEdit_12.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_2.addWidget(self.lineEdit_12)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy)
        self.lineEdit_13.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_2.addWidget(self.lineEdit_13)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_2.addWidget(self.lineEdit_10)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 340, 351, 391))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../UTS_PROJECT/activehighpasssecond.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 0, 312, 324))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 350, 351, 371))
        self.label_8.setText("")
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "CALCULATE"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "Voltage Output"))
        self.label_17.setText(_translate("MainWindow", "Cutoff frequency"))
        self.label_11.setText(_translate("MainWindow", "Gain of the pass band"))
        self.label_12.setText(_translate("MainWindow", "Voltage Gain (Amax / √{1+(f/fc)²"))
        self.label_13.setText(_translate("MainWindow", "Voltage Gain (Vout/Vin) "))
        self.label_14.setText(_translate("MainWindow", "The gain in dB is given is 20log (VG)"))
        self.label.setText(_translate("MainWindow", "Enter value of R1"))
        self.label_2.setText(_translate("MainWindow", "Enter value of R2"))
        self.label_3.setText(_translate("MainWindow", "Enter value of R3"))
        self.label_15.setText(_translate("MainWindow", "Enter value of R4"))
        self.label_4.setText(_translate("MainWindow", "Enter value of C1"))
        self.label_16.setText(_translate("MainWindow", "Enter value of C2"))
        self.label_6.setText(_translate("MainWindow", "Enter value of frequency"))
        self.label_5.setText(_translate("MainWindow", "Enter value of voltage"))
    def HandleQuestion(self):
        pic = self.label_8
        pic1=self.label_9
        pic.setPixmap(QtGui.QPixmap("plot11.png"))
        pic1.setPixmap(QtGui.QPixmap("plot12.png"))
        pic.show()
        pic1.show()
class Ui_MainWindow8(object):
    def calculate(self):

        model1 = load_fmu("activelowpass.fmu")
        objTKSolver1 = win32com.client.Dispatch("TKWX.Document")
        objTKSolver1.LoadModel("r", r"C:\Users\HARDIK\UTS_PROJECT\ActiveLowPassFilter.tkwx")

        model2 = load_fmu("activelowpassSecondOrder.fmu")
        objTKSolver2 = win32com.client.Dispatch("TKWX.Document")
        objTKSolver2.LoadModel("r", r"C:\Users\HARDIK\UTS_PROJECT\activelowpassSecondOrder.tkwx")

        R1 = self.lineEdit_2.text()
        R2 = self.lineEdit_9.text()
        R3 = self.lineEdit_8.text()
        R4 = self.lineEdit.text()
        C1 = self.lineEdit_13.text()
        C2 = self.lineEdit_11.text()
        f = self.lineEdit_10.text()
        vin = self.lineEdit_12.text()

        model1.set("R1.R", R1)
        model1.set("R2.R", R2)
        model1.set("R3.R", R3)
        model1.set("C1.C", C1)
        model1.set("sineVoltage.V", vin)
        model1.set("sineVoltage.freqHz", f)

        model2.set("R1.R", R1)
        model2.set("R2.R", R2)
        model2.set("R3.R", R3)
        model2.set("R4.R", R4)
        model2.set("C1.C", C1)
        model2.set("C2.C", C2)
        model2.set("sineVoltage.V", vin)
        model2.set("sineVoltage.freqHz", f)

        res1 = model1.simulate()
        res2 = model2.simulate()

        objTKSolver1.SetValue("R1", "i", R1)
        objTKSolver1.SetValue("C", "i", C1)
        objTKSolver1.SetValue("R2", "i", R2)
        objTKSolver1.SetValue("R3", "i", R3)
        objTKSolver1.SetValue("f", "i", f)
        objTKSolver1.SetValue("vin", "i", vin)
        objTKSolver1.SetValue("vout", "i", max(res1['voltageSensor.v']))
        objTKSolver1.Solve()
        fc1 = objTKSolver1.GetValue("Fc", "o")
        Amax1 = objTKSolver1.GetValue("Amax", "o")
        VoltageGain1 = objTKSolver1.GetValue("VoltageGain", "o")
        voltage_gain1 = objTKSolver1.GetValue("voltagegain", "o")
        gain_in_dB1 = objTKSolver1.GetValue("gain_in_dB", "o")
        self.textBrowser.setText(fc1)
        self.textBrowser_2.setText(Amax1)
        self.textBrowser_3.setText(VoltageGain1)
        self.textBrowser_4.setText(voltage_gain1)
        self.textBrowser_5.setText(gain_in_dB1)
        objTKSolver2.SetValue("R1", "i", R1)
        objTKSolver2.SetValue("R2", "i", R2)
        objTKSolver2.SetValue("R3", "i", R3)
        objTKSolver2.SetValue("R4", "i", R4)
        objTKSolver2.SetValue("C1", "i", C1)
        objTKSolver2.SetValue("C2", "i", C2)
        objTKSolver2.SetValue("f", "i", f)
        objTKSolver2.SetValue("vin", "i", vin)
        objTKSolver2.SetValue("vout", "i", max(res2['voltageSensor.v']))
        objTKSolver2.Solve()
        fc2 = objTKSolver2.GetValue("Fc", "o")
        Av2 = objTKSolver2.GetValue("Av", "o")
        voltage_gain2 = objTKSolver2.GetValue("voltagegain", "o")
        gain_in_dB2 = objTKSolver2.GetValue("gain_in_dB", "o")
        VoltageGain2 = objTKSolver2.GetValue("VoltageGain", "o")
        V=max(res2['voltageSensor.v'])
        self.textBrowser_13.setText(str(V))
        self.textBrowser_14.setText(fc2)
        self.textBrowser_15.setText(Av2)
        self.textBrowser_16.setText(VoltageGain2)
        self.textBrowser_17.setText(voltage_gain2)
        self.textBrowser_18.setText(gain_in_dB2)
        P.figure(figsize=(10, 8))
        P.grid(True)
        P.plot(res1['sineVoltage.v'], 'r', linewidth=1.0, color="mediumvioletred", label='INPUT Voltage')
        P.plot(res1['voltageSensor.v'], 'r', linewidth=1.0, color="limegreen", label='OUTPUT Voltage (FIRST ORDER)')
        P.plot(res2['voltageSensor.v'], 'r', linewidth=1.0, color="orange", label='OUTPUT Voltage (SECOND ORDER)')
        P.title("INPUT OUPUT Voltages")
        P.ylabel('Voltage (V)')
        P.xlabel('Time')
        P.legend()
        P.savefig("plot5.png")

        x1_1 = []
        x11_1 = []
        y1_1 = []
        y11_1 = []
        z1_1 = []
        z11_1 = []

        f1_1 = 1
        f2_1 = int(float(fc1)) * 10
        for i in range(f1_1, f2_1, 1):
            objTKSolver1.SetSubCell("l", 1, i, 1, str(i))
        objTKSolver1.ListSolve()
        index_1 = objTKSolver1.GetObjIndex("p", "P1")
        prop1_1 = objTKSolver1.GetProperty("p", index_1, 1)
        xlist_1 = objTKSolver1.GetSubCell("p", index_1, 1, 1)
        ylist_1 = objTKSolver1.GetSubCell("p", index_1, 1, 2)
        zlist_1 = objTKSolver1.GetSubCell("p", index_1, 2, 1)
        xListIndex_1 = objTKSolver1.GetObjIndex("l", xlist_1)
        yListIndex_1 = objTKSolver1.GetObjIndex("l", ylist_1)
        zListIndex_1 = objTKSolver1.GetObjIndex("l", zlist_1)
        for i in range(1, f2_1):
            x1_1.append(objTKSolver1.GetSubCell("l", xListIndex_1, i, 1))
            x11_1.append(float(x1_1[i - 1]))
        for i in range(1, f2_1):
            y1_1.append(objTKSolver1.GetSubCell("l", yListIndex_1, i, 1))
            y11_1.append(float(y1_1[i - 1]))

        for i in range(1, f2_1):
            z1_1.append(objTKSolver1.GetSubCell("l", zListIndex_1, i, 1))
            z11_1.append(float(z1_1[i - 1]))

        x1_2 = []
        x11_2 = []
        y1_2 = []
        y11_2 = []
        z1_2 = []
        z11_2 = []

        f1_2 = 1
        f2_2 = int(float(fc2)) * 10
        for i in range(f1_2, f2_2, 1):
            objTKSolver2.SetSubCell("l", 1, i, 1, str(i))
        objTKSolver2.ListSolve()
        index_2 = objTKSolver2.GetObjIndex("p", "P1")
        prop1_2 = objTKSolver2.GetProperty("p", index_2, 1)
        xlist_2 = objTKSolver2.GetSubCell("p", index_2, 1, 1)
        ylist_2 = objTKSolver2.GetSubCell("p", index_2, 1, 2)
        zlist_2 = objTKSolver2.GetSubCell("p", index_2, 2, 1)
        xListIndex_2 = objTKSolver2.GetObjIndex("l", xlist_2)
        yListIndex_2 = objTKSolver2.GetObjIndex("l", ylist_2)
        zListIndex_2 = objTKSolver2.GetObjIndex("l", zlist_2)
        for i in range(1, f2_2):
            x1_2.append(objTKSolver2.GetSubCell("l", xListIndex_2, i, 1))
            x11_2.append(float(x1_2[i - 1]))
        for i in range(1, f2_2):
            y1_2.append(objTKSolver2.GetSubCell("l", yListIndex_2, i, 1))
            y11_2.append(float(y1_2[i - 1]))

        for i in range(1, f2_2):
            z1_2.append(objTKSolver2.GetSubCell("l", zListIndex_2, i, 1))
            z11_2.append(float(z1_2[i - 1]))

        P.figure(figsize=(10, 8))
        P.grid(True)
        P.xscale('log')
        P.plot(z11_1, y11_1, linewidth=1.5, color="orange", linestyle='dashed', label='Cut off frequency (FIRST ORDER)')
        P.plot(x11_1, y11_1, linewidth=2.0, color="magenta", label="Voltage Gain in dB (FIRST ORDER)")
        P.plot(z11_2, y11_2, linewidth=1.5, color="blue", linestyle='dashed', label='Cut off frequency (SECOND ORDER)')
        P.plot(x11_2, y11_2, linewidth=2.0, color="limegreen", label="Voltage Gain in dB (SECOND ORDER)")
        P.fill_between(x11_1, y11_1, color='lavenderblush')
        P.fill_between(x11_2, y11_2, color='lavenderblush')
        P.title("VOLTAGE GAIN IN dB VS FREQUENCY")
        P.ylabel('Voltage Gain in dB')
        P.xlabel('Frequency (Hz)')
        P.legend()
        P.savefig("plot6.png")
        conn = sqlite3.connect('mydb.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO Activelowpass (R1,R2,R3,R4,C1,C2,f,vin,fc1,Amax1,voltage_gain1,gain_in_dB1,VoltageGain1,fc2,Av2,voltage_gain2,gain_in_dB2,VoltageGain2) VALUES (?, ?, ?, ?,?, ?, ?, ?,?,?,?,?,?,?,?,?,?,?)",
            (R1, R2, R3, R4, C1, C2, f, vin, fc1, Amax1, voltage_gain1, gain_in_dB1, VoltageGain1, fc2, Av2,
             voltage_gain2, gain_in_dB2, VoltageGain2))

        conn.commit()
        conn.close()

        self.HandleQuestion()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)

        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 312, 160))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 180, 671, 51))
        self.pushButton.setStyleSheet("background-color: rgb(87, 175, 0);\n"
"\n"
"font: 37pt \"MS Sans Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(330, 10, 211, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(720, 250, 471, 241))
        self.label_8.setText("")
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 250, 411, 234))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_14.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(430, 250, 251, 231))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_2.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_4.addWidget(self.textBrowser_2)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_3.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_4.addWidget(self.textBrowser_3)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_4.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.verticalLayout_4.addWidget(self.textBrowser_4)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_5.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_4.addWidget(self.textBrowser_5)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(560, 10, 312, 160))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_4.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_16.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_5.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_6.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(880, 7, 221, 161))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy)
        self.lineEdit_13.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_6.addWidget(self.lineEdit_13)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_6.addWidget(self.lineEdit_11)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_6.addWidget(self.lineEdit_10)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy)
        self.lineEdit_12.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_6.addWidget(self.lineEdit_12)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(430, 520, 251, 231))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_7)
        self.textBrowser_13.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.verticalLayout_9.addWidget(self.textBrowser_13)
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_7)
        self.textBrowser_14.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.verticalLayout_9.addWidget(self.textBrowser_14)
        self.textBrowser_15 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_7)
        self.textBrowser_15.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.verticalLayout_9.addWidget(self.textBrowser_15)
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_7)
        self.textBrowser_16.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.verticalLayout_9.addWidget(self.textBrowser_16)
        self.textBrowser_17 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_7)
        self.textBrowser_17.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.verticalLayout_9.addWidget(self.textBrowser_17)
        self.textBrowser_18 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_7)
        self.textBrowser_18.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.verticalLayout_9.addWidget(self.textBrowser_18)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(10, 520, 411, 234))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_10.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_25.setObjectName("label_25")
        self.verticalLayout_10.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_26.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_26.setObjectName("label_26")
        self.verticalLayout_10.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_27.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_27.setObjectName("label_27")
        self.verticalLayout_10.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_28.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_28.setObjectName("label_28")
        self.verticalLayout_10.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_29.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_29.setObjectName("label_29")
        self.verticalLayout_10.addWidget(self.label_29)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(720, 500, 471, 241))
        self.label_9.setText("")
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 490, 111, 20))
        self.label_7.setObjectName("label_7")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(160, 220, 91, 16))
        self.label_30.setObjectName("label_30")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter value of R1"))
        self.label_2.setText(_translate("MainWindow", "Enter value of R2"))
        self.label_3.setText(_translate("MainWindow", "Enter value of R3"))
        self.label_15.setText(_translate("MainWindow", "Enter value of R4"))
        self.pushButton.setText(_translate("MainWindow", "CALCULATE"))
        self.label_17.setText(_translate("MainWindow", "Cutoff frequency"))
        self.label_11.setText(_translate("MainWindow", "Gain of the pass band"))
        self.label_12.setText(_translate("MainWindow", "Voltage Gain (Amax / √{1+(f/fc)²"))
        self.label_13.setText(_translate("MainWindow", "Voltage Gain (Vout/Vin) "))
        self.label_14.setText(_translate("MainWindow", "The gain in dB is given is 20log (VG)"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Enter value of C1"))
        self.label_16.setText(_translate("MainWindow", "Enter value of C2"))
        self.label_5.setText(_translate("MainWindow", "Enter value of voltage"))
        self.label_6.setText(_translate("MainWindow", "Enter value of frequency"))
        self.textBrowser_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_14.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_15.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_16.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_17.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_18.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "Voltage Output"))
        self.label_25.setText(_translate("MainWindow", "Cutoff frequency"))
        self.label_26.setText(_translate("MainWindow", "Gain of the pass band"))
        self.label_27.setText(_translate("MainWindow", "Voltage Gain (Amax / √{1+(f/fc)²"))
        self.label_28.setText(_translate("MainWindow", "Voltage Gain (Vout/Vin) "))
        self.label_29.setText(_translate("MainWindow", "The gain in dB is given is 20log (VG)"))
        self.label_7.setText(_translate("MainWindow", "SECOND ORDER"))
        self.label_30.setText(_translate("MainWindow", "FIRST ORDER"))
    def HandleQuestion(self):
        pic = self.label_8
        pic1=self.label_9
        pic.setPixmap(QtGui.QPixmap("plot5.png"))
        pic1.setPixmap(QtGui.QPixmap("plot6.png"))
        pic.show()
        pic1.show()
class Ui_MainWindow9(object):
    def calculate(self):

        model1 = load_fmu("activelowpass.fmu")
        objTKSolver1 = win32com.client.Dispatch("TKWX.Document")
        objTKSolver1.LoadModel("r", r"C:\Users\HARDIK\UTS_PROJECT\activehighpass.tkwx")

        model2 = load_fmu("activelowpassSecondOrder.fmu")
        objTKSolver2 = win32com.client.Dispatch("TKWX.Document")
        objTKSolver2.LoadModel("r", r"C:\Users\HARDIK\UTS_PROJECT\activehighpasssecond.tkwx")

        R1 = self.lineEdit_2.text()
        R2 = self.lineEdit_9.text()
        R3 = self.lineEdit_8.text()
        R4 = self.lineEdit.text()
        C1 = self.lineEdit_13.text()
        C2 = self.lineEdit_11.text()
        f = self.lineEdit_10.text()
        vin = self.lineEdit_12.text()

        print("\n  SIMULATING....\n")
        model1.set("R1.R", R1)
        model1.set("R2.R", R2)
        model1.set("R3.R", R3)
        model1.set("C1.C", C1)
        model1.set("sineVoltage.V", vin)
        model1.set("sineVoltage.freqHz", f)

        model2.set("R1.R", R1)
        model2.set("R2.R", R2)
        model2.set("R3.R", R3)
        model2.set("R4.R", R4)
        model2.set("C1.C", C1)
        model2.set("C2.C", C2)
        model2.set("sineVoltage.V", vin)
        model2.set("sineVoltage.freqHz", f)

        res1 = model1.simulate()
        res2 = model2.simulate()

        objTKSolver1.SetValue("R1", "i", R1)
        objTKSolver1.SetValue("C", "i", C1)
        objTKSolver1.SetValue("R2", "i", R2)
        objTKSolver1.SetValue("R3", "i", R3)
        objTKSolver1.SetValue("f", "i", f)
        objTKSolver1.SetValue("vin", "i", vin)
        objTKSolver1.SetValue("vout", "i", max(res1['voltageSensor.v']))
        objTKSolver1.Solve()
        fc1 = objTKSolver1.GetValue("Fc", "o")
        Amax1 = objTKSolver1.GetValue("Amax", "o")
        VoltageGain1 = objTKSolver1.GetValue("VoltageGain", "o")
        voltage_gain1 = objTKSolver1.GetValue("voltagegain", "o")
        gain_in_dB1 = objTKSolver1.GetValue("gain_in_dB", "o")
        self.textBrowser.setText(fc1)
        self.textBrowser_2.setText(Amax1)
        self.textBrowser_3.setText(VoltageGain1)
        self.textBrowser_4.setText(voltage_gain1)
        self.textBrowser_5.setText(gain_in_dB1)
        objTKSolver2.SetValue("R1", "i", R1)
        objTKSolver2.SetValue("R2", "i", R2)
        objTKSolver2.SetValue("R3", "i", R3)
        objTKSolver2.SetValue("R4", "i", R4)
        objTKSolver2.SetValue("C1", "i", C1)
        objTKSolver2.SetValue("C2", "i", C2)
        objTKSolver2.SetValue("f", "i", f)
        objTKSolver2.SetValue("vin", "i", vin)
        objTKSolver2.SetValue("vout", "i", max(res2['voltageSensor.v']))
        objTKSolver2.Solve()
        fc2 = objTKSolver2.GetValue("Fc", "o")
        Av2 = objTKSolver2.GetValue("Av", "o")
        voltage_gain2 = objTKSolver2.GetValue("voltagegain", "o")
        gain_in_dB2 = objTKSolver2.GetValue("gain_in_dB", "o")
        VoltageGain2 = objTKSolver2.GetValue("VoltageGain", "o")
        V=max(res2['voltageSensor.v'])
        self.textBrowser_13.setText(str(V))
        self.textBrowser_14.setText(fc2)
        self.textBrowser_15.setText(Av2)
        self.textBrowser_16.setText(VoltageGain2)
        self.textBrowser_17.setText(voltage_gain2)
        self.textBrowser_18.setText(gain_in_dB2)

        P.figure(figsize=(10, 8))
        P.grid(True)
        P.plot(res1['sineVoltage.v'], 'r', linewidth=1.0, color="mediumvioletred", label='INPUT Voltage')
        P.plot(res1['voltageSensor.v'], 'r', linewidth=1.0, color="limegreen", label='OUTPUT Voltage (FIRST ORDER)')
        P.plot(res2['voltageSensor.v'], 'r', linewidth=1.0, color="orange", label='OUTPUT Voltage (SECOND ORDER)')
        P.title("INPUT OUPUT Voltages")
        P.ylabel('Voltage (V)')
        P.xlabel('Time')
        P.legend()
        P.savefig("plot7.png")

        x1_1 = []
        x11_1 = []
        y1_1 = []
        y11_1 = []
        z1_1 = []
        z11_1 = []

        f1_1 = 1
        f2_1 = int(float(fc1)) * 10
        for i in range(f1_1, f2_1, 1):
            objTKSolver1.SetSubCell("l", 1, i, 1, str(i))
        objTKSolver1.ListSolve()
        index_1 = objTKSolver1.GetObjIndex("p", "P1")
        prop1_1 = objTKSolver1.GetProperty("p", index_1, 1)
        xlist_1 = objTKSolver1.GetSubCell("p", index_1, 1, 1)
        ylist_1 = objTKSolver1.GetSubCell("p", index_1, 1, 2)
        zlist_1 = objTKSolver1.GetSubCell("p", index_1, 2, 1)
        xListIndex_1 = objTKSolver1.GetObjIndex("l", xlist_1)
        yListIndex_1 = objTKSolver1.GetObjIndex("l", ylist_1)
        zListIndex_1 = objTKSolver1.GetObjIndex("l", zlist_1)
        for i in range(1, f2_1):
            x1_1.append(objTKSolver1.GetSubCell("l", xListIndex_1, i, 1))
            x11_1.append(float(x1_1[i - 1]))
        for i in range(1, f2_1):
            y1_1.append(objTKSolver1.GetSubCell("l", yListIndex_1, i, 1))
            y11_1.append(float(y1_1[i - 1]))

        for i in range(1, f2_1):
            z1_1.append(objTKSolver1.GetSubCell("l", zListIndex_1, i, 1))
            z11_1.append(float(z1_1[i - 1]))

        x1_2 = []
        x11_2 = []
        y1_2 = []
        y11_2 = []
        z1_2 = []
        z11_2 = []

        f1_2 = 1
        f2_2 = int(float(fc2)) * 10
        for i in range(f1_2, f2_2, 1):
            objTKSolver2.SetSubCell("l", 1, i, 1, str(i))
        objTKSolver2.ListSolve()
        index_2 = objTKSolver2.GetObjIndex("p", "P1")
        prop1_2 = objTKSolver2.GetProperty("p", index_2, 1)
        xlist_2 = objTKSolver2.GetSubCell("p", index_2, 1, 1)
        ylist_2 = objTKSolver2.GetSubCell("p", index_2, 1, 2)
        zlist_2 = objTKSolver2.GetSubCell("p", index_2, 2, 1)
        xListIndex_2 = objTKSolver2.GetObjIndex("l", xlist_2)
        yListIndex_2 = objTKSolver2.GetObjIndex("l", ylist_2)
        zListIndex_2 = objTKSolver2.GetObjIndex("l", zlist_2)
        for i in range(1, f2_2):
            x1_2.append(objTKSolver2.GetSubCell("l", xListIndex_2, i, 1))
            x11_2.append(float(x1_2[i - 1]))
        for i in range(1, f2_2):
            y1_2.append(objTKSolver2.GetSubCell("l", yListIndex_2, i, 1))
            y11_2.append(float(y1_2[i - 1]))

        for i in range(1, f2_2):
            z1_2.append(objTKSolver2.GetSubCell("l", zListIndex_2, i, 1))
            z11_2.append(float(z1_2[i - 1]))

        P.figure(figsize=(10, 8))
        P.grid(True)
        P.xscale('log')
        P.plot(z11_1, y11_1, linewidth=1.5, color="orange", linestyle='dashed', label='Cut off frequency (FIRST ORDER)')
        P.plot(x11_1, y11_1, linewidth=2.0, color="magenta", label="Voltage Gain in dB (FIRST ORDER)")
        P.plot(z11_2, y11_2, linewidth=1.5, color="blue", linestyle='dashed', label='Cut off frequency (SECOND ORDER)')
        P.plot(x11_2, y11_2, linewidth=2.0, color="limegreen", label="Voltage Gain in dB (SECOND ORDER)")
        P.fill_between(x11_1, y11_1, color='lavenderblush')
        P.fill_between(x11_2, y11_2, color='lavenderblush')
        P.title("VOLTAGE GAIN IN dB VS FREQUENCY")
        P.ylabel('Voltage Gain in dB')
        P.xlabel('Frequency (Hz)')
        P.legend()
        P.savefig("plot8.png")
        conn = sqlite3.connect('mydb.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO Activehighpass (R1,R2,R3,R4,C1,C2,f,vin,fc1,Amax1,voltage_gain1,gain_in_dB1,VoltageGain1,fc2,Av2,voltage_gain2,gain_in_dB2,VoltageGain2) VALUES (?, ?, ?, ?,?, ?, ?, ?,?,?,?,?,?,?,?,?,?,?)",
            (R1, R2, R3, R4, C1, C2, f, vin, fc1, Amax1, voltage_gain1, gain_in_dB1, VoltageGain1, fc2, Av2,
             voltage_gain2, gain_in_dB2, VoltageGain2))

        conn.commit()
        conn.close()

        self.HandleQuestion()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)

        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 312, 160))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 180, 671, 51))
        self.pushButton.setStyleSheet("background-color: rgb(87, 175, 0);\n"
"\n"
"font: 37pt \"MS Sans Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(330, 10, 211, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(720, 250, 471, 241))
        self.label_8.setText("")
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 250, 411, 234))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_14.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(430, 250, 251, 231))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_2.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_4.addWidget(self.textBrowser_2)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_3.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_4.addWidget(self.textBrowser_3)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_4.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.verticalLayout_4.addWidget(self.textBrowser_4)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_5.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_4.addWidget(self.textBrowser_5)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(560, 10, 312, 160))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_4.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_16.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_5.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_6.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(880, 7, 221, 161))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy)
        self.lineEdit_13.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_6.addWidget(self.lineEdit_13)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_6.addWidget(self.lineEdit_11)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_6.addWidget(self.lineEdit_10)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy)
        self.lineEdit_12.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_6.addWidget(self.lineEdit_12)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(430, 520, 251, 231))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_7)
        self.textBrowser_13.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.verticalLayout_9.addWidget(self.textBrowser_13)
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_7)
        self.textBrowser_14.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.verticalLayout_9.addWidget(self.textBrowser_14)
        self.textBrowser_15 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_7)
        self.textBrowser_15.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.verticalLayout_9.addWidget(self.textBrowser_15)
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_7)
        self.textBrowser_16.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.verticalLayout_9.addWidget(self.textBrowser_16)
        self.textBrowser_17 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_7)
        self.textBrowser_17.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.verticalLayout_9.addWidget(self.textBrowser_17)
        self.textBrowser_18 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_7)
        self.textBrowser_18.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.verticalLayout_9.addWidget(self.textBrowser_18)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(10, 520, 411, 234))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_10.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_25.setObjectName("label_25")
        self.verticalLayout_10.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_26.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_26.setObjectName("label_26")
        self.verticalLayout_10.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_27.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_27.setObjectName("label_27")
        self.verticalLayout_10.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_28.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_28.setObjectName("label_28")
        self.verticalLayout_10.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_29.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_29.setObjectName("label_29")
        self.verticalLayout_10.addWidget(self.label_29)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(720, 500, 471, 241))
        self.label_9.setText("")
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 490, 111, 20))
        self.label_7.setObjectName("label_7")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(160, 220, 91, 16))
        self.label_30.setObjectName("label_30")
        self.pushButton.clicked.connect(self.calculate)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter value of R1"))
        self.label_2.setText(_translate("MainWindow", "Enter value of R2"))
        self.label_3.setText(_translate("MainWindow", "Enter value of R3"))
        self.label_15.setText(_translate("MainWindow", "Enter value of R4"))
        self.pushButton.setText(_translate("MainWindow", "CALCULATE"))
        self.label_17.setText(_translate("MainWindow", "Cutoff frequency"))
        self.label_11.setText(_translate("MainWindow", "Gain of the pass band"))
        self.label_12.setText(_translate("MainWindow", "Voltage Gain (Amax / √{1+(f/fc)²"))
        self.label_13.setText(_translate("MainWindow", "Voltage Gain (Vout/Vin) "))
        self.label_14.setText(_translate("MainWindow", "The gain in dB is given is 20log (VG)"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Enter value of C1"))
        self.label_16.setText(_translate("MainWindow", "Enter value of C2"))
        self.label_5.setText(_translate("MainWindow", "Enter value of voltage"))
        self.label_6.setText(_translate("MainWindow", "Enter value of frequency"))
        self.textBrowser_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_14.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_15.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_16.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_17.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_18.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "Voltage Output"))
        self.label_25.setText(_translate("MainWindow", "Cutoff frequency"))
        self.label_26.setText(_translate("MainWindow", "Gain of the pass band"))
        self.label_27.setText(_translate("MainWindow", "Voltage Gain (Amax / √{1+(f/fc)²"))
        self.label_28.setText(_translate("MainWindow", "Voltage Gain (Vout/Vin) "))
        self.label_29.setText(_translate("MainWindow", "The gain in dB is given is 20log (VG)"))
        self.label_7.setText(_translate("MainWindow", "SECOND ORDER"))
        self.label_30.setText(_translate("MainWindow", "FIRST ORDER"))
    def HandleQuestion(self):
        pic = self.label_8
        pic1=self.label_9
        pic.setPixmap(QtGui.QPixmap("plot7.png"))
        pic1.setPixmap(QtGui.QPixmap("plot8.png"))
        pic.show()
        pic1.show()
class Ui_MainWindow10(object):
    def calculate(self):
        objTKSolver = win32com.client.Dispatch("TKWX.Document")
        objTKSolver.LoadModel("r", r"C:\Users\HARDIK\UTS_PROJECT\multiplefeedback.tkwx")

        R1 = self.lineEdit_2.text()
        R2 = self.lineEdit_9.text()
        R3 = self.lineEdit_8.text()
        C1 = self.lineEdit_12.text()
        C2 = self.lineEdit_13.text()
        Fc1 = self.lineEdit_10.text()
        Fc2 = self.lineEdit.text()
        vin = self.lineEdit_3.text()
        objTKSolver.SetValue("R1", "i", R1)
        objTKSolver.SetValue("R2", "i", R2)
        objTKSolver.SetValue("R3", "i", R3)
        objTKSolver.SetValue("C1", "i", C1)
        objTKSolver.SetValue("C2", "i", C2)
        objTKSolver.SetValue("vin", "i", vin)
        objTKSolver.SetValue("Fc1", "i", Fc1)
        objTKSolver.SetValue("Fc2", "i", Fc2)
        objTKSolver.Solve()
        Fo = objTKSolver.GetValue("Fo", "o")
        C = objTKSolver.GetValue("C", "o")
        BW = objTKSolver.GetValue("BW", "o")
        Q = objTKSolver.GetValue("Q", "o")
        self.textBrowser_6.setText(Fo)
        self.textBrowser.setText(BW)
        self.textBrowser_3.setText(Q)
        self.textBrowser_4.setText(C)



        m = float(1)
        n = float(Fo) * 2
        o = float((m + n) / 20)
        f_arr = N.arange(m, n, o)
        vg_arr = []
        gain_in_dB_arr = []

        for i in range(len(f_arr)):
            model = load_fmu("multifeedbackactivebandpass.fmu")
            model.set("r1.R", R1)
            model.set("r2.R", R2)
            model.set("r3.R", R3)
            model.set("c1.C", C1)
            model.set("c2.C", C2)
            model.set("sineVoltage.V", vin)
            model.set("sineVoltage.freqHz", f_arr[i])

            if (f_arr[i] <= float(Fo)):
                res = model.simulate()
                a = max(res['opAmp.out.v'])
                objTKSolver.SetValue("vout", "i", a)
                objTKSolver.Solve()
                voltagegain = objTKSolver.GetValue("voltagegain", "o")
                gain_in_dB = objTKSolver.GetValue("gain_in_dB", "o")
                vg_arr.append(float(voltagegain))
                gain_in_dB_arr.append(float(gain_in_dB))

        vg_arr = vg_arr + vg_arr[::-1]
        gain_in_dB_arr = gain_in_dB_arr + gain_in_dB_arr[::-1]
        f_arr = f_arr[:len(gain_in_dB_arr)]
        index = 1
        for i in f_arr:
            objTKSolver.SetSubCell("l", 1, index, 1, str(i))
            index = index + 1

        index = 1
        for i in gain_in_dB_arr:
            objTKSolver.SetSubCell("l", 2, index, 1, str(i))
            index = index + 1

        P.figure(figsize=(8, 6))
        P.grid(True)
        P.plot(f_arr, gain_in_dB_arr, 'r', linewidth=2.0, color="magenta")
        P.title("Voltage Gain in dB VS Frequency")
        P.ylabel('Voltage gain in dB')
        P.xlabel('Frequency Hz')
        P.savefig("plot19.png")

        index1 = -1
        index2 = -1
        for i in f_arr:
            if (i <= float(Fc1)):
                index1 = index1 + 1
            else:
                break
        for i in f_arr:
            if (i <= float(Fc2)):
                index2 = index2 + 1
            else:
                break

        f_arr = f_arr[index1:index2 + 1]
        gain_in_dB_arr = gain_in_dB_arr[index1:index2 + 1]
        P.figure(figsize=(8, 6))
        P.grid(True)
        P.plot(f_arr, gain_in_dB_arr, 'r', linewidth=2.0, color="orange")
        P.title("Voltage Gain in dB VS Frequency")
        P.ylabel('Voltage gain in dB')
        # P. fill_between(x11, y11, color='lavender')
        P.xlabel('Frequency Hz')
        P.savefig("plot20.png")
        conn = sqlite3.connect('mydb.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO Multifeedback (R1,R2,R3,C1,C2,vin,Fc1,Fc2,Fo,C,BW,Q) VALUES (?, ?, ?, ?,?, ?, ?, ?,?,?,?,?)",
            (R1, R2, R3, C1, C2, vin, Fc1, Fc2, Fo, C, BW, Q))

        conn.commit()
        conn.close()

        self.HandleQuestion()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(600, 0, 251, 231))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(800, 340, 381, 381))
        self.label_9.setText("")
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(870, 0, 341, 231))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_6.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.verticalLayout_4.addWidget(self.textBrowser_6)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_3.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_4.addWidget(self.textBrowser_3)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_4.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.verticalLayout_4.addWidget(self.textBrowser_4)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 340, 351, 391))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../UTS_PROJECT/multiplefeedback.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 312, 324))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(330, 0, 211, 321))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy)
        self.lineEdit_12.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_2.addWidget(self.lineEdit_12)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy)
        self.lineEdit_13.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_2.addWidget(self.lineEdit_13)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_2.addWidget(self.lineEdit_10)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(400, 350, 351, 371))
        self.label_8.setText("")
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 260, 671, 51))
        self.pushButton.setStyleSheet("background-color: rgb(87, 175, 0);\n"
"\n"
"font: 37pt \"MS Sans Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "CUTOFF FREQUENCY"))
        self.label_17.setText(_translate("MainWindow", "BANDWIDTH"))
        self.label_11.setText(_translate("MainWindow", "QUALITY FACTOR"))
        self.label_12.setText(_translate("MainWindow", "CAPACITANCE"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.75pt;\"><br /></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.75pt;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.75pt;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.75pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Enter value of R1"))
        self.label_2.setText(_translate("MainWindow", "Enter value of R2"))
        self.label_3.setText(_translate("MainWindow", "Enter value of R3"))
        self.label_4.setText(_translate("MainWindow", "Enter value of C1"))
        self.label_16.setText(_translate("MainWindow", "Enter value of C2"))
        self.label_6.setText(_translate("MainWindow", "Enter value of FC1"))
        self.label_15.setText(_translate("MainWindow", "Enter value of FC2"))
        self.label_5.setText(_translate("MainWindow", "Enter value of voltage"))
        self.pushButton.setText(_translate("MainWindow", "CALCULATE"))
    def HandleQuestion(self):
        pic = self.label_8
        pic1=self.label_9
        pic.setPixmap(QtGui.QPixmap("plot19.png"))
        pic1.setPixmap(QtGui.QPixmap("plot20.png"))
        pic.show()
        pic1.show()
class Ui_MainWindow11(object):
    def calculate(self):
        objTKSolver = win32com.client.Dispatch("TKWX.Document")
        objTKSolver.LoadModel("r", r"C:\Users\HARDIK\UTS_PROJECT\bandstopfilter.tkwx")
        print("\n\n")

        FL = self.lineEdit_2.text()
        FH = self.lineEdit_9.text()
        R = self.lineEdit_8.text()
        CL = self.lineEdit_12.text()
        CH = self.lineEdit_13.text()
        vin = self.lineEdit_10.text()

        objTKSolver.SetValue("FL", "i", FL)
        objTKSolver.SetValue("FH", "i", FH)
        objTKSolver.SetValue("CL", "i", CL)
        objTKSolver.SetValue("CH", "i", CH)
        objTKSolver.SetValue("vin", "i", vin)
        objTKSolver.Solve()
        RL = objTKSolver.GetValue("RL", "o")
        RH = objTKSolver.GetValue("RH", "o")
        FC = objTKSolver.GetValue("FC", "o")
        Q = objTKSolver.GetValue("Q", "o")
        FBW = objTKSolver.GetValue("FBW", "o")



        self.textBrowser_6.setText(RH)
        self.textBrowser.setText(RL)
        self.textBrowser_3.setText(FC)
        self.textBrowser_5.setText(Q)
        self.textBrowser_4.setText(FBW)

        print("\n\n")
        m = float(1)
        n = float(FC) * 2
        o = float((m + n) / 20)
        f_arr = N.arange(m, n + (4 * o), o)
        vg_arr = []
        gain_in_dB_arr = []

        for i in range(len(f_arr)):
            model = load_fmu("bandstopfilter.fmu")
            model.set("RL.R", RL)
            model.set("RH.R", RH)
            model.set("R1.R", R)
            model.set("R2.R", R)
            model.set("R3.R", R)
            model.set("CL.C", CL)
            model.set("CH.C", CH)
            model.set("sineVoltage.V", vin)
            model.set("sineVoltage.freqHz", f_arr[i])
            if (f_arr[i] <= float(FC)):  # 200 250 300 350 400 450 500 550 600 650 700 750 800
                res = model.simulate()
                a = max(res['voltageSensor.v'])
                objTKSolver.SetValue("vout", "i", a)
                objTKSolver.Solve()
                voltagegain = objTKSolver.GetValue("voltagegain", "o")
                gain_in_dB = objTKSolver.GetValue("gain_in_dB", "o")
                vg_arr.append(float(voltagegain))
                gain_in_dB_arr.append(float(gain_in_dB))

        vg_arr = vg_arr + vg_arr[::-1]
        gain_in_dB_arr = gain_in_dB_arr + gain_in_dB_arr[::-1]
        f_arr = f_arr[:len(gain_in_dB_arr)]
        index = 1
        for i in f_arr:
            objTKSolver.SetSubCell("l", 1, index, 1, str(i))
            index = index + 1

        index = 1
        for i in gain_in_dB_arr:
            objTKSolver.SetSubCell("l", 2, index, 1, str(i))
            index = index + 1

        P.figure(figsize=(8, 6))
        P.grid(True)
        P.plot(f_arr, gain_in_dB_arr, 'r', linewidth=2.0, color="magenta")
        P.title("Voltage Gain in dB VS Frequency")
        P.ylabel('Voltage gain in dB')
        P.xlabel('Frequency Hz')
        P.savefig("plot13.png")

        index1 = -1
        index2 = -1
        for i in f_arr:
            if (i <= float(FL)):
                index1 = index1 + 1
            else:
                break
        for i in f_arr:
            if (i <= float(FH)):
                index2 = index2 + 1
            else:
                break

        f_arr = f_arr[index1:index2 + 1]
        gain_in_dB_arr = gain_in_dB_arr[index1:index2 + 1]
        P.figure(figsize=(8, 6))
        P.grid(True)
        P.plot(f_arr, gain_in_dB_arr, 'r', linewidth=2.0, color="orange")
        P.title("Voltage Gain in dB VS Frequency")
        P.ylabel('Voltage gain in dB')
        # P. fill_between(x11, y11, color='lavender')
        P.xlabel('Frequency Hz')
        P.savefig("plot14.png")
        conn = sqlite3.connect('mydb.db')
        c = conn.cursor()
        c.execute("INSERT INTO Bandstop (FL,FH,R,CL,CH,vin,RL,RH,FC,Q,FBW) VALUES (?, ?, ?, ?,?, ?, ?, ?,?,?,?)",
                  (FL, FH, R, CL, CH, vin, RL, RH, FC, Q, FBW))

        conn.commit()
        conn.close()

        self.HandleQuestion()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)

        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(600, 0, 251, 231))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(850, 330, 381, 381))
        self.label_9.setText("")
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(870, 0, 341, 231))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_6.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.verticalLayout_4.addWidget(self.textBrowser_6)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_3.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_4.addWidget(self.textBrowser_3)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_5.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_4.addWidget(self.textBrowser_5)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_4.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.verticalLayout_4.addWidget(self.textBrowser_4)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 340, 411, 391))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../UTS_PROJECT/Bandstop.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 338, 324))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(360, 0, 211, 321))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy)
        self.lineEdit_12.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_2.addWidget(self.lineEdit_12)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy)
        self.lineEdit_13.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_2.addWidget(self.lineEdit_13)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_2.addWidget(self.lineEdit_10)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(470, 340, 351, 371))
        self.label_8.setText("")
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 250, 621, 51))
        self.pushButton.setStyleSheet("background-color: rgb(87, 175, 0);\n"
"\n"
"font: 37pt \"MS Sans Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "RH"))
        self.label_17.setText(_translate("MainWindow", "RL"))
        self.label_11.setText(_translate("MainWindow", "FC"))
        self.label_12.setText(_translate("MainWindow", "QUALITY FACTOR"))
        self.label_13.setText(_translate("MainWindow", "FBW"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Enter value of FL"))
        self.label_2.setText(_translate("MainWindow", "Enter value of FH"))
        self.label_4.setText(_translate("MainWindow", "Enter value of R"))
        self.label_16.setText(_translate("MainWindow", "Enter value of CL"))
        self.label_3.setText(_translate("MainWindow", "Enter value of CH"))
        self.label_6.setText(_translate("MainWindow", "Enter value of Voltage"))
        self.pushButton.setText(_translate("MainWindow", "CALCULATE"))
    def HandleQuestion(self):
        pic = self.label_8
        pic1=self.label_9
        pic.setPixmap(QtGui.QPixmap("plot13.png"))
        pic1.setPixmap(QtGui.QPixmap("plot14.png"))
        pic.show()
        pic1.show()
class Ui_MainWindow12(object):
    def calculate(self):
        model = load_fmu("RLCSERIES.fmu")
        objTKSolver = win32com.client.Dispatch("TKWX.Document")
        objTKSolver.LoadModel("r", r"C:\Users\HARDIK\UTS_PROJECT\RLCSERIES.tkwx")

        R = self.lineEdit_2.text()
        L = self.lineEdit_9.text()
        C = self.lineEdit_8.text()
        f= self.lineEdit_11.text()
        V = self.lineEdit_10.text()
        print("\n\n")

        objTKSolver.SetValue("R", "i", R)
        objTKSolver.SetValue("L", "i", L)
        objTKSolver.SetValue("C", "i", C)
        objTKSolver.SetValue("f", "i", f)
        objTKSolver.SetValue("Vs", "i", V)

        objTKSolver.Solve()

        XL = objTKSolver.GetValue("XL", "o")
        XC = objTKSolver.GetValue("XC", "o")
        Z = objTKSolver.GetValue("Z", "o")
        I = objTKSolver.GetValue("I", "o")
        Vr = objTKSolver.GetValue("Vr", "o")
        Vl = objTKSolver.GetValue("Vl", "o")
        Vc = objTKSolver.GetValue("Vc", "o")
        phi = objTKSolver.GetValue("Φ", "o")
        Fr = objTKSolver.GetValue("Fr", "o")

        self.textBrowser_2.setText(XL)
        self.textBrowser_6.setText(XC)
        self.textBrowser.setText(Z)
        self.textBrowser_7.setText(I)
        self.textBrowser_8.setText(Vr)
        self.textBrowser_3.setText(Vl)
        self.textBrowser_9.setText(Vc)
        self.textBrowser_4.setText(phi)
        self.textBrowser_5.setText(Fr)



        model.set("resistor.R", R)
        model.set("inductor.L", L)
        model.set("capacitor.C", C)
        model.set("sineVoltage.V", V)
        model.set("sineVoltage.freqHz", f)

        res = model.simulate()

        r = model.get("resistor.R")
        l = model.get("inductor.L")
        c = model.get("capacitor.C")
        v = model.get("sineVoltage.V")
        fr = model.get("sineVoltage.freqHz")

        r_res = res['resistor.R']
        l_res = res['inductor.L']
        c_res = res["capacitor.C"]
        v_res = res["sineVoltage.V"]
        f_res = res["sineVoltage.freqHz"]
        i_res = res['currentSensor.i']


        fig = P.figure(figsize=(6, 6))
        P.subplot(2, 1, 1)
        P.grid(True)
        P.plot(i_res, 'r', linewidth=1.0, color="mediumvioletred")
        P.title("Current ")
        P.ylabel('Current (A)')
        P.xlabel('Time (s)')
        P.savefig("plot17.png")

        P.subplot(2, 1, 2)
        P.plot(l_res, linewidth=1.0, marker='o', color="aqua")
        P.title("Inductor ")
        P.grid(True)
        P.ylabel('Inductor (farad)')
        P.xlabel('Time (s)')


        f1 = 1
        f2 = float(Fr) * 2
        arr = N.arange(f1, f2, 1.0)
        F = []
        F1 = []
        F2 = []
        for i in arr:
            objTKSolver.SetValue("f", "i", str(i))
            objTKSolver.Solve()
            a = objTKSolver.GetValue("XL", "o")
            b = objTKSolver.GetValue("XC", "o")
            c = objTKSolver.GetValue("Z", "o")
            F.append(float(a))
            F1.append(float(b))
            F2.append(float(c))
        P.figure(figsize=(8, 6))
        P.grid(True)
        P.plot(arr, F, linewidth=1.0, color="lightgreen", marker='o', label='XL')
        P.plot(arr, F1, linewidth=1.0, color="orange", marker='o', label='XC')
        P.plot(arr, F2, linewidth=1.0, color="magenta", marker='o', label='Z')
        P.title("Series Resonance Frequency")
        P.ylabel('Reactance in ohms')
        P.xlabel('frequency (Hz)')
        P.legend()
        P.yscale('log')
        P.savefig("plot18.png")
        conn = sqlite3.connect('mydb.db')
        c = conn.cursor()
        c.execute("INSERT INTO series (R,L,C,f,V,XL,XC,Z,I,Vr,Vl,Vc,phi,Fr) VALUES (?, ?, ?, ?,?, ?, ?, ?,?,?,?,?,?,?)",
                  (R, L, C, f, V, XL, XC, Z, I, Vr, Vl, Vc, phi, Fr))

        conn.commit()
        conn.close()
        self.HandleQuestion()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)

        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 350, 351, 91))
        self.pushButton.setStyleSheet("background-color: rgb(87, 175, 0);\n"
"\n"
"font: 37pt \"MS Sans Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(830, 360, 381, 371))
        self.label_9.setText("")
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(570, 10, 301, 321))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_14.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_19.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_3.addWidget(self.label_19)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_18.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_3.addWidget(self.label_18)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_16.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 460, 351, 281))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../UTS_PROJECT/rlcseries.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(350, 10, 211, 321))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_2.addWidget(self.lineEdit_11)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_2.addWidget(self.lineEdit_10)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(440, 360, 351, 371))
        self.label_8.setText("")
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(910, 10, 251, 321))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_2.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_4.addWidget(self.textBrowser_2)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_6.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.verticalLayout_4.addWidget(self.textBrowser_6)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_7.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.verticalLayout_4.addWidget(self.textBrowser_7)
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_8.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.verticalLayout_4.addWidget(self.textBrowser_8)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_3.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_4.addWidget(self.textBrowser_3)
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_9.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.verticalLayout_4.addWidget(self.textBrowser_9)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_4.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.verticalLayout_4.addWidget(self.textBrowser_4)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_5.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_4.addWidget(self.textBrowser_5)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 330, 324))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "CALCULATE"))
        self.label_10.setText(_translate("MainWindow", "INDUCTIVE REACTANCE"))
        self.label_17.setText(_translate("MainWindow", "CAPACITIVE REACTANCE"))
        self.label_11.setText(_translate("MainWindow", "IMPEDANCE"))
        self.label_12.setText(_translate("MainWindow", "CURRENT"))
        self.label_13.setText(_translate("MainWindow", "VOLTAGE ACROSS R"))
        self.label_14.setText(_translate("MainWindow", "VOLTAGE ACROSS L"))
        self.label_19.setText(_translate("MainWindow", "VOLTAGE ACROSS C"))
        self.label_18.setText(_translate("MainWindow", "PHASE ANGLE"))
        self.label_16.setText(_translate("MainWindow", "RESONANT FREQUENCY"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Value of RESISTOR"))
        self.label_2.setText(_translate("MainWindow", "Value of INDUCTOR"))
        self.label_3.setText(_translate("MainWindow", "Value of CAPACITOR"))
        self.label_15.setText(_translate("MainWindow", "Value of FREQUENCY"))
        self.label_5.setText(_translate("MainWindow", "Value of VOLTAGE"))
    def HandleQuestion(self):
        pic = self.label_8
        pic1=self.label_9
        pic.setPixmap(QtGui.QPixmap("plot17.png"))
        pic1.setPixmap(QtGui.QPixmap("plot18.png"))
        pic.show()
        pic1.show()

class Ui_MainWindow13(object):
    def calculate(self):
        model = load_fmu("RLCPARALLEL.fmu")
        objTKSolver = win32com.client.Dispatch("TKWX.Document")
        objTKSolver.LoadModel("r", r"C:\Users\HARDIK\UTS_PROJECT\RLCPARALLEL.tkwx")

        R = self.lineEdit_2.text()
        L = self.lineEdit_9.text()
        C = self.lineEdit_8.text()
        f= self.lineEdit_11.text()
        V = self.lineEdit_10.text()

        objTKSolver.SetValue("R", "i", R)
        objTKSolver.SetValue("L", "i", L)
        objTKSolver.SetValue("C", "i", C)
        objTKSolver.SetValue("f", "i", f)
        objTKSolver.SetValue("V", "i", V)

        objTKSolver.Solve()

        XL = objTKSolver.GetValue("XL", "o")
        XC = objTKSolver.GetValue("XC", "o")
        Z = objTKSolver.GetValue("Z", "o")
        IR = objTKSolver.GetValue("IR", "o")
        IL = objTKSolver.GetValue("IL", "o")
        IC = objTKSolver.GetValue("IC", "o")
        IS = objTKSolver.GetValue("IS", "o")
        G = objTKSolver.GetValue("G", "o")
        BC = objTKSolver.GetValue("BC", "o")
        Y = objTKSolver.GetValue("Y", "o")
        phi = objTKSolver.GetValue("phi", "o")
        Fr = objTKSolver.GetValue("Fr", "o")


        self.textBrowser_2.setText(XL)
        self.textBrowser_6.setText(XC)
        self.textBrowser.setText(Z)
        self.textBrowser_7.setText(IR)
        self.textBrowser_10.setText(IL)
        self.textBrowser_11.setText(IC)
        self.textBrowser_8.setText(G)
        self.textBrowser_3.setText(BC)
        self.textBrowser_9.setText(Y)
        self.textBrowser_4.setText(phi)
        self.textBrowser_5.setText(Fr)


        model.set("resistor.R", R)
        model.set("inductor.L", L)
        model.set("capacitor.C", C)
        model.set("sineVoltage.V", V)
        model.set("sineVoltage.freqHz", f)

        res = model.simulate()

        r = model.get("resistor.R")
        l = model.get("inductor.L")
        c = model.get("capacitor.C")
        v = model.get("sineVoltage.V")
        fr = model.get("sineVoltage.freqHz")

        r_res = res['resistor.R']
        l_res = res['inductor.L']
        c_res = res["capacitor.C"]
        v_res = res["sineVoltage.V"]
        f_res = res["sineVoltage.freqHz"]
        i_res = res['currentSensor.i']


        fig = P.figure(figsize=(6, 6))
        P.subplot(2, 1, 1)
        P.plot(i_res, 'r', linewidth=1.0, color="mediumvioletred")
        P.title("Current ")
        P.grid(True)
        P.ylabel('Current (A)')
        P.xlabel('Time (s)')
        P.savefig("plot15.png")


        f1 = 1
        f2 = float(Fr) * 2
        arr = N.arange(f1, f2, 1.0)
        F = []
        F1 = []
        F2 = []
        for i in arr:
            objTKSolver.SetValue("f", "i", str(i))
            objTKSolver.Solve()
            a = objTKSolver.GetValue("XL", "o")
            b = objTKSolver.GetValue("XC", "o")
            c = objTKSolver.GetValue("Z", "o")
            F.append(float(a))
            F1.append(float(b))
            F2.append(float(c))
        P.figure(figsize=(8, 6))
        P.grid(True)
        P.plot(arr, F, linewidth=1.0, color="lightgreen", marker='o', label='XL')
        P.plot(arr, F1, linewidth=1.0, color="orange", marker='o', label='XC')
        P.plot(arr, F2, linewidth=1.0, color="magenta", marker='o', label='Z')
        P.title("Resonance Frequency")
        P.ylabel('Reactance in ohms')
        P.xlabel('Frequency (Hz)')
        P.legend()
        P.yscale('log')
        P.savefig("plot16.png")
        conn = sqlite3.connect('mydb.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO parallel (R,L,C,f,V,XL,XC,Z,IR,IL,IC,G,BC,Y,phi,Fr) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (R, L, C, f, V, XL, XC, Z, IR, IL, IC, G, BC, Y, phi, Fr))

        conn.commit()
        conn.close()
        self.HandleQuestion()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)

        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 380, 291, 61))
        self.pushButton.setStyleSheet("background-color: rgb(87, 175, 0);\n"
"\n"
"font: 37pt \"MS Sans Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(830, 400, 391, 331))
        self.label_9.setText("")
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(570, 10, 301, 361))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_14.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_19.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_3.addWidget(self.label_19)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_18.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_3.addWidget(self.label_18)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_16.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_21.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_3.addWidget(self.label_21)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_20.setStyleSheet("font: 19pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_20.setObjectName("label_20")
        self.verticalLayout_3.addWidget(self.label_20)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 460, 351, 281))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../UTS_PROJECT/rlcparallel.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(350, 10, 211, 361))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_2.addWidget(self.lineEdit_11)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setStyleSheet("background-color:rgb(219, 252, 255); ")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_2.addWidget(self.lineEdit_10)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(400, 400, 391, 331))
        self.label_8.setText("")
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(900, 10, 301, 361))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_2.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_4.addWidget(self.textBrowser_2)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_6.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.verticalLayout_4.addWidget(self.textBrowser_6)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_7.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.verticalLayout_4.addWidget(self.textBrowser_7)
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_10.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.verticalLayout_4.addWidget(self.textBrowser_10)
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_11.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.verticalLayout_4.addWidget(self.textBrowser_11)
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_8.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.verticalLayout_4.addWidget(self.textBrowser_8)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_3.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_4.addWidget(self.textBrowser_3)
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_9.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.verticalLayout_4.addWidget(self.textBrowser_9)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_4.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.verticalLayout_4.addWidget(self.textBrowser_4)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_5.setStyleSheet("background-color: rgb(114, 255, 251);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_4.addWidget(self.textBrowser_5)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 330, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(19, 50, 255);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "CALCULATE"))
        self.label_10.setText(_translate("MainWindow", "INDUCTIVE REACTANCE"))
        self.label_17.setText(_translate("MainWindow", "CAPACITIVE REACTANCE"))
        self.label_11.setText(_translate("MainWindow", "IMPEDANCE"))
        self.label_12.setText(_translate("MainWindow", "TOTAL CURRENT"))
        self.label_13.setText(_translate("MainWindow", "CURRENT ACROSS R"))
        self.label_14.setText(_translate("MainWindow", "CURRENT ACROSS L"))
        self.label_19.setText(_translate("MainWindow", "CURRENT ACROSS C"))
        self.label_18.setText(_translate("MainWindow", "CONDUCTANCE"))
        self.label_16.setText(_translate("MainWindow", "CAPACITIVE ADMITTANCE"))
        self.label_21.setText(_translate("MainWindow", "PHASE ANGLE"))
        self.label_20.setText(_translate("MainWindow", "RESONANT FREQUENCY"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Value of RESISTOR"))
        self.label_2.setText(_translate("MainWindow", "Value of INDUCTOR"))
        self.label_3.setText(_translate("MainWindow", "Value of CAPACITOR"))
        self.label_15.setText(_translate("MainWindow", "Value of FREQUENCY"))
        self.label_5.setText(_translate("MainWindow", "Value of VOLTAGE"))
    def HandleQuestion(self):
        pic = self.label_8
        pic1=self.label_9
        pic.setPixmap(QtGui.QPixmap("plot15.png"))
        pic1.setPixmap(QtGui.QPixmap("plot16.png"))
        pic.show()
        pic1.show()
class Ui_MainWindow20(object):
    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow14()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def load(self):
        connection=sqlite3.connect('mydb.db')
        query="SELECT * FROM Activelowpass1"
        result=connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
        connection.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1261, 681))
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(830, 700, 201, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 700, 201, 51))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.load)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "BACK"))
        self.pushButton_3.setText(_translate("MainWindow", "LOAD"))
class Ui_MainWindow23(object):
    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow14()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def load(self):
        connection=sqlite3.connect('mydb.db')
        query="SELECT * FROM Activehighpass1"
        result=connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
        connection.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1261, 681))
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(830, 700, 201, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 700, 201, 51))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.load)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "BACK"))
        self.pushButton_3.setText(_translate("MainWindow", "LOAD"))
class Ui_MainWindow21(object):
    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow14()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def load(self):
        connection=sqlite3.connect('mydb.db')
        query="SELECT * FROM Activelowpass2"
        result=connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
        connection.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1291, 671))
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 690, 211, 61))
        self.pushButton.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.load)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 690, 211, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.back)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "LOAD"))
        self.pushButton_2.setText(_translate("MainWindow", "BACK"))
class Ui_MainWindow24(object):
    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow14()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def load(self):
        connection=sqlite3.connect('mydb.db')
        query="SELECT * FROM Activehighpass2"
        result=connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
        connection.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1291, 671))
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 690, 211, 61))
        self.pushButton.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.load)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 690, 211, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.back)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "LOAD"))
        self.pushButton_2.setText(_translate("MainWindow", "BACK"))

class Ui_MainWindow22(object):
    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow14()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def load(self):
        connection=sqlite3.connect('mydb.db')
        query="SELECT * FROM Activelowpass"
        result=connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
        connection.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1281, 701))
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(18)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 710, 221, 41))
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.load)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 710, 221, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.back)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "LOAD"))
        self.pushButton_2.setText(_translate("MainWindow", "BACK"))
class Ui_MainWindow25(object):
    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow14()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def load(self):
        connection=sqlite3.connect('mydb.db')
        query="SELECT * FROM Activehighpass"
        result=connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
        connection.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1281, 701))
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(18)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 710, 221, 41))
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.load)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 710, 221, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.back)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "LOAD"))
        self.pushButton_2.setText(_translate("MainWindow", "BACK"))
class Ui_MainWindow14(object):
    def openwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow20()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def openwindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow21()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def openwindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow22()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def openwindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow23()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def openwindow4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow24()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def openwindow5(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow25()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def openwindow6(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow26()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def openwindow7(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow27()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def openwindow8(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow28()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def openwindow9(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow29()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()









    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 450, 1191, 141))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_13 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("background-color: rgb(88, 242, 255);\n"
                                         "font: 20pt \"MV Boli\";\n"
                                         "")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.openwindow6)
        self.horizontalLayout_3.addWidget(self.pushButton_13)
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("background-color: rgb(88, 242, 255);\n"
                                         "font: 20pt \"MV Boli\";\n"
                                         "")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.pushButton_10.clicked.connect(self.openwindow7)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 120, 1191, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setMouseTracking(True)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_6.setStyleSheet("background-color: rgb(76, 124, 255);\n"
                                        "font: 22pt \"MV Boli\";\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.openwindow)
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("background-color: rgb(76, 124, 255);\n"
                                        "\n"
                                        "font: 22pt \"MV Boli\";\n"
                                        "")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.openwindow1)
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_11 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("background-color: rgb(76, 124, 255);\n"
                                         "font: 22pt \"MV Boli\";\n"
                                         "")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.openwindow2)
        self.horizontalLayout.addWidget(self.pushButton_11)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(40, 610, 1191, 131))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_14 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setStyleSheet("background-color: rgb(238, 255, 254);\n"
                                         "font: 22pt \"MV Boli\";")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(self.openwindow8)
        self.horizontalLayout_4.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setStyleSheet("font: 22pt \"MV Boli\";\n"
                                         "background-color: rgb(238, 255, 254);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(self.openwindow9)
        self.horizontalLayout_4.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet("background-color: rgb(88, 242, 255);\n"
                                         "background-color: rgb(255, 0, 0);\n"
                                         "font: 20pt \"MV Boli\";\n"
                                         "")
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_4.addWidget(self.pushButton_16)
        self.pushButton_16.clicked.connect(self.back)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 270, 1193, 161))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("background-color: rgb(201, 255, 156);\n"
                                        "font: 22pt \"MV Boli\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.openwindow3)
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("background-color: rgb(201, 255, 156);\n"
                                        "\n"
                                        "font: 22pt \"MV Boli\";\n"
                                        "\n"
                                        "")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.openwindow4)
        self.horizontalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("background-color: rgb(201, 255, 156);\n"
                                         "font: 22pt \"MV Boli\";\n"
                                         "")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.openwindow5)
        self.horizontalLayout_2.addWidget(self.pushButton_12)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 10, 481, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_13.setText(_translate("MainWindow", "ACTIVE BAND PASS FILTER "))
        self.pushButton_10.setText(_translate("MainWindow", " ACTIVE BAND STOP FILTER"))
        self.pushButton_6.setText(_translate("MainWindow", "ACTIVE LOW PASS FILTER\n"
                                                           " (FIRST ORDER)"))
        self.pushButton_7.setText(_translate("MainWindow", "ACTIVE LOW PASS FILTER \n"
                                                           "(SECOND ORDER)"))
        self.pushButton_11.setText(_translate("MainWindow", "ACTIVE LOW PASS FILTER \n"
                                                            "(COMBINED)"))
        self.pushButton_14.setText(_translate("MainWindow", "RLCSERIES"))
        self.pushButton_15.setText(_translate("MainWindow", "RLCPARALLEL"))
        self.pushButton_16.setText(_translate("MainWindow", "BACK"))
        self.pushButton_8.setText(_translate("MainWindow", "ACTIVE HIGH PASS FILTER \n"
                                                           "(FIRST ORDER)"))
        self.pushButton_9.setText(_translate("MainWindow", "ACTIVE HIGH PASS FILTER\n"
                                                           " (SECOND ORDER)"))
        self.pushButton_12.setText(_translate("MainWindow", "ACTIVE HIGH PASS FILTER \n"
                                                            "(COMBINED)"))
        self.label.setText(_translate("MainWindow", "DATABASE"))
class Ui_MainWindow26(object):
    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow14()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def load(self):
        connection=sqlite3.connect('mydb.db')
        query="SELECT * FROM Multifeedback"
        result=connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
        connection.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1281, 681))
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 700, 141, 41))
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.load)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 700, 141, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.back)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "LOAD"))
        self.pushButton_2.setText(_translate("MainWindow", "BACK"))
class Ui_MainWindow27(object):
    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow14()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def load(self):
        connection=sqlite3.connect('mydb.db')
        query="SELECT * FROM Bandstop"
        result=connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
        connection.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1261, 681))
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(830, 700, 201, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 700, 201, 51))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.load)
        self.pushButton_2.clicked.connect(self.back)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "BACK"))
        self.pushButton_3.setText(_translate("MainWindow", "LOAD"))
class Ui_MainWindow28(object):
    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow14()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def load(self):
        connection=sqlite3.connect('mydb.db')
        query="SELECT * FROM series"
        result=connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
        connection.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1281, 681))
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 690, 211, 61))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.load)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 690, 211, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.back)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "LOAD"))
        self.pushButton_2.setText(_translate("MainWindow", "BACK"))
class Ui_MainWindow29(object):
    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow14()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def load(self):
        connection = sqlite3.connect('mydb.db')
        query = "SELECT * FROM parallel"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1284, 800)
        MainWindow.move(300,100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1281, 671))
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(16)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 700, 141, 51))
        self.pushButton.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.load)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 700, 141, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.back)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "LOAD"))
        self.pushButton_2.setText(_translate("MainWindow", "BACK"))

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Background, QtCore.Qt.gray)
    MainWindow.setPalette(palette)
    MainWindow.showMaximized()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
