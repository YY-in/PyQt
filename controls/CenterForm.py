# -*- coding: utf-8 -*- 
# @Time : 2021/8/19 1:52 下午 
# @Author : infinity-penguin
# @File : CenterForm.py

# QDesktopWidget 可以得到整个屏幕的尺寸


import sys
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm, self).__init__()

        # 设置主窗口的标题
        self.setWindowTitle("第一个主窗口应用")

        # 设置窗口的尺寸
        self.resize(400, 300)

    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2

        self.move(newLeft, newTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./favicon.ico'))
    main = CenterForm()
    main.show()
    sys.exit(app.exec_())
