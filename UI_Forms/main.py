from PyQt5 import uic
import sys
from PyQt5.QtCore import *
from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QtCore, QMainWindow , QLabel , QVBoxLayout , QPushButton, QWidget , QLineEdit , QMessageBox
from PyQt5.QtGui import *
from Stock_Report import Ui_Dialog

import sys

class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext
    @property
    def run(self):                              # 2. Implement run()
        window = QWidget()
        version = self.build_settings['version']
        window.setWindowTitle("Stocks_Update v" + version)
        window.resize(250, 150)
        Label = QLabel("IPO To be seached")   # 9. Create a label obj
        self.textbox = QLineEdit()
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        okbutton = QPushButton('Ok')
        okbutton.setToolTip('Search')
        okbutton.clicked.connect(self.on_click)
        exitbutton = QPushButton('Exit')
        exitbutton.clicked.connect(self.exitBtn)


        layout = QVBoxLayout()                  # 6. Set up a Layout Variable
        layout.addWidget(self.textbox)
        layout.addWidget(Label)                 # 8 . attache Label to layout variable
        layout.addWidget(okbutton)                 # 7. Add Button (OK)
        layout.addWidget(exitbutton)               # 10. Add Button (exit)

        window.setLayout(layout)
        window.show()
        return self.app.exec_()                 # 3. End run() with this line


    #@pyqtSlot()
    def on_click(self):

        self.window2 = QWidget.QDialog()()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window2)
        self.window2.show()

        #textboxValue = self.textbox.text()
        #QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        #QMessageBox.about(self,"IPO ","message" + textboxValue)
        #self.textbox.setText("")


    def exitBtn(self):
        sys.exit()


if __name__ == '__main__':

    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run                     # 5. Invoke run()
    sys.exit(exit_code)
