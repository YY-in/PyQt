# SizePolicy 尺寸策略
sizeHint(期望尺寸)
对于大多数控件来说，sizeHint的值是只读的

读取期望尺寸sizeHint
```
self.pushButton.sizeHint().width()
self.pushButton.sizeHint().height()
```
最小期望尺寸miniumSizeHint
```
self.pushButton.miniumSizeHint().width()
self.pushButton.miniumSizeHint().height()
```
代码
```
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import sizePolicy

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = sizePolicy.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
```



