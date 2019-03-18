# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ResultsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogCheck(object):
    def setupUi(self, DialogCheck):
        DialogCheck.setObjectName("DialogCheck")
        DialogCheck.resize(327, 115)
        self.okbtn = QtWidgets.QPushButton(DialogCheck)
        self.okbtn.setGeometry(QtCore.QRect(100, 70, 111, 32))
        self.okbtn.setObjectName("okbtn")
        self.okbtn.clicked.connect(self.windowClose)

        self.retranslateUi(DialogCheck)
        QtCore.QMetaObject.connectSlotsByName(DialogCheck)

    def retranslateUi(self, DialogCheck):
        _translate = QtCore.QCoreApplication.translate
        DialogCheck.setWindowTitle(_translate("DialogCheck", "Results"))
        self.okbtn.setText(_translate("DialogCheck", "Ok"))


    def windowClose(self):
        QtWidgets.qApp.quit
        #sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogCheck = QtWidgets.QDialog()
    ui = Ui_DialogCheck()
    ui.setupUi(DialogCheck)
    DialogCheck.show()
    sys.exit(app.exec_())
