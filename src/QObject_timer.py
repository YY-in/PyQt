# -*- coding: utf-8 -*- 
# @Time : 2021/8/17 12:45 下午 
# @Author : infinity-penguin
# @File : QObject_timer.py

from PyQt5.Qt import *
import sys


class Obj(QObject):
    def timerEvent(self, QTimerEvent): # QTimerEvent 参数
        print(QTimerEvent, 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    obj = Obj()
    timer_id = obj.startTimer(1000)

    # obj.killTimer(timer_id)

    window.show()
    sys.exit(app.exec_())