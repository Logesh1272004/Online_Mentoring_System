# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MentG.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import csv
import sqlsuname
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def stmark(self):
        f1=open('sname.txt','r')
        r=f1.read()
        f1.close()
        r2=sqlsuname.uname(r)
        f=open('tmarks.csv', 'a+')
        cw=csv.writer(f)
        m1=self.lineEdit_2.text()
        m2=self.lineEdit_3.text()
        m3=self.lineEdit_7.text()
        m4=self.lineEdit_5.text()
        l=[r2,m1,m2,m3,m4]
        cw.writerow(l)
        f.close()
        Form.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 720)
        Form.setMinimumSize(QtCore.QSize(480, 720))
        Form.setMaximumSize(QtCore.QSize(480, 720))

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        Form.setFont(font)
        Form.setStyleSheet("background: rgb(134,186,212);")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 40, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 180, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 410, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 330, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 250, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 175, 81, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("background-color: rgb(185,215,230);\n"
                                    "border-radius: 10px;")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(380, 250, 81, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet("background-color: rgb(185,215,230);\n"
                                    "border-radius: 10px;")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(380, 330, 81, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setStyleSheet("background-color: rgb(185,215,230);\n"
                                    "border-radius: 10px;")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(380, 410, 81, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setStyleSheet("background-color: rgb(185,215,230);\n"
                                    "border-radius: 10px;")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(220, 110, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(370, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 500, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.pushButton.setFont(font)
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
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(300, 175, 81, 41))
        self.label_8.setText("N/A")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(300, 250, 81, 41))
        self.label_9.setText("N/A")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(300, 330, 81, 41))
        self.label_10.setText("N/A")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(300, 410, 81, 41))
        self.label_11.setText("N/A")
        self.label_11.setObjectName("label_11")

        f=open('sname.txt','r')
        r=f.read()
        f.close()
        r2=sqlsuname.uname(r)
        f1=open('target.csv', 'r')
        cr=csv.reader(f1)
        for row in cr:
            if(row[0] == r2):
                self.label_8.setText(row[1])
                self.label_9.setText(row[2])
                self.label_10.setText(row[3])
                self.label_11.setText(row[4])

        f1.close()

        self.pushButton.clicked.connect(self.stmark)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Marks"))
        self.label_2.setText(_translate("Form", "Data Science"))
        self.label_3.setText(_translate("Form", "Mathematics"))
        self.label_4.setText(_translate("Form", "Big data"))
        self.label_5.setText(_translate("Form", "Machine Learning"))
        self.label_6.setText(_translate("Form", "Target expected"))
        self.label_7.setText(_translate("Form", "Marks Scored"))
        self.pushButton.setText(_translate("Form", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
