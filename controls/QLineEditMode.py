# -*- coding: utf-8 -*- 
# @Time : 2021/8/22 2:25 下午 
# @Author : infinity-penguin
# @File : QLineEditMode.py
"""
QLineEdit控件与回显模式

基本功能：输入单行的文本

EchoMode(回显模式)

4种回显模式
1.Normal    正常回显模式
2.NoEcho    不回显
3.Password  密码掩饰回显
4.PasswordEchoOnEdit  密码半掩饰回显

"""
import sys
from PyQt5.QtWidgets import QFormLayout, QLineEdit, QWidget, QApplication


class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("文本输入框回显")

        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoLineEdit = QLineEdit()

        # 添加到布局
        formLayout.addRow("Normal", normalLineEdit)  # Label、Widgets
        formLayout.addRow("NoEcho", noEchoLineEdit)
        formLayout.addRow("Password", passwordLineEdit)
        formLayout.addRow("PasswordEchoOnEdit", passwordEchoLineEdit)

        # PlaceholderText 显示提示
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QLabel
from PyQt5.QtWidgets import *


class Winform(QWidget):
    def __init__(self):
        super(Winform, self).__init__()
        self.setWindowTitle("test")
        self.resize(400, 100)
        self.main()

    def main(self):
        # 1.声明布局
        self.formlayout = QFormLayout()
        # 2.声明控件
        self.label1 = QLabel("账号")
        self.lineEdit1 = QLineEdit()
        self.label2 = QLabel("密码")
        self.lineEdit2 = QLineEdit()
        # 对lineEdit2设置密码隐藏
        self.lineEdit2.setEchoMode(QLineEdit.Password)

        # 3.将控件加入到布局当中
        self.formlayout.addRow(self.label1, self.lineEdit1)
        self.formlayout.addRow(self.label2, self.lineEdit2)
        # 4.将整个带有控件的布局加入到主类中
        self.setLayout(self.formlayout)
        self.signIn = QPushButton("登录")
        # self.signIn=QPushButton("注册")
        self.signIn.setFixedWidth(80)
        self.signIn.setFixedHeight(30)
        self.formlayout.addRow("", self.signIn)


if __name__ == "__main__":
    # sys.argv是参数
    # 所有的PyQt5应用必须创建一个应用（Application）对象。
    # sys.argv参数是一个来自命令行的参数列表。
    # Python脚本可以在shell中运行。这是我们用来控制我们应用启动的一种方法。
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec())
    # app.exec_() - -------------消息循环结束之后，进程自然也会结束
    # sys.exit(app.exec_()) - ---消息循环结束之后返回0，接着调用sys.exit(0)
    # 退出程序
"""