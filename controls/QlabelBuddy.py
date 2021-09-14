# -*- coding: utf-8 -*- 
# @Time : 2021/8/20 4:52 下午 
# @Author : infinity-penguin
# @File : QlabelBuddy.py
'''
QLabel与伙伴关系

'''
from _ctypes import Union

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import sys




class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QLabel与伙伴控件")

        nameLabel = QLabel('&Name', self)
        nameLineEdit = QLineEdit(self)
        # 设置伙伴控件
        nameLabel.setBuddy(nameLabel)

        passwordLabel = QLabel("&Password", self)
        passwordLineEdit = QLineEdit(self)
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel)
        mainLayout.addWidget(nameLineEdit)  # 初始行数，初始列数，占用行数，占用列数
        mainLayout.addWidget(passwordLabel)
        mainLayout.addWidget(passwordLineEdit)

        mainLayout.addWidget(btnOK)
        mainLayout.addWidget(btnCancel)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()
    sys.exit(app.exec_())
