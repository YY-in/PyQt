# -*- coding: utf-8 -*- 
# @Time : 2021/8/17 11:44 上午 
# @Author : infinity-penguin
# @File : QObeject.py
import sys

from PyQt5.Qt import *


class Window(QWidget):  # 继承于QWidget
    def __init__(self):
        super().__init__()  # 调用父类的属性和方法，即获取QWidget方法和属性
        self.setWindowTitle("QObject对象名称属性添加")
        self.resize(600, 500)
        self.func_list()  # 自定义函数

    def func_list(self):
        self.func()
        self.func1()

    def func(self):
        obj = QObject()
        obj.setObjectName("第一个Object对象")
        print(obj.objectName())

    def func1(self):
        obj1 = QObject()
        obj1.setProperty("level1", "第一")  # 给对象添加一个属性和值
        obj1.setProperty("level2", "第二")
        print(obj1.property("level1"))  # 获取对象某一个特定的属性的值
        print(obj1.dynamicPropertyNames())  # 获取对象所有的属性


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个应用程序对象
    window = Window()
    window.show()
    sys.exit(app.exec_())
