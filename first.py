import sys
import untitled
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtGui import  QIcon
class FirstMainWin(QMainWindow,untitled.Ui_MainWindow):
   #构造窗体
    def __init__(self,parent=None):
         super(FirstMainWin,self).__init__(parent)
         self.setupUi(self) #很重要，是将desiger的控件加到窗体中，由desiger设计的布局
         self.initUI()

         # 设置信号槽
         self.pushButton_4.clicked.connect(self.hello)

         self.lineEdit_5.textChanged.connect(self.change5)
         self.lineEdit_14.textChanged.connect(self.change14)
         self.lineEdit_6.textChanged.connect(self.change6)
         self.lineEdit_13.textChanged.connect(self.change13)



   # 初始化窗体
    def initUI(self):
        #自定义样式
         self.setWindowIcon(QIcon('./image/1.ico'))
         self.status=self.statusBar()
         self.status.showMessage('只存在5秒',5000)
         #设置窗体的标题
         self.setWindowTitle('我的第一个pyqt程序')



         self.show()
    def hello(self):
        self.textEdit.setText("hello world")
    # def change14(self):
    #
    def change5(self):
            text14=int(self.lineEdit_5.text())*2
            self.lineEdit_14.setText(str(text14))

    def change14(self):
            text19 = int(self.lineEdit_14.text()) * 2
            self.lineEdit_19.setText(str(text19))

    def change6(self):
            text13 = int(self.lineEdit_6.text()) * 2
            self.lineEdit_13.setText(str(text13))
    def change13(self):
            text18 = int(self.lineEdit_13.text()) * 2
            self.lineEdit_18.setText(str(text18))


if __name__=='__main__':
    app=QApplication(sys.argv)
    #实例化窗体
    w=FirstMainWin()

    #打开主循环，并关闭窗体
    sys.exit(app.exec_())