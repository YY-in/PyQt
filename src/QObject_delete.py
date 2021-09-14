# -*- coding: utf-8 -*- 
# @Time : 2021/8/17 12:18 下午 
# @Author : infinity-penguin
# @File : QObject_delete.py

from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("对象删除")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        obj1 = QObject()
        self.obj1 = obj1
        obj2 = QObject()
        obj3 = QObject()
        obj2.setParent(obj1)
        obj3.setParent(obj2)
        print(obj1)
        print(obj2)
        print(obj3)

        obj1.destroyed.connect(lambda: print('obj1被释放'))  # 信号
        obj2.destroyed.connect(lambda: print('obj2被释放'))
        obj3.destroyed.connect(lambda: print('obj3被释放'))

        # del obj2   解除obj2对象名称 与 内存中obj2实际指针 的连接，并没有删除内存中的内容，编译后仍会执行
        print(obj2.deleteLater())  # 在代码执行结束后删除代码，可以将一个对象从堆空间中直接删除
        print(obj1.children())

        # 案例
        label1 = QLabel(self)
        label1.setText('label1')
        label1.move(50, 50)
        label1.setStyleSheet('background-color:green')

        label2 = QLabel(self)
        label2.setText('label2')
        label2.move(100, 100)
        label2.setStyleSheet('background-color:green')

        label3 = QLabel(self)
        label3.setText('label3')
        label3.move(150, 150)
        label3.setStyleSheet('background-color:green')

        # label2.deleteLater()
        del label2


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
