# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\pyqt\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(189, 21, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(690, 30, 81, 192))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 21, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(71, 21, 81, 23))
        self.pushButton_14.setObjectName("pushButton_14")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setWindowModality(QtCore.Qt.ApplicationModal)
        self.line.setGeometry(QtCore.QRect(70, 70, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(42)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(22)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(40, 130, 91, 20))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 180, 104, 71))
        self.textEdit.setObjectName("textEdit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(280, 420, 90, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_6.addWidget(self.lineEdit_10)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.label_13)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(280, 400, 90, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_7.addWidget(self.lineEdit_11)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(279, 480, 90, 22))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_8.addWidget(self.lineEdit_12)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_8.addWidget(self.label_15)
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(280, 350, 90, 22))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_9.addWidget(self.lineEdit_13)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_9.addWidget(self.label_16)
        self.layoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(280, 320, 90, 22))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.horizontalLayout_10.addWidget(self.lineEdit_14)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_10.addWidget(self.label_17)
        self.layoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_6.setGeometry(QtCore.QRect(380, 420, 90, 22))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.horizontalLayout_11.addWidget(self.lineEdit_15)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_11.addWidget(self.label_18)
        self.layoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_7.setGeometry(QtCore.QRect(380, 400, 90, 22))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.horizontalLayout_12.addWidget(self.lineEdit_16)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_7)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_12.addWidget(self.label_19)
        self.layoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_9.setGeometry(QtCore.QRect(380, 350, 90, 22))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.layoutWidget_9)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.horizontalLayout_14.addWidget(self.lineEdit_18)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_9)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_14.addWidget(self.label_21)
        self.layoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_10.setGeometry(QtCore.QRect(380, 320, 90, 22))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.layoutWidget_10)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.horizontalLayout_15.addWidget(self.lineEdit_19)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_10)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_15.addWidget(self.label_22)
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(380, 480, 91, 23))
        self.pushButton_15.setObjectName("pushButton_15")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(470, 50, 177, 100))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(150, 110, 251, 161))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 2, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 2, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 3, 0, 1, 2)
        self.pushButton_13 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 3, 2, 1, 1)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(90, 310, 62, 211))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.widget2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(181, 320, 90, 22))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout.addWidget(self.lineEdit_5)
        self.label_8 = QtWidgets.QLabel(self.widget3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.widget4 = QtWidgets.QWidget(self.centralwidget)
        self.widget4.setGeometry(QtCore.QRect(181, 350, 90, 22))
        self.widget4.setObjectName("widget4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget4)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_2.addWidget(self.lineEdit_6)
        self.label_9 = QtWidgets.QLabel(self.widget4)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.widget5 = QtWidgets.QWidget(self.centralwidget)
        self.widget5.setGeometry(QtCore.QRect(181, 400, 90, 22))
        self.widget5.setObjectName("widget5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget5)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_3.addWidget(self.lineEdit_7)
        self.label_10 = QtWidgets.QLabel(self.widget5)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.widget6 = QtWidgets.QWidget(self.centralwidget)
        self.widget6.setGeometry(QtCore.QRect(181, 420, 90, 22))
        self.widget6.setObjectName("widget6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget6)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_4.addWidget(self.lineEdit_8)
        self.label_11 = QtWidgets.QLabel(self.widget6)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.widget7 = QtWidgets.QWidget(self.centralwidget)
        self.widget7.setGeometry(QtCore.QRect(180, 480, 90, 22))
        self.widget7.setObjectName("widget7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget7)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_5.addWidget(self.lineEdit_9)
        self.label_12 = QtWidgets.QLabel(self.widget7)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setCheckable(True)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setCheckable(True)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setCheckable(True)
        self.action_3.setObjectName("action_3")
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action)
        self.toolBar.addAction(self.action_2)
        self.toolBar.addAction(self.action_3)

        self.retranslateUi(MainWindow)
        self.pushButton_14.clicked.connect(MainWindow.close)
        self.checkBox.toggled['bool'].connect(self.textEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "这是我的"))
        self.pushButton.setText(_translate("MainWindow", "2"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "1"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "12"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "13"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "13"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "15"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_14.setText(_translate("MainWindow", "关闭窗口"))
        self.checkBox.setText(_translate("MainWindow", "显示/不显示"))
        self.label_13.setText(_translate("MainWindow", "英尺="))
        self.label_14.setText(_translate("MainWindow", "英尺="))
        self.label_15.setText(_translate("MainWindow", "F"))
        self.label_16.setText(_translate("MainWindow", "磅尺="))
        self.label_17.setText(_translate("MainWindow", "磅尺="))
        self.label_18.setText(_translate("MainWindow", "厘米"))
        self.label_19.setText(_translate("MainWindow", "英尺"))
        self.label_21.setText(_translate("MainWindow", "牛米"))
        self.label_22.setText(_translate("MainWindow", "磅寸"))
        self.pushButton_15.setText(_translate("MainWindow", "清除所有"))
        self.label.setText(_translate("MainWindow", "姓名："))
        self.label_2.setText(_translate("MainWindow", "年龄："))
        self.label_3.setText(_translate("MainWindow", "身高："))
        self.label_4.setText(_translate("MainWindow", "电话："))
        self.pushButton_6.setText(_translate("MainWindow", "1"))
        self.pushButton_5.setText(_translate("MainWindow", "2"))
        self.pushButton_2.setText(_translate("MainWindow", "3"))
        self.pushButton_3.setText(_translate("MainWindow", "4"))
        self.pushButton_7.setText(_translate("MainWindow", "5"))
        self.pushButton_8.setText(_translate("MainWindow", "6"))
        self.pushButton_9.setText(_translate("MainWindow", "4"))
        self.pushButton_11.setText(_translate("MainWindow", "5"))
        self.pushButton_10.setText(_translate("MainWindow", "6"))
        self.pushButton_12.setText(_translate("MainWindow", "0"))
        self.pushButton_13.setText(_translate("MainWindow", "+"))
        self.label_5.setText(_translate("MainWindow", "力矩换算："))
        self.label_6.setText(_translate("MainWindow", "长度换算："))
        self.label_7.setText(_translate("MainWindow", "温度换算："))
        self.label_8.setText(_translate("MainWindow", "牛米="))
        self.label_9.setText(_translate("MainWindow", "磅寸="))
        self.label_10.setText(_translate("MainWindow", "厘米="))
        self.label_11.setText(_translate("MainWindow", "英寸="))
        self.label_12.setText(_translate("MainWindow", "C="))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "新建"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action.setText(_translate("MainWindow", "打开"))
        self.action.setToolTip(_translate("MainWindow", "打开"))
        self.action_2.setText(_translate("MainWindow", "关闭"))
        self.action_2.setToolTip(_translate("MainWindow", "关闭"))
        self.action_3.setText(_translate("MainWindow", "新建"))

