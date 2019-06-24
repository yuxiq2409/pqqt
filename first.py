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
        self.pushButton_15.clicked.connect(self.change0)

   # 初始化窗体
    def initUI(self):
        #自定义样式
         self.setWindowIcon(QIcon('./image/1.ico'))
         self.status=self.statusBar()
         self.status.showMessage('只存在5秒',5000)
         #设置窗体的标题
         self.setWindowTitle('我的第一个pyqt程序')

    def hello(self):
        self.textEdit.setText("hello world")
    # def change14(self):
    #
    def change5(self):
        if self.lineEdit_5.text() == "":
            self.lineEdit_14.text = ""
        else:
            text14=round(float(self.lineEdit_5.text())*0.74,3)
            self.lineEdit_14.setText(str(text14))

    def change14(self):
        if self.lineEdit_14.text()== "":
            self.lineEdit_19.text=""
        else:
            text19 =round(float(self.lineEdit_14.text()) * 12,3)
            self.lineEdit_19.setText(str(text19))

    def change6(self):
        if self.lineEdit_6.text() == "":
            self.lineEdit_13.text = ""
        else:
            text13 = float(self.lineEdit_6.text()) * 2.5
            self.lineEdit_13.setText(str(text13))

    def change13(self):
        if self.lineEdit_13.text() == "":
            self.lineEdit_18.text = ""
        else:
            text18 = float(self.lineEdit_13.text()) * 2
            self.lineEdit_18.setText(str(text18))
    def change0(self):
        self.lineEdit_19.clear()
        self.lineEdit_14.clear()
        self.lineEdit_5.clear()

        self.lineEdit_18.clear()
        self.lineEdit_13.clear()
        self.lineEdit_6.clear()


if __name__=='__main__':
    app=QApplication(sys.argv)
    #实例化窗体
    w=FirstMainWin()
    w.show()
    #打开主循环，并关闭窗体
    sys.exit(app.exec_())