#Singal_and_Slot 信号与槽
##Qt的核心机制，也是PyQt的核心机制
信号：是由对象或控件控件发射出去的消息，可以理解为事件

槽：本质上是一个函数或者方法，理解为事件函数

按钮的单击事件：当单击按钮时，按钮就会向外部发送单击的消息，这些发送出去的信号需要一些代码来拦截，这些代码就是槽

需要将信号和槽绑定

一个信号可以和多个槽绑定
