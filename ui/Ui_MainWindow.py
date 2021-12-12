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
"    color: rgb(255,255,255);\n"
"    text-align: left;;\n"
"    padding-left: 20px;\n"
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
"    padding-left: 20px;\n"
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
"    color: rgb(255,255,255);\n"
"    text-align: left;;\n"
"    padding-left: 20px;\n"
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
        self.importButton.setGeometry(QtCore.QRect(460, 50, 91, 20))
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
        self.imageListView.setGeometry(QtCore.QRect(40, 90, 511, 311))
        self.imageListView.setMinimumSize(QtCore.QSize(511, 311))
        self.imageListView.setMaximumSize(QtCore.QSize(99999, 99999))
        self.imageListView.setStyleSheet("\n"
"QScrollBar:vertical {\n"
"     border-radius: 5px;\n"
"     background-color: rgb(27, 29, 35);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(75,166,255);\n"
"    border-radius: 5px;\n"
"}")
        self.imageListView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageListView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.imageListView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.imageListView.setAutoScrollMargin(16)
        self.imageListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.imageListView.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.imageListView.setResizeMode(QtWidgets.QListView.Adjust)
        self.imageListView.setViewMode(QtWidgets.QListView.IconMode)
        self.imageListView.setUniformItemSizes(True)
        self.imageListView.setObjectName("imageListView")
        self.importProgressBar = QtWidgets.QProgressBar(self.libraryPage)
        self.importProgressBar.setGeometry(QtCore.QRect(460, 50, 91, 20))
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
        self.importProgressBar.setProperty("value", 50)
        self.importProgressBar.setTextVisible(False)
        self.importProgressBar.setObjectName("importProgressBar")
        self.deleteLibraryButton = QtWidgets.QPushButton(self.libraryPage)
        self.deleteLibraryButton.setGeometry(QtCore.QRect(460, 420, 91, 20))
        self.deleteLibraryButton.setMinimumSize(QtCore.QSize(81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deleteLibraryButton.setFont(font)
        self.deleteLibraryButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteLibraryButton.setStyleSheet("QPushButton {    \n"
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
        self.deleteLibraryButton.setDefault(True)
        self.deleteLibraryButton.setObjectName("deleteLibraryButton")
        self.faceDetectionCheckBox = QtWidgets.QCheckBox(self.libraryPage)
        self.faceDetectionCheckBox.setGeometry(QtCore.QRect(40, 50, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.faceDetectionCheckBox.setFont(font)
        self.faceDetectionCheckBox.setStyleSheet("QCheckBox{\n"
"    color: rgb(255,255,255);\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"     border-radius: 2px;\n"
"     background-color: rgb(27, 29, 35);\n"
"    border: 1px solid rgb(27, 29, 35);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"     border-radius: 2px;\n"
"     background-color: rgb(75,166,255);\n"
"    border: 1px solid rgb(27, 29, 35);\n"
"}")
        self.faceDetectionCheckBox.setChecked(False)
        self.faceDetectionCheckBox.setObjectName("faceDetectionCheckBox")
        self.minNeighborsLabel = QtWidgets.QLabel(self.libraryPage)
        self.minNeighborsLabel.setGeometry(QtCore.QRect(200, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.minNeighborsLabel.setFont(font)
        self.minNeighborsLabel.setStyleSheet("color: rgb(255,255,255);")
        self.minNeighborsLabel.setObjectName("minNeighborsLabel")
        self.minNeighborsLineEdit = QtWidgets.QLineEdit(self.libraryPage)
        self.minNeighborsLineEdit.setGeometry(QtCore.QRect(290, 50, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.minNeighborsLineEdit.setFont(font)
        self.minNeighborsLineEdit.setStyleSheet("QLineEdit {    \n"
"    border: none;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5;\n"
"}")
        self.minNeighborsLineEdit.setObjectName("minNeighborsLineEdit")
        self.importButton.raise_()
        self.libraryLineEdit.raise_()
        self.libraryLabel.raise_()
        self.libraryLine.raise_()
        self.imageListView.raise_()
        self.importProgressBar.raise_()
        self.deleteLibraryButton.raise_()
        self.faceDetectionCheckBox.raise_()
        self.minNeighborsLabel.raise_()
        self.minNeighborsLineEdit.raise_()
        self.stackedWidget.addWidget(self.libraryPage)
        self.classicPage = QtWidgets.QWidget()
        self.classicPage.setObjectName("classicPage")
        self.mosaicImageLineEdit = QtWidgets.QLineEdit(self.classicPage)
        self.mosaicImageLineEdit.setGeometry(QtCore.QRect(150, 50, 401, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mosaicImageLineEdit.setFont(font)
        self.mosaicImageLineEdit.setStyleSheet("QLineEdit {    \n"
"    border: none;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5;\n"
"}")
        self.mosaicImageLineEdit.setObjectName("mosaicImageLineEdit")
        self.classicButton = QtWidgets.QPushButton(self.classicPage)
        self.classicButton.setGeometry(QtCore.QRect(460, 250, 91, 20))
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
        self.classicProgressBar = QtWidgets.QProgressBar(self.classicPage)
        self.classicProgressBar.setGeometry(QtCore.QRect(460, 250, 91, 20))
        self.classicProgressBar.setMinimumSize(QtCore.QSize(81, 20))
        self.classicProgressBar.setStyleSheet("QProgressBar {\n"
"    color: rgb(255,255,255);\n"
"     border-radius: 5px;\n"
"     background-color: rgb(27, 29, 35);\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     border-radius: 5px;\n"
"     background-color: rgb(75,166,255);\n"
" }")
        self.classicProgressBar.setProperty("value", 50)
        self.classicProgressBar.setTextVisible(False)
        self.classicProgressBar.setObjectName("classicProgressBar")
        self.mosaicHeightLineEdit = QtWidgets.QLineEdit(self.classicPage)
        self.mosaicHeightLineEdit.setGeometry(QtCore.QRect(150, 110, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mosaicHeightLineEdit.setFont(font)
        self.mosaicHeightLineEdit.setStyleSheet("QLineEdit {    \n"
"    border: none;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5;\n"
"}")
        self.mosaicHeightLineEdit.setObjectName("mosaicHeightLineEdit")
        self.mosaicWidthLineEdit = QtWidgets.QLineEdit(self.classicPage)
        self.mosaicWidthLineEdit.setGeometry(QtCore.QRect(150, 80, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mosaicWidthLineEdit.setFont(font)
        self.mosaicWidthLineEdit.setStyleSheet("QLineEdit {    \n"
"    border: none;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5;\n"
"}")
        self.mosaicWidthLineEdit.setClearButtonEnabled(False)
        self.mosaicWidthLineEdit.setObjectName("mosaicWidthLineEdit")
        self.mosaicLabel = QtWidgets.QLabel(self.classicPage)
        self.mosaicLabel.setGeometry(QtCore.QRect(40, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mosaicLabel.setFont(font)
        self.mosaicLabel.setStyleSheet("color: rgb(255,255,255);")
        self.mosaicLabel.setObjectName("mosaicLabel")
        self.mosaicWidthLabel = QtWidgets.QLabel(self.classicPage)
        self.mosaicWidthLabel.setGeometry(QtCore.QRect(60, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mosaicWidthLabel.setFont(font)
        self.mosaicWidthLabel.setStyleSheet("color: rgb(255,255,255);")
        self.mosaicWidthLabel.setObjectName("mosaicWidthLabel")
        self.mosaicHeightLabel = QtWidgets.QLabel(self.classicPage)
        self.mosaicHeightLabel.setGeometry(QtCore.QRect(60, 110, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mosaicHeightLabel.setFont(font)
        self.mosaicHeightLabel.setStyleSheet("color: rgb(255,255,255);")
        self.mosaicHeightLabel.setObjectName("mosaicHeightLabel")
        self.keepAspectRatioCheckBox = QtWidgets.QCheckBox(self.classicPage)
        self.keepAspectRatioCheckBox.setGeometry(QtCore.QRect(60, 140, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.keepAspectRatioCheckBox.setFont(font)
        self.keepAspectRatioCheckBox.setStyleSheet("QCheckBox{\n"
"    color: rgb(255,255,255);\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"     border-radius: 2px;\n"
"     background-color: rgb(27, 29, 35);\n"
"    border: 1px solid rgb(27, 29, 35);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"     border-radius: 2px;\n"
"     background-color: rgb(75,166,255);\n"
"    border: 1px solid rgb(27, 29, 35);\n"
"}")
        self.keepAspectRatioCheckBox.setChecked(True)
        self.keepAspectRatioCheckBox.setObjectName("keepAspectRatioCheckBox")
        self.elementLabel = QtWidgets.QLabel(self.classicPage)
        self.elementLabel.setGeometry(QtCore.QRect(40, 180, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.elementLabel.setFont(font)
        self.elementLabel.setStyleSheet("color: rgb(255,255,255);")
        self.elementLabel.setObjectName("elementLabel")
        self.mosaicImageLabel = QtWidgets.QLabel(self.classicPage)
        self.mosaicImageLabel.setGeometry(QtCore.QRect(60, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mosaicImageLabel.setFont(font)
        self.mosaicImageLabel.setStyleSheet("color: rgb(255,255,255);")
        self.mosaicImageLabel.setObjectName("mosaicImageLabel")
        self.elementSizeLabel = QtWidgets.QLabel(self.classicPage)
        self.elementSizeLabel.setGeometry(QtCore.QRect(60, 210, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.elementSizeLabel.setFont(font)
        self.elementSizeLabel.setStyleSheet("color: rgb(255,255,255);")
        self.elementSizeLabel.setObjectName("elementSizeLabel")
        self.elementSizeComboBox = QtWidgets.QComboBox(self.classicPage)
        self.elementSizeComboBox.setGeometry(QtCore.QRect(150, 210, 53, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.elementSizeComboBox.setFont(font)
        self.elementSizeComboBox.setStyleSheet("QComboBox {    \n"
"    border: none;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5;\n"
"}")
        self.elementSizeComboBox.setFrame(True)
        self.elementSizeComboBox.setObjectName("elementSizeComboBox")
        self.elementSizeComboBox.addItem("")
        self.elementSizeComboBox.addItem("")
        self.elementSizeComboBox.addItem("")
        self.elementSizeComboBox.addItem("")
        self.stackedWidget.addWidget(self.classicPage)
        self.partialPage = QtWidgets.QWidget()
        self.partialPage.setObjectName("partialPage")
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
        self.partialTabButton.setText(_translate("MainWindow", "WIP . . ."))
        self.libraryLineEdit.setText(_translate("MainWindow", "D:\\Projekt\\Uni\\Medienverarbeitung\\res\\out"))
        self.libraryLabel.setText(_translate("MainWindow", "Bibliothek"))
        self.importButton.setText(_translate("MainWindow", "importieren"))
        self.deleteLibraryButton.setText(_translate("MainWindow", "Bibliothek Löschen"))
        self.faceDetectionCheckBox.setText(_translate("MainWindow", "Auf Gesichter zuschneiden"))
        self.minNeighborsLabel.setText(_translate("MainWindow", "Schwellenwert:"))
        self.minNeighborsLineEdit.setText(_translate("MainWindow", "30"))
        self.mosaicImageLineEdit.setText(_translate("MainWindow", "D:\\Projekt\\Uni\\Medienverarbeitung\\res\\input.png"))
        self.classicButton.setText(_translate("MainWindow", "erstellen"))
        self.mosaicHeightLineEdit.setText(_translate("MainWindow", "144"))
        self.mosaicWidthLineEdit.setText(_translate("MainWindow", "256"))
        self.mosaicLabel.setText(_translate("MainWindow", "Mosaik:"))
        self.mosaicWidthLabel.setText(_translate("MainWindow", "Breite:"))
        self.mosaicHeightLabel.setText(_translate("MainWindow", "Höhe:"))
        self.keepAspectRatioCheckBox.setText(_translate("MainWindow", "Höhe automatisch bestimmen"))
        self.elementLabel.setText(_translate("MainWindow", "Elemente:"))
        self.mosaicImageLabel.setText(_translate("MainWindow", "Bild:"))
        self.elementSizeLabel.setText(_translate("MainWindow", "Breite/Höhe:"))
        self.elementSizeComboBox.setItemText(0, _translate("MainWindow", "32"))
        self.elementSizeComboBox.setItemText(1, _translate("MainWindow", "64"))
        self.elementSizeComboBox.setItemText(2, _translate("MainWindow", "128"))
        self.elementSizeComboBox.setItemText(3, _translate("MainWindow", "256"))

