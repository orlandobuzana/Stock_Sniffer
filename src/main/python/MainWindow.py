# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Status.ui'
#
# Created by: Orlando Buzana
#
# WARNING! All changes made in this file will be lost!
from fbs_runtime.application_context import ApplicationContext

from PyQt5 import QtCore, QtGui, QtWidgets
from Results import Ui_Results


class Ui_MainWindowAnalytics(ApplicationContext):#object):
    def setupUi(self, MainWindowAnalytics):

        MainWindowAnalytics.setObjectName("MainWindowAnalytics")
        MainWindowAnalytics.resize(320, 143)
        self.centralwidget = QtWidgets.QWidget(MainWindowAnalytics)
        self.centralwidget.setObjectName("centralwidget")
        self.exitbtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitbtn.setGeometry(QtCore.QRect(90, 60, 111, 32))
        self.exitbtn.setObjectName("exitbtn")
        self.exitbtn.clicked.connect(self.windowClose)
        self.searchbtn = QtWidgets.QPushButton(self.centralwidget)
        self.searchbtn.setGeometry(QtCore.QRect(190, 60, 111, 32))
        self.searchbtn.setObjectName("searchbtn")
        self.searchbtn.clicked.connect(self.newWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label.setObjectName("label")
        self.lineIPO = QtWidgets.QLineEdit(self.centralwidget)
        self.lineIPO.setGeometry(QtCore.QRect(20, 30, 281, 21))
        self.lineIPO.setInputMask("")
        self.lineIPO.setText("")
        self.lineIPO.setObjectName("lineIPO")
        MainWindowAnalytics.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowAnalytics)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 22))
        self.menubar.setObjectName("menubar")
        MainWindowAnalytics.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowAnalytics)
        self.statusbar.setObjectName("statusbar")
        MainWindowAnalytics.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowAnalytics)
        QtCore.QMetaObject.connectSlotsByName(MainWindowAnalytics)

    def retranslateUi(self, MainWindowAnalytics):
        _translate = QtCore.QCoreApplication.translate
        version = self.build_settings['version']
        MainWindowAnalytics.setWindowTitle(_translate("MainWindowAnalytics", "Stocks Analytics "+version))
        self.exitbtn.setToolTip(_translate("MainWindowAnalytics", "Close Application"))
        self.exitbtn.setText(_translate("MainWindowAnalytics", "Exit"))
        self.searchbtn.setToolTip(_translate("MainWindowAnalytics", "Search for new IPO"))
        self.searchbtn.setText(_translate("MainWindowAnalytics", "Search"))
        self.label.setText(_translate("MainWindowAnalytics", "Write the IPO:"))

    def newWindow(self):

        self.window2 = QtWidgets.QWidget()
        self.ui = Ui_Results()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def windowClose(self):

       sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowAnalytics = QtWidgets.QMainWindow()
    ui = Ui_MainWindowAnalytics()
    ui.setupUi(MainWindowAnalytics)
    MainWindowAnalytics.show()
    sys.exit(app.exec_())
