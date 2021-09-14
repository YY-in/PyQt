# -*- coding: utf-8 -*- 
# @Time : 2021/8/19 2:12 下午 
# @Author : infinity-penguin
# @File : QuitApplicqtion.py
import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QDesktopWidget, QMainWindow, QApplication, QPushButton, \
    QBoxLayout  # 水平布局
from PyQt5.QtGui import QIcon


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(300, 120)
        self.setWindowTitle("退出应用程序")
        # 添加button
        self.button1 = QPushButton("退出应用程序")
        # 将信号与槽进行绑定
        self.button1.clicked.connect(lambda: self.onClick_Button())
        # 创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    #   按钮单击事件的方法(自定义的槽)
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text()+'按钮被按下')
        application = QApplication.instance()
        # 退出应用程序
        application.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())
