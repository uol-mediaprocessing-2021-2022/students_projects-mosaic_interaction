# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 450)
        MainWindow.setMinimumSize(QtCore.QSize(800, 450))
        MainWindow.setMaximumSize(QtCore.QSize(800, 450))
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 450))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 450))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 802, 452))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_frame = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.left_frame.setMinimumSize(QtCore.QSize(200, 450))
        self.left_frame.setMaximumSize(QtCore.QSize(200, 450))
        self.left_frame.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_frame.setObjectName("left_frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.left_frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 201, 152))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.libraryTabButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.libraryTabButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.libraryTabButton.setFont(font)
        self.libraryTabButton.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"/*    text-align: center;*/\n"
"    color: rgb(255,255,255);\n"
"    text-align: left;;\n"
"    padding-left: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(44, 49, 60);\n"
"}\n"
"QPushButton:checked {    \n"
"    background-color: rgb(44, 49, 60);\n"
"}")
        self.libraryTabButton.setCheckable(True)
        self.libraryTabButton.setChecked(True)
        self.libraryTabButton.setAutoExclusive(True)
        self.libraryTabButton.setObjectName("libraryTabButton")
        self.verticalLayout.addWidget(self.libraryTabButton)
        self.classicTabButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.classicTabButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.classicTabButton.setFont(font)
        self.classicTabButton.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"/*    text-align: center;*/\n"
"    color: rgb(255,255,255);\n"
"    text-align: left;;\n"
"    padding-left: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(44, 49, 60);\n"
"}\n"
"QPushButton:checked {    \n"
"    background-color: rgb(44, 49, 60);\n"
"}")
        self.classicTabButton.setCheckable(True)
        self.classicTabButton.setAutoExclusive(True)
        self.classicTabButton.setObjectName("classicTabButton")
        self.verticalLayout.addWidget(self.classicTabButton)
        self.partialTabButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.partialTabButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partialTabButton.setFont(font)
        self.partialTabButton.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"/*    text-align: center;*/\n"
