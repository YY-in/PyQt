# -*- coding: utf-8 -*- 
# @Time : 2021/8/17 10:36 上午 
# @Author : infinity-penguin
# @File : ImportTest.py
import sys
from OOHelloWorld import Window
from PyQt5.Qt import *

app =QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())