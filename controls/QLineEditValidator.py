# -*- coding: utf-8 -*- 
# @Time : 2021/8/22 11:12 下午 
# @Author : infinity-penguin
# @File : QLineEditValidator.py
"""
现在QLineEdit控件的输入(校验器)
如果限制只能输入整数、浮点数或满足一定条件的字符串

"""

import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator, QIntValidator
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QLabel
from PyQt5.QtWidgets import *


class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.setWindowTitle("校验器")
        self.resize(400, 100)
        self.main()

    def main(self):
        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        regLineEdit = QLineEdit()

        self.setLayout(formLayout)

        formLayout.addRow("整数类型", intLineEdit)
        formLayout.addRow("浮点类型", doubleLineEdit)
        formLayout.addRow("数字和字母", regLineEdit)

        intLineEdit.setPlaceholderText("整形")
        doubleLineEdit.setPlaceholderText("浮点型")
        regLineEdit.setPlaceholderText("字母和数字")

        # 整数校验器
        intValidator = QIntValidator(self)
        intValidator.setRange(1, 99)

        # 浮点型校验器
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360, 360)
        # 设置正常显示浮点数
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 设置精度，小数点后两位
        doubleValidator.setDecimals(2)

        # 正则表达式校验器
        reg = QRegExp("[a-zA-z0-9]+$")
        regValidator = QRegExpValidator(self)
        regValidator.setRegExp(reg)

        # 设置校验器
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        regLineEdit.setValidator(regValidator)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())
