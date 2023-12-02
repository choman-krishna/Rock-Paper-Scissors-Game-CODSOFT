# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\choose.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_secondWindow(object):
    def setupUi(self, secondWindow):
        secondWindow.setObjectName("secondWindow")
        secondWindow.resize(620, 481)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(secondWindow.sizePolicy().hasHeightForWidth())
        secondWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(secondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rock = QtWidgets.QPushButton(self.centralwidget)
        self.rock.setGeometry(QtCore.QRect(40, 20, 271, 161))
        self.rock.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rock.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\img/rock.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rock.setIcon(icon)
        self.rock.setIconSize(QtCore.QSize(250, 500))
        self.rock.setCheckable(True)
        self.rock.setObjectName("rock")
        self.scissors = QtWidgets.QPushButton(self.centralwidget)
        self.scissors.setGeometry(QtCore.QRect(190, 220, 281, 171))
        self.scissors.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scissors.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\img/scissors.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scissors.setIcon(icon1)
        self.scissors.setIconSize(QtCore.QSize(300, 500))
        self.scissors.setObjectName("scissors")
        self.paper = QtWidgets.QPushButton(self.centralwidget)
        self.paper.setGeometry(QtCore.QRect(340, 20, 271, 161))
        self.paper.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.paper.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\img/paper.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paper.setIcon(icon2)
        self.paper.setIconSize(QtCore.QSize(350, 200))
        self.paper.setObjectName("paper")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 190, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 180, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 400, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        secondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(secondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 26))
        self.menubar.setObjectName("menubar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        secondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(secondWindow)
        self.statusbar.setObjectName("statusbar")
        secondWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(secondWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuExit.addAction(self.actionQuit)
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(secondWindow)
        QtCore.QMetaObject.connectSlotsByName(secondWindow)

    def retranslateUi(self, secondWindow):
        _translate = QtCore.QCoreApplication.translate
        secondWindow.setWindowTitle(_translate("secondWindow", "MainWindow"))
        self.label.setText(_translate("secondWindow", "Rock"))
        self.label_2.setText(_translate("secondWindow", "Paper"))
        self.label_3.setText(_translate("secondWindow", "Scissors"))
        self.menuExit.setTitle(_translate("secondWindow", "Exit"))
        self.actionQuit.setText(_translate("secondWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    secondWindow = QtWidgets.QMainWindow()
    ui = Ui_secondWindow()
    ui.setupUi(secondWindow)
    secondWindow.show()
    sys.exit(app.exec_())