# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MentA.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def stu(self):
        subprocess.call(["python", "studlist.py"])

    def res(self):
        subprocess.call(["python", "resource.py"])

    def rem(self):
        subprocess.call(["python", "remainder.py"])

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 720)
        Form.setMinimumSize(QtCore.QSize(480, 720))
        Form.setMaximumSize(QtCore.QSize(480, 720))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        Form.setFont(font)
        Form.setStyleSheet("background: rgb(134,186,212);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 30, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 140, 191, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: rgb(185,215,230)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{\n"
"background:rgba(254, 234, 230);\n"
"background: rgb(185,215,230);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"color:rgba(255,255,255);\n"
"background: rgba(0, 0, 0,200);\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 240, 191, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background: rgb(185,215,230)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background:rgba(254, 234, 230);\n"
"background: rgb(185,215,230);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"color:rgba(255,255,255);\n"
"background: rgba(0, 0, 0,200);\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 340, 191, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background: rgb(185,215,230)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background:rgba(254, 234, 230);\n"
"background: rgb(185,215,230);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"color:rgba(255,255,255);\n"
"background: rgba(0, 0, 0,200);\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 440, 191, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background: rgb(185,215,230)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background:rgba(254, 234, 230);\n"
"background: rgb(185,215,230);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"color:rgba(255,255,255);\n"
"background: rgba(0, 0, 0,200);\n"
"border-radius: 10px;\n"
"}")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.pushButton_3.clicked.connect(self.res)
        self.pushButton_2.clicked.connect(self.rem)
        self.pushButton.clicked.connect(self.stu)
        self.pushButton_4.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Welcome"))
        self.pushButton.setText(_translate("Form", "View Students"))
        self.pushButton_2.setText(_translate("Form", "Remainder"))
        self.pushButton_3.setText(_translate("Form", "Resources"))
        self.pushButton_4.setText(_translate("Form", "Exit"))

        f = open("mentor.txt", "r")
        r = f.read()
        f.close()
        self.label_2.setText(_translate("Form", r))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
