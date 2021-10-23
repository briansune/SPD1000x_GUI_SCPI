# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/spd1000x_gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_oMainWind(object):
    def setupUi(self, oMainWind):
        oMainWind.setObjectName("oMainWind")
        oMainWind.resize(492, 592)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/spd_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        oMainWind.setWindowIcon(icon)
        oMainWind.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(oMainWind)
        self.centralwidget.setObjectName("centralwidget")
        self.oLcdVoltageMea = QtWidgets.QLCDNumber(self.centralwidget)
        self.oLcdVoltageMea.setGeometry(QtCore.QRect(10, 10, 271, 161))
        self.oLcdVoltageMea.setSmallDecimalPoint(False)
        self.oLcdVoltageMea.setDigitCount(5)
        self.oLcdVoltageMea.setObjectName("oLcdVoltageMea")
        self.oLcdVoltIn0 = QtWidgets.QLCDNumber(self.centralwidget)
        self.oLcdVoltIn0.setGeometry(QtCore.QRect(20, 460, 31, 51))
        self.oLcdVoltIn0.setSmallDecimalPoint(False)
        self.oLcdVoltIn0.setDigitCount(1)
        self.oLcdVoltIn0.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.oLcdVoltIn0.setObjectName("oLcdVoltIn0")
        self.oDialCurr = QtWidgets.QDial(self.centralwidget)
        self.oDialCurr.setGeometry(QtCore.QRect(220, 350, 111, 111))
        self.oDialCurr.setMaximum(9)
        self.oDialCurr.setSingleStep(1)
        self.oDialCurr.setPageStep(1)
        self.oDialCurr.setInvertedAppearance(False)
        self.oDialCurr.setInvertedControls(False)
        self.oDialCurr.setWrapping(False)
        self.oDialCurr.setNotchTarget(5.0)
        self.oDialCurr.setNotchesVisible(True)
        self.oDialCurr.setObjectName("oDialCurr")
        self.oLabCon = QtWidgets.QLabel(self.centralwidget)
        self.oLabCon.setGeometry(QtCore.QRect(390, 0, 51, 51))
        self.oLabCon.setMaximumSize(QtCore.QSize(90, 90))
        self.oLabCon.setText("")
        self.oLabCon.setPixmap(QtGui.QPixmap(":/image/red.png"))
        self.oLabCon.setScaledContents(True)
        self.oLabCon.setObjectName("oLabCon")
        self.oLcdCurrentMea = QtWidgets.QLCDNumber(self.centralwidget)
        self.oLcdCurrentMea.setGeometry(QtCore.QRect(10, 180, 271, 161))
        self.oLcdCurrentMea.setSmallDecimalPoint(False)
        self.oLcdCurrentMea.setDigitCount(5)
        self.oLcdCurrentMea.setObjectName("oLcdCurrentMea")
        self.oButConnect = QtWidgets.QPushButton(self.centralwidget)
        self.oButConnect.setGeometry(QtCore.QRect(350, 90, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.oButConnect.setFont(font)
        self.oButConnect.setObjectName("oButConnect")
        self.oDialVolt = QtWidgets.QDial(self.centralwidget)
        self.oDialVolt.setGeometry(QtCore.QRect(40, 350, 111, 111))
        self.oDialVolt.setAcceptDrops(False)
        self.oDialVolt.setMaximum(9)
        self.oDialVolt.setPageStep(1)
        self.oDialVolt.setTracking(True)
        self.oDialVolt.setWrapping(False)
        self.oDialVolt.setNotchTarget(5.0)
        self.oDialVolt.setNotchesVisible(True)
        self.oDialVolt.setObjectName("oDialVolt")
        self.oLcdVoltIn1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.oLcdVoltIn1.setGeometry(QtCore.QRect(50, 460, 31, 51))
        self.oLcdVoltIn1.setSmallDecimalPoint(False)
        self.oLcdVoltIn1.setDigitCount(1)
        self.oLcdVoltIn1.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.oLcdVoltIn1.setObjectName("oLcdVoltIn1")
        self.oLcdVoltIn2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.oLcdVoltIn2.setGeometry(QtCore.QRect(100, 460, 31, 51))
        self.oLcdVoltIn2.setSmallDecimalPoint(False)
        self.oLcdVoltIn2.setDigitCount(1)
        self.oLcdVoltIn2.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.oLcdVoltIn2.setObjectName("oLcdVoltIn2")
        self.oLcdVoltIn3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.oLcdVoltIn3.setGeometry(QtCore.QRect(130, 460, 31, 51))
        self.oLcdVoltIn3.setSmallDecimalPoint(False)
        self.oLcdVoltIn3.setDigitCount(1)
        self.oLcdVoltIn3.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.oLcdVoltIn3.setObjectName("oLcdVoltIn3")
        self.oLcdCurrIn2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.oLcdCurrIn2.setGeometry(QtCore.QRect(290, 460, 31, 51))
        self.oLcdCurrIn2.setSmallDecimalPoint(False)
        self.oLcdCurrIn2.setDigitCount(1)
        self.oLcdCurrIn2.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.oLcdCurrIn2.setObjectName("oLcdCurrIn2")
        self.oLcdCurrIn0 = QtWidgets.QLCDNumber(self.centralwidget)
        self.oLcdCurrIn0.setGeometry(QtCore.QRect(210, 460, 31, 51))
        self.oLcdCurrIn0.setSmallDecimalPoint(False)
        self.oLcdCurrIn0.setDigitCount(1)
        self.oLcdCurrIn0.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.oLcdCurrIn0.setObjectName("oLcdCurrIn0")
        self.oLcdCurrIn1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.oLcdCurrIn1.setGeometry(QtCore.QRect(240, 460, 31, 51))
        self.oLcdCurrIn1.setSmallDecimalPoint(False)
        self.oLcdCurrIn1.setDigitCount(1)
        self.oLcdCurrIn1.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.oLcdCurrIn1.setObjectName("oLcdCurrIn1")
        self.oButVoltSel = QtWidgets.QPushButton(self.centralwidget)
        self.oButVoltSel.setGeometry(QtCore.QRect(80, 389, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.oButVoltSel.setFont(font)
        self.oButVoltSel.setStyleSheet("border: 2px solid black;\n"
"background-color: rgb(211, 211, 211);\n"
"border-radius: 15px;")
        self.oButVoltSel.setObjectName("oButVoltSel")
        self.oButCurrSel = QtWidgets.QPushButton(self.centralwidget)
        self.oButCurrSel.setGeometry(QtCore.QRect(260, 389, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.oButCurrSel.setFont(font)
        self.oButCurrSel.setStyleSheet("border: 2px solid black;\n"
"background-color: rgb(211, 211, 211);\n"
"border-radius: 15px;")
        self.oButCurrSel.setDefault(False)
        self.oButCurrSel.setObjectName("oButCurrSel")
        self.oGrpBut = QtWidgets.QGroupBox(self.centralwidget)
        self.oGrpBut.setGeometry(QtCore.QRect(350, 260, 131, 71))
        self.oGrpBut.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border: 0px")
        self.oGrpBut.setTitle("")
        self.oGrpBut.setAlignment(QtCore.Qt.AlignCenter)
        self.oGrpBut.setFlat(False)
        self.oGrpBut.setObjectName("oGrpBut")
        self.oRbutUsb = QtWidgets.QRadioButton(self.oGrpBut)
        self.oRbutUsb.setGeometry(QtCore.QRect(10, 40, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.oRbutUsb.setFont(font)
        self.oRbutUsb.setObjectName("oRbutUsb")
        self.oRbutEthernet = QtWidgets.QRadioButton(self.oGrpBut)
        self.oRbutEthernet.setGeometry(QtCore.QRect(10, 10, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.oRbutEthernet.setFont(font)
        self.oRbutEthernet.setCheckable(True)
        self.oRbutEthernet.setChecked(False)
        self.oRbutEthernet.setObjectName("oRbutEthernet")
        self.oGrpBut2 = QtWidgets.QGroupBox(self.centralwidget)
        self.oGrpBut2.setGeometry(QtCore.QRect(350, 370, 131, 71))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.oGrpBut2.setFont(font)
        self.oGrpBut2.setAutoFillBackground(False)
        self.oGrpBut2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border: 0px")
        self.oGrpBut2.setTitle("")
        self.oGrpBut2.setFlat(False)
        self.oGrpBut2.setObjectName("oGrpBut2")
        self.oRbut4Wire = QtWidgets.QRadioButton(self.oGrpBut2)
        self.oRbut4Wire.setGeometry(QtCore.QRect(10, 40, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.oRbut4Wire.setFont(font)
        self.oRbut4Wire.setObjectName("oRbut4Wire")
        self.oRbut2Wire = QtWidgets.QRadioButton(self.oGrpBut2)
        self.oRbut2Wire.setGeometry(QtCore.QRect(10, 10, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.oRbut2Wire.setFont(font)
        self.oRbut2Wire.setCheckable(True)
        self.oRbut2Wire.setChecked(False)
        self.oRbut2Wire.setObjectName("oRbut2Wire")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 520, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(296, 12, 31, 161))
        font = QtGui.QFont()
        font.setPointSize(34)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 180, 31, 161))
        font = QtGui.QFont()
        font.setPointSize(34)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 460, 16, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 460, 16, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.oLabLock = QtWidgets.QLabel(self.centralwidget)
        self.oLabLock.setGeometry(QtCore.QRect(380, 470, 51, 41))
        self.oLabLock.setMaximumSize(QtCore.QSize(90, 90))
        self.oLabLock.setText("")
        self.oLabLock.setPixmap(QtGui.QPixmap(":/image/unlock.png"))
        self.oLabLock.setScaledContents(True)
        self.oLabLock.setObjectName("oLabLock")
        self.oButLock = QtWidgets.QPushButton(self.centralwidget)
        self.oButLock.setGeometry(QtCore.QRect(350, 330, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.oButLock.setFont(font)
        self.oButLock.setObjectName("oButLock")
        self.oButPwr = QtWidgets.QPushButton(self.centralwidget)
        self.oButPwr.setGeometry(QtCore.QRect(350, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.oButPwr.setFont(font)
        self.oButPwr.setObjectName("oButPwr")
        self.oLabOnOff = QtWidgets.QLabel(self.centralwidget)
        self.oLabOnOff.setGeometry(QtCore.QRect(390, 140, 51, 51))
        self.oLabOnOff.setMaximumSize(QtCore.QSize(90, 90))
        self.oLabOnOff.setText("")
        self.oLabOnOff.setPixmap(QtGui.QPixmap(":/image/red.png"))
        self.oLabOnOff.setScaledContents(True)
        self.oLabOnOff.setObjectName("oLabOnOff")
        self.oComboDev = QtWidgets.QComboBox(self.centralwidget)
        self.oComboDev.setGeometry(QtCore.QRect(350, 61, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.oComboDev.setFont(font)
        self.oComboDev.setEditable(True)
        self.oComboDev.setObjectName("oComboDev")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(81, 460, 20, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(271, 460, 20, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        oMainWind.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(oMainWind)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 492, 21))
        self.menubar.setObjectName("menubar")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        self.oMenu = QtWidgets.QMenu(self.menubar)
        self.oMenu.setObjectName("oMenu")
        oMainWind.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(oMainWind)
        self.statusbar.setObjectName("statusbar")
        oMainWind.setStatusBar(self.statusbar)
        self.oActExit = QtWidgets.QAction(oMainWind)
        self.oActExit.setObjectName("oActExit")
        self.oActAbout = QtWidgets.QAction(oMainWind)
        self.oActAbout.setObjectName("oActAbout")
        self.menuInfo.addAction(self.oActAbout)
        self.oMenu.addAction(self.oActExit)
        self.menubar.addAction(self.oMenu.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(oMainWind)
        QtCore.QMetaObject.connectSlotsByName(oMainWind)

    def retranslateUi(self, oMainWind):
        _translate = QtCore.QCoreApplication.translate
        oMainWind.setWindowTitle(_translate("oMainWind", "SPD1xxxx Power Supply Tool V1.0"))
        self.oButConnect.setText(_translate("oMainWind", "Connect"))
        self.oButVoltSel.setText(_translate("oMainWind", "▶"))
        self.oButCurrSel.setText(_translate("oMainWind", "▶"))
        self.oRbutUsb.setText(_translate("oMainWind", "USB"))
        self.oRbutEthernet.setText(_translate("oMainWind", "Ethernet"))
        self.oRbut4Wire.setText(_translate("oMainWind", "4 Wires"))
        self.oRbut2Wire.setText(_translate("oMainWind", "2 Wires"))
        self.label_2.setText(_translate("oMainWind", "SPD Voltage & Current Setup"))
        self.label_3.setText(_translate("oMainWind", "V"))
        self.label_4.setText(_translate("oMainWind", "A"))
        self.label_5.setText(_translate("oMainWind", "V"))
        self.label_6.setText(_translate("oMainWind", "A"))
        self.oButLock.setText(_translate("oMainWind", "Lock"))
        self.oButPwr.setText(_translate("oMainWind", "On"))
        self.label_8.setText(_translate("oMainWind", "."))
        self.label_9.setText(_translate("oMainWind", "."))
        self.menuInfo.setTitle(_translate("oMainWind", "Info"))
        self.oMenu.setTitle(_translate("oMainWind", "Edit"))
        self.oActExit.setText(_translate("oMainWind", "Exit"))
        self.oActAbout.setText(_translate("oMainWind", "About"))

import ui_res_rc
