# -*- coding: utf-8 -*- 
# @Time : 2021/8/20 1:15 下午 
# @Author : infinity-penguin
# @File : QLabelDemo.py
'''
setAlignment()  设置文本对齐方式，alignment排成直线

setIndent()  设置文本锁进

text()  获取文本内容

setBuddy()  设置伙伴关系

setText()  设置文本内容

selectedText() 返回所选择的字符

setWordWrap() 设置是否允许换行

Qlabel 常用的信号（事件）：
1。当鼠标划过Qlabel控件时触发：linkHovered
2。当鼠标单击Qlabel控件时触发：linkActivated

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QPixmap  # Palette调色板
from PyQt5.QtCore import Qt


class QlabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText('<font color=yellow>这是一个文本标签</font>')
        label1.setAutoFillBackground(True)  # 自动添加背景
        patette = QPalette()
        patette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(patette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href ='#'>欢迎使用Python GUI程序</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("./favicon.ico"))

        label4.setText("<a href='https://www.baidu.com/'>百度一下 </a>")
        label4.setToolTip("这是一个超链接")

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel控件演示")

    def linkHovered(self):
        print('当鼠标滑过label2标签时，触发事件')

    def linkClicked(self):
        print("当鼠标单击label4标签时，触发事件")


if __name__ =="__main__":
    app = QApplication(sys.argv)
    main =QlabelDemo()
    main.show()
    sys.exit(app.exec_())

