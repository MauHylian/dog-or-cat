# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 911)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelPath = QtWidgets.QLabel(self.centralwidget)
        self.labelPath.setObjectName("labelPath")
        self.gridLayout.addWidget(self.labelPath, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.view = QtWidgets.QGraphicsView(self.centralwidget)
        self.view.setObjectName("view")
        self.gridLayout.addWidget(self.view, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.labelPrediccion = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelPrediccion.setFont(font)
        self.labelPrediccion.setObjectName("labelPrediccion")
        self.verticalLayout_2.addWidget(self.labelPrediccion)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonCargar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCargar.setObjectName("buttonCargar")
        self.horizontalLayout.addWidget(self.buttonCargar)
        self.buttonPredecir = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPredecir.setObjectName("buttonPredecir")
        self.horizontalLayout.addWidget(self.buttonPredecir)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelPath.setText(_translate("MainWindow", "TextLabel"))
        self.labelPrediccion.setText(_translate("MainWindow", "TextLabel"))
        self.buttonCargar.setText(_translate("MainWindow", "Cargar Imagen"))
        self.buttonPredecir.setText(_translate("MainWindow", "Predecir"))
