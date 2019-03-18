# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ResultsForm.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Results(object):
    def setupUi(self, Results):
        Results.setObjectName("Results")
        Results.resize(395, 300)
        self.exitbtn = QtWidgets.QPushButton(Results)
        self.exitbtn.setGeometry(QtCore.QRect(260, 260, 111, 32))
        self.exitbtn.setObjectName("exitbtn")
        self.savebtn = QtWidgets.QPushButton(Results)
        self.savebtn.setGeometry(QtCore.QRect(140, 260, 111, 32))
        self.savebtn.setObjectName("savebtn")
        self.newSeachbtn = QtWidgets.QPushButton(Results)
        self.newSeachbtn.setGeometry(QtCore.QRect(20, 260, 111, 32))
        self.newSeachbtn.setObjectName("newSeachbtn")
        self.ipoInfoviwer = QtWidgets.QTextEdit(Results)
        self.ipoInfoviwer.setGeometry(QtCore.QRect(20, 10, 351, 231))
        self.ipoInfoviwer.setObjectName("ipoInfoviwer")

        self.retranslateUi(Results)
        QtCore.QMetaObject.connectSlotsByName(Results)

    def retranslateUi(self, Results):
        _translate = QtCore.QCoreApplication.translate
        Results.setWindowTitle(_translate("Results", "Results fo: "))
        self.exitbtn.setText(_translate("Results", "Exit"))
        self.savebtn.setText(_translate("Results", "Save"))
        self.newSeachbtn.setText(_translate("Results", "New Search"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Results = QtWidgets.QWidget()
    ui = Ui_Results()
    ui.setupUi(Results)
    Results.show()
    sys.exit(app.exec_())
