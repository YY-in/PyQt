# -*- coding: utf-8 -*- 
# @Time : 2021/8/17 12:13 下午 
# @Author : infinity-penguin
# @File : QObject_typeDefine.py
'''
        isWidgetType()  # 判断类型
        inherits('')  # 是否继承与某个类
'''

from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("类型判定")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        obj = QObject()
        win = QWidget()
        btn = QPushButton()
        label = QLabel()

        obj_list = [obj, win, btn, label]
        for o in obj_list:
            # print(o.isWidgetType())
            print(o.inherits('QPushButton'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())