# -*- coding: utf-8 -*- 
# @Time : 2021/8/17 9:45 上午 
# @Author : infinity-penguin
# @File : HelloWorld.py
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)  # sys.argv 是命令行参数；创建一个应用程序

window = QWidget()  # widget 小部件 window是widget的对象
window.setWindowTitle("软件名称")
window.resize(600, 500)  # resize 设置widget大小

btn = QPushButton(window)  # button继承于window，所以该button存在的位置是在window内部
btn.setText("按钮")  # 设置button文本
btn.resize(120, 30)  # 设置button的大小
btn.move(100, 100)  # 设置button在window中的位置
btn.setStyleSheet('background-color:green;font-size:16px;')  # QSS设置背景颜色和字体大小

label = QLabel()  # 创建标签,并没有被继承，所以单独显示
label.setText('标签')

label.show()
window.show()

sys.exit(app.exec_())  # 检测退出原因；app.exec_()循环程序，不循环会闪退
