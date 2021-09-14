# -*- coding: utf-8 -*- 
# @Time : 2021/8/17 8:12 下午 
# @Author : infinity-penguin
# @File : RunMainWinSingal_Slot.py
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import MainWinSingal_Slot

if __name__ == '__main__':
    app =QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainWinSingal_Slot.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())