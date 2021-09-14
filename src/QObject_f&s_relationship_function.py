# -*- coding: utf-8 -*- 
# @Time : 2021/8/17 12:01 下午 
# @Author : infinity-penguin
# @File : QObject_f&s_relationship_function.py
'''
        obj1.setParent(obj2)  # 设置父对象
        obj3.setParent(obj1)  #
        print(obj1.parent())  # 获取父对象
        print(obj2.children())
        print(obj2.findChild(QObject))   # 获取直接的子对象
        print(obj2.findChildren(QObject))   # 获取所有的子对象
'''

from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("父子关系")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        obj1 = QObject()
        print('obj1', obj1)
        obj2 = QObject()
        print('obj2', obj2)
        obj3 = QObject()
        print('obj3', obj3)
        obj2.setParent(obj1)
        obj3.setParent(obj2)
        print(obj2.parent())
        print(obj2.children())

        print(obj1.findChild(QObject))
        print(obj1.findChildren(QObject))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())