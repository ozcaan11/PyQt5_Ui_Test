# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uixml/mainform.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_Left = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_Left.sizePolicy().hasHeightForWidth())
        self.dockWidget_Left.setSizePolicy(sizePolicy)
        self.dockWidget_Left.setMinimumSize(QtCore.QSize(200, 419))
        self.dockWidget_Left.setMaximumSize(QtCore.QSize(300, 524287))
        self.dockWidget_Left.setStyleSheet("QDockWidget#dockWidget_Left {border: 2px dashed #456 }")
        self.dockWidget_Left.setSizeIncrement(QtCore.QSize(0, 0))
        self.dockWidget_Left.setFloating(False)
        self.dockWidget_Left.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_Left.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_Left.setObjectName("dockWidget_Left")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.cmdBooks = QtWidgets.QCommandLinkButton(self.dockWidgetContents)
        self.cmdBooks.setObjectName("cmdBooks")
        self.verticalLayout.addWidget(self.cmdBooks)
        self.cmdReaders = QtWidgets.QCommandLinkButton(self.dockWidgetContents)
        self.cmdReaders.setObjectName("cmdReaders")
        self.verticalLayout.addWidget(self.cmdReaders)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.dockWidget_Left.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_Left)
        self.dockWidget_Top = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_Top.setMinimumSize(QtCore.QSize(196, 70))
        self.dockWidget_Top.setMaximumSize(QtCore.QSize(524287, 70))
        self.dockWidget_Top.setStyleSheet("QDockWidget#dockWidget_Top {border: 2px dashed #456 }")
        self.dockWidget_Top.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_Top.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.TopDockWidgetArea)
        self.dockWidget_Top.setObjectName("dockWidget_Top")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.txtSearch = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.txtSearch.setObjectName("txtSearch")
        self.horizontalLayout_3.addWidget(self.txtSearch)
        self.btnSearch = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.btnSearch.setObjectName("btnSearch")
        self.horizontalLayout_3.addWidget(self.btnSearch)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.dockWidget_Top.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_Top)
        self.dockWidget_Right = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_Right.setMinimumSize(QtCore.QSize(250, 419))
        self.dockWidget_Right.setMaximumSize(QtCore.QSize(350, 524287))
        self.dockWidget_Right.setStyleSheet("QDockWidget#dockWidget_Right {border: 2px dashed #456 }")
        self.dockWidget_Right.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_Right.setObjectName("dockWidget_Right")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblName = QtWidgets.QLabel(self.dockWidgetContents_4)
        self.lblName.setObjectName("lblName")
        self.verticalLayout_4.addWidget(self.lblName)
        self.txtName = QtWidgets.QLineEdit(self.dockWidgetContents_4)
        self.txtName.setObjectName("txtName")
        self.verticalLayout_4.addWidget(self.txtName)
        self.lblAuthor_Starttime = QtWidgets.QLabel(self.dockWidgetContents_4)
        self.lblAuthor_Starttime.setObjectName("lblAuthor_Starttime")
        self.verticalLayout_4.addWidget(self.lblAuthor_Starttime)
        self.txtAuthor_Starttime = QtWidgets.QLineEdit(self.dockWidgetContents_4)
        self.txtAuthor_Starttime.setObjectName("txtAuthor_Starttime")
        self.verticalLayout_4.addWidget(self.txtAuthor_Starttime)
        self.lblPageNo_Endtime = QtWidgets.QLabel(self.dockWidgetContents_4)
        self.lblPageNo_Endtime.setObjectName("lblPageNo_Endtime")
        self.verticalLayout_4.addWidget(self.lblPageNo_Endtime)
        self.txtPageNo_Endtime = QtWidgets.QLineEdit(self.dockWidgetContents_4)
        self.txtPageNo_Endtime.setObjectName("txtPageNo_Endtime")
        self.verticalLayout_4.addWidget(self.txtPageNo_Endtime)
        self.lblShortDesc_Before = QtWidgets.QLabel(self.dockWidgetContents_4)
        self.lblShortDesc_Before.setObjectName("lblShortDesc_Before")
        self.verticalLayout_4.addWidget(self.lblShortDesc_Before)
        self.txtShortDesc_Before = QtWidgets.QTextEdit(self.dockWidgetContents_4)
        self.txtShortDesc_Before.setObjectName("txtShortDesc_Before")
        self.verticalLayout_4.addWidget(self.txtShortDesc_Before)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.dockWidget_Right.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_Right)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dockWidget_Left.setWindowTitle(_translate("MainWindow", "Menu"))
        self.cmdBooks.setText(_translate("MainWindow", "Books"))
        self.cmdReaders.setText(_translate("MainWindow", "Readers"))
        self.btnSearch.setText(_translate("MainWindow", "Search"))
        self.dockWidget_Right.setWindowTitle(_translate("MainWindow", "Details"))
        self.lblName.setText(_translate("MainWindow", "Name"))
        self.lblAuthor_Starttime.setText(_translate("MainWindow", "Author"))
        self.lblPageNo_Endtime.setText(_translate("MainWindow", "Page numbers"))
        self.lblShortDesc_Before.setText(_translate("MainWindow", "Short description"))

