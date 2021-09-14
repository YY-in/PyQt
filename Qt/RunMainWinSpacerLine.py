# -*- coding: utf-8 -*- 
# @Time : 2021/8/17 3:08 下午 
# @Author : infinity-penguin
# @File : RunMainWinSpacerLine.py
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import MainWinSpacerLine

if __name__ == '__main__':
    app =QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainWinSpacerLine.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())