"    color: rgb(255,255,255);\n"
"    text-align: left;;\n"
"    padding-left: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(44, 49, 60);\n"
"}\n"
"QPushButton:checked {    \n"
"    background-color: rgb(44, 49, 60);\n"
"}")
        self.partialTabButton.setCheckable(True)
        self.partialTabButton.setAutoExclusive(True)
        self.partialTabButton.setFlat(True)
        self.partialTabButton.setObjectName("partialTabButton")
        self.verticalLayout.addWidget(self.partialTabButton)
        self.horizontalLayout.addWidget(self.left_frame)
        self.stackedWidget = QtWidgets.QStackedWidget(self.horizontalLayoutWidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(600, 450))
        self.stackedWidget.setMaximumSize(QtCore.QSize(600, 450))
        self.stackedWidget.setStyleSheet("background-color: rgb(44, 49, 60);")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stackedWidget.setObjectName("stackedWidget")
        self.libraryPage = QtWidgets.QWidget()
        self.libraryPage.setObjectName("libraryPage")
        self.libraryLineEdit = QtWidgets.QLineEdit(self.libraryPage)
        self.libraryLineEdit.setGeometry(QtCore.QRect(110, 20, 441, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.libraryLineEdit.setFont(font)
        self.libraryLineEdit.setStyleSheet("QLineEdit {    \n"
"    border: none;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5;\n"
"}")
        self.libraryLineEdit.setObjectName("libraryLineEdit")
        self.libraryLabel = QtWidgets.QLabel(self.libraryPage)
        self.libraryLabel.setGeometry(QtCore.QRect(40, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.libraryLabel.setFont(font)
        self.libraryLabel.setStyleSheet("color: rgb(255,255,255);")
        self.libraryLabel.setObjectName("libraryLabel")
        self.importButton = QtWidgets.QPushButton(self.libraryPage)
        self.importButton.setGeometry(QtCore.QRect(470, 50, 81, 20))
        self.importButton.setMinimumSize(QtCore.QSize(81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.importButton.setFont(font)
        self.importButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.importButton.setStyleSheet("QPushButton {    \n"
"    border: rgb(255,255,255);\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(75,166,255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(51, 59, 73);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(33, 37, 43);\n"
"}")
        self.importButton.setDefault(True)
        self.importButton.setObjectName("importButton")
        self.libraryLine = QtWidgets.QFrame(self.libraryPage)
        self.libraryLine.setGeometry(QtCore.QRect(40, 70, 511, 21))
        self.libraryLine.setStyleSheet("color: rgb(27, 29, 35)")
        self.libraryLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.libraryLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.libraryLine.setObjectName("libraryLine")
        self.imageListView = QtWidgets.QListView(self.libraryPage)
        self.imageListView.setGeometry(QtCore.QRect(40, 90, 511, 351))
        self.imageListView.setMinimumSize(QtCore.QSize(511, 311))
        self.imageListView.setMaximumSize(QtCore.QSize(99999, 99999))
        self.imageListView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageListView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.imageListView.setAutoScrollMargin(16)
        self.imageListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.imageListView.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.imageListView.setResizeMode(QtWidgets.QListView.Adjust)
        self.imageListView.setViewMode(QtWidgets.QListView.IconMode)
        self.imageListView.setUniformItemSizes(True)
        self.imageListView.setObjectName("imageListView")
        self.importButton.raise_()
        self.libraryLineEdit.raise_()
        self.libraryLabel.raise_()
        self.libraryLine.raise_()
        self.imageListView.raise_()
        self.stackedWidget.addWidget(self.libraryPage)
        self.classicPage = QtWidgets.QWidget()
        self.classicPage.setObjectName("classicPage")
        self.mainImageLabel = QtWidgets.QLabel(self.classicPage)
        self.mainImageLabel.setGeometry(QtCore.QRect(40, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mainImageLabel.setFont(font)
        self.mainImageLabel.setStyleSheet("color: rgb(255,255,255);")
        self.mainImageLabel.setObjectName("mainImageLabel")
        self.mainImageLineEdit = QtWidgets.QLineEdit(self.classicPage)
        self.mainImageLineEdit.setGeometry(QtCore.QRect(110, 20, 441, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mainImageLineEdit.setFont(font)
        self.mainImageLineEdit.setStyleSheet("QLineEdit {    \n"
"    border: none;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5;\n"
"}")
        self.mainImageLineEdit.setObjectName("mainImageLineEdit")
        self.classicButton = QtWidgets.QPushButton(self.classicPage)
        self.classicButton.setGeometry(QtCore.QRect(470, 50, 81, 20))
        self.classicButton.setMinimumSize(QtCore.QSize(81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.classicButton.setFont(font)
        self.classicButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.classicButton.setStyleSheet("QPushButton {    \n"
"    border: rgb(255,255,255);\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(75,166,255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(51, 59, 73);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(33, 37, 43);\n"
"}")
        self.classicButton.setDefault(True)
        self.classicButton.setObjectName("classicButton")
        self.classicLine = QtWidgets.QFrame(self.classicPage)
        self.classicLine.setGeometry(QtCore.QRect(40, 70, 511, 21))
        self.classicLine.setStyleSheet("color: rgb(27, 29, 35)")
        self.classicLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.classicLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.classicLine.setObjectName("classicLine")
        self.stackedWidget.addWidget(self.classicPage)
        self.partialPage = QtWidgets.QWidget()
        self.partialPage.setObjectName("partialPage")
        self.importProgressBar = QtWidgets.QProgressBar(self.partialPage)
        self.importProgressBar.setGeometry(QtCore.QRect(500, 410, 81, 20))
        self.importProgressBar.setMinimumSize(QtCore.QSize(81, 20))
        self.importProgressBar.setStyleSheet("QProgressBar {\n"
"    color: rgb(255,255,255);\n"
"     border-radius: 5px;\n"
"     background-color: rgb(27, 29, 35);\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     border-radius: 5px;\n"
"     background-color: rgb(75,166,255);\n"
" }")
        self.importProgressBar.setProperty("value", 24)
        self.importProgressBar.setTextVisible(False)
        self.importProgressBar.setObjectName("importProgressBar")
        self.stackedWidget.addWidget(self.partialPage)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.libraryTabButton.setText(_translate("MainWindow", "Bibliothek"))
        self.classicTabButton.setText(_translate("MainWindow", "Mosaic erstellen"))
        self.partialTabButton.setText(_translate("MainWindow", "Teil-Mosaic erstellen"))
        self.libraryLineEdit.setText(_translate("MainWindow", "D:\\Projekt\\Uni\\Medienverarbeitung\\res\\out"))
        self.libraryLabel.setText(_translate("MainWindow", "Bibliothek"))
        self.importButton.setText(_translate("MainWindow", "importieren"))
        self.mainImageLabel.setText(_translate("MainWindow", "Bild"))
        self.mainImageLineEdit.setText(_translate("MainWindow", "D:\\Projekt\\Uni\\Medienverarbeitung\\res\\input.png"))
        self.classicButton.setText(_translate("MainWindow", "erstellen"))

