# -*- coding: utf-8 -*- 
# @Time : 2021/8/17 9:12 下午 
# @Author : infinity-penguin
# @File : RunMainWinMenuToolbar.py
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import MainWinMenuToolbar

if __name__ == "__main__":
    app =QApplication(sys.argv)
    window = QMainWindow()
    ui = MainWinMenuToolbar.Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())