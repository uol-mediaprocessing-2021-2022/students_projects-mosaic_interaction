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
        self.mosaicTabButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.mosaicTabButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mosaicTabButton.setFont(font)
        self.mosaicTabButton.setStyleSheet("QPushButton {    \n"
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
        self.mosaicTabButton.setCheckable(True)
        self.mosaicTabButton.setAutoExclusive(True)
        self.mosaicTabButton.setObjectName("mosaicTabButton")
        self.verticalLayout.addWidget(self.mosaicTabButton)
        self.detailMosaicTabButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.detailMosaicTabButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.detailMosaicTabButton.setFont(font)
        self.detailMosaicTabButton.setStyleSheet("QPushButton {    \n"
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
        self.detailMosaicTabButton.setCheckable(True)
        self.detailMosaicTabButton.setAutoExclusive(True)
        self.detailMosaicTabButton.setFlat(True)
        self.detailMosaicTabButton.setObjectName("detailMosaicTabButton")
        self.verticalLayout.addWidget(self.detailMosaicTabButton)
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
        self.mosaicPage = QtWidgets.QWidget()
        self.mosaicPage.setObjectName("mosaicPage")
        self.mosaicImageLineEdit = QtWidgets.QLineEdit(self.mosaicPage)
        self.mosaicImageLineEdit.setGeometry(QtCore.QRect(160, 50, 390, 20))
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
        self.mosaicButton = QtWidgets.QPushButton(self.mosaicPage)
        self.mosaicButton.setGeometry(QtCore.QRect(460, 420, 91, 20))
        self.mosaicButton.setMinimumSize(QtCore.QSize(81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mosaicButton.setFont(font)
        self.mosaicButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mosaicButton.setStyleSheet("QPushButton {    \n"
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
        self.mosaicButton.setDefault(True)
        self.mosaicButton.setObjectName("mosaicButton")
        self.mosaicProgressBar = QtWidgets.QProgressBar(self.mosaicPage)
        self.mosaicProgressBar.setGeometry(QtCore.QRect(460, 420, 91, 20))
        self.mosaicProgressBar.setMinimumSize(QtCore.QSize(81, 20))
        self.mosaicProgressBar.setStyleSheet("QProgressBar {\n"
"    color: rgb(255,255,255);\n"
"     border-radius: 5px;\n"
"     background-color: rgb(27, 29, 35);\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     border-radius: 5px;\n"
"     background-color: rgb(75,166,255);\n"
" }")
        self.mosaicProgressBar.setProperty("value", 50)
        self.mosaicProgressBar.setTextVisible(False)
        self.mosaicProgressBar.setObjectName("mosaicProgressBar")
        self.mosaicHeightLineEdit = QtWidgets.QLineEdit(self.mosaicPage)
        self.mosaicHeightLineEdit.setGeometry(QtCore.QRect(160, 110, 31, 21))
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
        self.mosaicWidthLineEdit = QtWidgets.QLineEdit(self.mosaicPage)
        self.mosaicWidthLineEdit.setGeometry(QtCore.QRect(160, 80, 31, 21))
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
        self.mosaicLabel = QtWidgets.QLabel(self.mosaicPage)
        self.mosaicLabel.setGeometry(QtCore.QRect(40, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mosaicLabel.setFont(font)
        self.mosaicLabel.setStyleSheet("color: rgb(255,255,255);")
        self.mosaicLabel.setObjectName("mosaicLabel")
        self.mosaicWidthLabel = QtWidgets.QLabel(self.mosaicPage)
        self.mosaicWidthLabel.setGeometry(QtCore.QRect(60, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mosaicWidthLabel.setFont(font)
        self.mosaicWidthLabel.setStyleSheet("color: rgb(255,255,255);")
        self.mosaicWidthLabel.setObjectName("mosaicWidthLabel")
        self.mosaicHeightLabel = QtWidgets.QLabel(self.mosaicPage)
        self.mosaicHeightLabel.setGeometry(QtCore.QRect(60, 110, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mosaicHeightLabel.setFont(font)
        self.mosaicHeightLabel.setStyleSheet("color: rgb(255,255,255);")
        self.mosaicHeightLabel.setObjectName("mosaicHeightLabel")
        self.mosaicKeepAspectRatioCheckBox = QtWidgets.QCheckBox(self.mosaicPage)
        self.mosaicKeepAspectRatioCheckBox.setGeometry(QtCore.QRect(60, 140, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mosaicKeepAspectRatioCheckBox.setFont(font)
        self.mosaicKeepAspectRatioCheckBox.setStyleSheet("QCheckBox{\n"
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
        self.mosaicKeepAspectRatioCheckBox.setChecked(True)
        self.mosaicKeepAspectRatioCheckBox.setObjectName("mosaicKeepAspectRatioCheckBox")
        self.mosaicElementLabel = QtWidgets.QLabel(self.mosaicPage)
        self.mosaicElementLabel.setGeometry(QtCore.QRect(40, 200, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mosaicElementLabel.setFont(font)
        self.mosaicElementLabel.setStyleSheet("color: rgb(255,255,255);")
        self.mosaicElementLabel.setObjectName("mosaicElementLabel")
        self.mosaicImageLabel = QtWidgets.QLabel(self.mosaicPage)
        self.mosaicImageLabel.setGeometry(QtCore.QRect(60, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mosaicImageLabel.setFont(font)
        self.mosaicImageLabel.setStyleSheet("color: rgb(255,255,255);")
        self.mosaicImageLabel.setObjectName("mosaicImageLabel")
        self.mosaicElementSizeLabel = QtWidgets.QLabel(self.mosaicPage)
        self.mosaicElementSizeLabel.setGeometry(QtCore.QRect(60, 230, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mosaicElementSizeLabel.setFont(font)
        self.mosaicElementSizeLabel.setStyleSheet("color: rgb(255,255,255);")
        self.mosaicElementSizeLabel.setObjectName("mosaicElementSizeLabel")
        self.mosaicElementSizeComboBox = QtWidgets.QComboBox(self.mosaicPage)
        self.mosaicElementSizeComboBox.setGeometry(QtCore.QRect(160, 230, 53, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mosaicElementSizeComboBox.setFont(font)
        self.mosaicElementSizeComboBox.setStyleSheet("QComboBox {    \n"
"    border: none;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5;\n"
"}")
        self.mosaicElementSizeComboBox.setFrame(True)
        self.mosaicElementSizeComboBox.setObjectName("mosaicElementSizeComboBox")
        self.mosaicElementSizeComboBox.addItem("")
        self.mosaicElementSizeComboBox.addItem("")
        self.mosaicElementSizeComboBox.addItem("")
        self.mosaicElementSizeComboBox.addItem("")
        self.mosaicElementSizeComboBox.addItem("")
        self.mosaicTransparencyLabel = QtWidgets.QLabel(self.mosaicPage)
        self.mosaicTransparencyLabel.setGeometry(QtCore.QRect(60, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mosaicTransparencyLabel.setFont(font)
        self.mosaicTransparencyLabel.setStyleSheet("color: rgb(255,255,255);")
        self.mosaicTransparencyLabel.setObjectName("mosaicTransparencyLabel")
        self.mosaicTransparencySlider = QtWidgets.QSlider(self.mosaicPage)
        self.mosaicTransparencySlider.setGeometry(QtCore.QRect(150, 170, 160, 21))
        self.mosaicTransparencySlider.setStyleSheet("QSlider {\n"
"    color: rgb(75,166,255);\n"
"}\n"
"QSlider:hover {\n"
"    color: rgb(51, 59, 73);\n"
"}")
        self.mosaicTransparencySlider.setMaximum(100)
        self.mosaicTransparencySlider.setOrientation(QtCore.Qt.Horizontal)
        self.mosaicTransparencySlider.setObjectName("mosaicTransparencySlider")
        self.stackedWidget.addWidget(self.mosaicPage)
        self.detailMosaicPage = QtWidgets.QWidget()
        self.detailMosaicPage.setObjectName("detailMosaicPage")
        self.detailMosaicImageLineEdit = QtWidgets.QLineEdit(self.detailMosaicPage)
        self.detailMosaicImageLineEdit.setGeometry(QtCore.QRect(160, 50, 390, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicImageLineEdit.setFont(font)
        self.detailMosaicImageLineEdit.setStyleSheet("QLineEdit {    \n"
"    border: none;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5;\n"
"}")
        self.detailMosaicImageLineEdit.setObjectName("detailMosaicImageLineEdit")
        self.detailMosaicWidthLabel = QtWidgets.QLabel(self.detailMosaicPage)
        self.detailMosaicWidthLabel.setGeometry(QtCore.QRect(60, 80, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicWidthLabel.setFont(font)
        self.detailMosaicWidthLabel.setStyleSheet("color: rgb(255,255,255);")
        self.detailMosaicWidthLabel.setObjectName("detailMosaicWidthLabel")
        self.detailMosaicHeightLabel = QtWidgets.QLabel(self.detailMosaicPage)
        self.detailMosaicHeightLabel.setGeometry(QtCore.QRect(60, 110, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicHeightLabel.setFont(font)
        self.detailMosaicHeightLabel.setStyleSheet("color: rgb(255,255,255);")
        self.detailMosaicHeightLabel.setObjectName("detailMosaicHeightLabel")
        self.detailMosaicLabel = QtWidgets.QLabel(self.detailMosaicPage)
        self.detailMosaicLabel.setGeometry(QtCore.QRect(40, 20, 120, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicLabel.setFont(font)
        self.detailMosaicLabel.setStyleSheet("color: rgb(255,255,255);")
        self.detailMosaicLabel.setObjectName("detailMosaicLabel")
        self.detailMosaicKeepAspectRatioCheckBox = QtWidgets.QCheckBox(self.detailMosaicPage)
        self.detailMosaicKeepAspectRatioCheckBox.setGeometry(QtCore.QRect(60, 140, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicKeepAspectRatioCheckBox.setFont(font)
        self.detailMosaicKeepAspectRatioCheckBox.setStyleSheet("QCheckBox{\n"
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
        self.detailMosaicKeepAspectRatioCheckBox.setChecked(True)
        self.detailMosaicKeepAspectRatioCheckBox.setObjectName("detailMosaicKeepAspectRatioCheckBox")
        self.detailMosaicWidthLineEdit = QtWidgets.QLineEdit(self.detailMosaicPage)
        self.detailMosaicWidthLineEdit.setGeometry(QtCore.QRect(160, 80, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicWidthLineEdit.setFont(font)
        self.detailMosaicWidthLineEdit.setStyleSheet("QLineEdit {    \n"
"    border: none;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5;\n"
"}")
        self.detailMosaicWidthLineEdit.setClearButtonEnabled(False)
        self.detailMosaicWidthLineEdit.setObjectName("detailMosaicWidthLineEdit")
        self.detailMosaicImageLabel = QtWidgets.QLabel(self.detailMosaicPage)
        self.detailMosaicImageLabel.setGeometry(QtCore.QRect(60, 50, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicImageLabel.setFont(font)
        self.detailMosaicImageLabel.setStyleSheet("color: rgb(255,255,255);")
        self.detailMosaicImageLabel.setObjectName("detailMosaicImageLabel")
        self.detailMosaicProgressBar = QtWidgets.QProgressBar(self.detailMosaicPage)
        self.detailMosaicProgressBar.setGeometry(QtCore.QRect(460, 420, 91, 20))
        self.detailMosaicProgressBar.setMinimumSize(QtCore.QSize(81, 20))
        self.detailMosaicProgressBar.setStyleSheet("QProgressBar {\n"
"    color: rgb(255,255,255);\n"
"     border-radius: 5px;\n"
"     background-color: rgb(27, 29, 35);\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     border-radius: 5px;\n"
"     background-color: rgb(75,166,255);\n"
" }")
        self.detailMosaicProgressBar.setProperty("value", 50)
        self.detailMosaicProgressBar.setTextVisible(False)
        self.detailMosaicProgressBar.setObjectName("detailMosaicProgressBar")
        self.detailMosaicHeightLineEdit = QtWidgets.QLineEdit(self.detailMosaicPage)
        self.detailMosaicHeightLineEdit.setGeometry(QtCore.QRect(160, 110, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicHeightLineEdit.setFont(font)
        self.detailMosaicHeightLineEdit.setStyleSheet("QLineEdit {    \n"
"    border: none;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5;\n"
"}")
        self.detailMosaicHeightLineEdit.setObjectName("detailMosaicHeightLineEdit")
        self.detailMosaicButton = QtWidgets.QPushButton(self.detailMosaicPage)
        self.detailMosaicButton.setGeometry(QtCore.QRect(460, 420, 91, 20))
        self.detailMosaicButton.setMinimumSize(QtCore.QSize(81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicButton.setFont(font)
        self.detailMosaicButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.detailMosaicButton.setStyleSheet("QPushButton {    \n"
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
        self.detailMosaicButton.setDefault(True)
        self.detailMosaicButton.setObjectName("detailMosaicButton")
        self.detailMosaicElementMinSizeComboBox = QtWidgets.QComboBox(self.detailMosaicPage)
        self.detailMosaicElementMinSizeComboBox.setGeometry(QtCore.QRect(160, 230, 53, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicElementMinSizeComboBox.setFont(font)
        self.detailMosaicElementMinSizeComboBox.setStyleSheet("QComboBox {    \n"
"    border: none;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5;\n"
"}")
        self.detailMosaicElementMinSizeComboBox.setFrame(True)
        self.detailMosaicElementMinSizeComboBox.setObjectName("detailMosaicElementMinSizeComboBox")
        self.detailMosaicElementMinSizeComboBox.addItem("")
        self.detailMosaicElementMinSizeComboBox.addItem("")
        self.detailMosaicElementMinSizeComboBox.addItem("")
        self.detailMosaicElementMinSizeComboBox.addItem("")
        self.detailMosaicElementMinSizeComboBox.addItem("")
        self.detailMosaicElementLabel = QtWidgets.QLabel(self.detailMosaicPage)
        self.detailMosaicElementLabel.setGeometry(QtCore.QRect(40, 200, 120, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicElementLabel.setFont(font)
        self.detailMosaicElementLabel.setStyleSheet("color: rgb(255,255,255);")
        self.detailMosaicElementLabel.setObjectName("detailMosaicElementLabel")
        self.detailMosaicElementMinSizeLabel = QtWidgets.QLabel(self.detailMosaicPage)
        self.detailMosaicElementMinSizeLabel.setGeometry(QtCore.QRect(60, 230, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicElementMinSizeLabel.setFont(font)
        self.detailMosaicElementMinSizeLabel.setStyleSheet("color: rgb(255,255,255);")
        self.detailMosaicElementMinSizeLabel.setObjectName("detailMosaicElementMinSizeLabel")
        self.detailMosaicElementMaxSizeComboBox = QtWidgets.QComboBox(self.detailMosaicPage)
        self.detailMosaicElementMaxSizeComboBox.setGeometry(QtCore.QRect(160, 260, 53, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicElementMaxSizeComboBox.setFont(font)
        self.detailMosaicElementMaxSizeComboBox.setStyleSheet("QComboBox {    \n"
"    border: none;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5;\n"
"}")
        self.detailMosaicElementMaxSizeComboBox.setFrame(True)
        self.detailMosaicElementMaxSizeComboBox.setObjectName("detailMosaicElementMaxSizeComboBox")
        self.detailMosaicElementMaxSizeComboBox.addItem("")
        self.detailMosaicElementMaxSizeComboBox.addItem("")
        self.detailMosaicElementMaxSizeComboBox.addItem("")
        self.detailMosaicElementMaxSizeComboBox.addItem("")
        self.detailMosaicElementMaxSizeComboBox.addItem("")
        self.detailMosaicElementMaxSizeLabel = QtWidgets.QLabel(self.detailMosaicPage)
        self.detailMosaicElementMaxSizeLabel.setGeometry(QtCore.QRect(60, 260, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicElementMaxSizeLabel.setFont(font)
        self.detailMosaicElementMaxSizeLabel.setStyleSheet("color: rgb(255,255,255);")
        self.detailMosaicElementMaxSizeLabel.setObjectName("detailMosaicElementMaxSizeLabel")
        self.detailMosaicElementAllowedDeviationLabel = QtWidgets.QLabel(self.detailMosaicPage)
        self.detailMosaicElementAllowedDeviationLabel.setGeometry(QtCore.QRect(60, 290, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicElementAllowedDeviationLabel.setFont(font)
        self.detailMosaicElementAllowedDeviationLabel.setStyleSheet("color: rgb(255,255,255);")
        self.detailMosaicElementAllowedDeviationLabel.setObjectName("detailMosaicElementAllowedDeviationLabel")
        self.detailMosaicElementAllowedDeviationLineEdit = QtWidgets.QLineEdit(self.detailMosaicPage)
        self.detailMosaicElementAllowedDeviationLineEdit.setGeometry(QtCore.QRect(160, 290, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicElementAllowedDeviationLineEdit.setFont(font)
        self.detailMosaicElementAllowedDeviationLineEdit.setStyleSheet("QLineEdit {    \n"
"    border: none;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5;\n"
"}")
        self.detailMosaicElementAllowedDeviationLineEdit.setObjectName("detailMosaicElementAllowedDeviationLineEdit")
        self.detailMosaicElementAllowedDeviationPercentageLabel = QtWidgets.QLabel(self.detailMosaicPage)
        self.detailMosaicElementAllowedDeviationPercentageLabel.setGeometry(QtCore.QRect(190, 290, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicElementAllowedDeviationPercentageLabel.setFont(font)
        self.detailMosaicElementAllowedDeviationPercentageLabel.setStyleSheet("color: rgb(255,255,255);")
        self.detailMosaicElementAllowedDeviationPercentageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.detailMosaicElementAllowedDeviationPercentageLabel.setObjectName("detailMosaicElementAllowedDeviationPercentageLabel")
        self.detailMosaicUseEdgedetectionCheckBox = QtWidgets.QCheckBox(self.detailMosaicPage)
        self.detailMosaicUseEdgedetectionCheckBox.setGeometry(QtCore.QRect(60, 320, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicUseEdgedetectionCheckBox.setFont(font)
        self.detailMosaicUseEdgedetectionCheckBox.setStyleSheet("QCheckBox{\n"
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
        self.detailMosaicUseEdgedetectionCheckBox.setChecked(True)
        self.detailMosaicUseEdgedetectionCheckBox.setObjectName("detailMosaicUseEdgedetectionCheckBox")
        self.detailMosaicShowEdgesButton = QtWidgets.QPushButton(self.detailMosaicPage)
        self.detailMosaicShowEdgesButton.setGeometry(QtCore.QRect(60, 350, 91, 20))
        self.detailMosaicShowEdgesButton.setMinimumSize(QtCore.QSize(81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicShowEdgesButton.setFont(font)
        self.detailMosaicShowEdgesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.detailMosaicShowEdgesButton.setStyleSheet("QPushButton {    \n"
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
        self.detailMosaicShowEdgesButton.setDefault(True)
        self.detailMosaicShowEdgesButton.setObjectName("detailMosaicShowEdgesButton")
        self.detailMosaicTransparencySlider = QtWidgets.QSlider(self.detailMosaicPage)
        self.detailMosaicTransparencySlider.setGeometry(QtCore.QRect(150, 170, 160, 21))
        self.detailMosaicTransparencySlider.setStyleSheet("QSlider {\n"
"    color: rgb(75,166,255);\n"
"}\n"
"QSlider:hover {\n"
"    color: rgb(51, 59, 73);\n"
"}")
        self.detailMosaicTransparencySlider.setMaximum(100)
        self.detailMosaicTransparencySlider.setOrientation(QtCore.Qt.Horizontal)
        self.detailMosaicTransparencySlider.setObjectName("detailMosaicTransparencySlider")
        self.detailMosaicTransparencyLabel = QtWidgets.QLabel(self.detailMosaicPage)
        self.detailMosaicTransparencyLabel.setGeometry(QtCore.QRect(60, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detailMosaicTransparencyLabel.setFont(font)
        self.detailMosaicTransparencyLabel.setStyleSheet("color: rgb(255,255,255);")
        self.detailMosaicTransparencyLabel.setObjectName("detailMosaicTransparencyLabel")
        self.detailMosaicElementAllowedDeviationPercentageLabel.raise_()
        self.detailMosaicButton.raise_()
        self.detailMosaicImageLineEdit.raise_()
        self.detailMosaicWidthLabel.raise_()
        self.detailMosaicHeightLabel.raise_()
        self.detailMosaicLabel.raise_()
        self.detailMosaicKeepAspectRatioCheckBox.raise_()
        self.detailMosaicWidthLineEdit.raise_()
        self.detailMosaicImageLabel.raise_()
        self.detailMosaicProgressBar.raise_()
        self.detailMosaicHeightLineEdit.raise_()
        self.detailMosaicElementMinSizeComboBox.raise_()
        self.detailMosaicElementLabel.raise_()
        self.detailMosaicElementMinSizeLabel.raise_()
        self.detailMosaicElementMaxSizeComboBox.raise_()
        self.detailMosaicElementMaxSizeLabel.raise_()
        self.detailMosaicElementAllowedDeviationLabel.raise_()
        self.detailMosaicElementAllowedDeviationLineEdit.raise_()
        self.detailMosaicUseEdgedetectionCheckBox.raise_()
        self.detailMosaicShowEdgesButton.raise_()
        self.detailMosaicTransparencySlider.raise_()
        self.detailMosaicTransparencyLabel.raise_()
        self.stackedWidget.addWidget(self.detailMosaicPage)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.libraryTabButton.setText(_translate("MainWindow", "Bibliothek"))
        self.mosaicTabButton.setText(_translate("MainWindow", "Mosaic erstellen"))
        self.detailMosaicTabButton.setText(_translate("MainWindow", "Detail-Mosaik erstellen"))
        self.libraryLineEdit.setText(_translate("MainWindow", "D:\\Projekt\\Uni\\Medienverarbeitung\\res\\out"))
        self.libraryLabel.setText(_translate("MainWindow", "Bibliothek"))
        self.importButton.setText(_translate("MainWindow", "importieren"))
        self.deleteLibraryButton.setText(_translate("MainWindow", "Bibliothek Löschen"))
        self.faceDetectionCheckBox.setText(_translate("MainWindow", "Auf Gesichter zuschneiden"))
        self.minNeighborsLabel.setText(_translate("MainWindow", "Schwellenwert:"))
        self.minNeighborsLineEdit.setText(_translate("MainWindow", "30"))
        self.mosaicImageLineEdit.setText(_translate("MainWindow", "D:\\Projekt\\Uni\\Medienverarbeitung\\res\\input.png"))
        self.mosaicButton.setText(_translate("MainWindow", "erstellen"))
        self.mosaicHeightLineEdit.setText(_translate("MainWindow", "144"))
        self.mosaicWidthLineEdit.setText(_translate("MainWindow", "256"))
        self.mosaicLabel.setText(_translate("MainWindow", "Mosaik:"))
        self.mosaicWidthLabel.setText(_translate("MainWindow", "Breite:"))
        self.mosaicHeightLabel.setText(_translate("MainWindow", "Höhe:"))
        self.mosaicKeepAspectRatioCheckBox.setText(_translate("MainWindow", "Höhe automatisch bestimmen"))
        self.mosaicElementLabel.setText(_translate("MainWindow", "Elemente:"))
        self.mosaicImageLabel.setText(_translate("MainWindow", "Bild:"))
        self.mosaicElementSizeLabel.setText(_translate("MainWindow", "Breite/Höhe:"))
        self.mosaicElementSizeComboBox.setItemText(0, _translate("MainWindow", "32"))
        self.mosaicElementSizeComboBox.setItemText(1, _translate("MainWindow", "64"))
        self.mosaicElementSizeComboBox.setItemText(2, _translate("MainWindow", "128"))
        self.mosaicElementSizeComboBox.setItemText(3, _translate("MainWindow", "256"))
        self.mosaicElementSizeComboBox.setItemText(4, _translate("MainWindow", "512"))
        self.mosaicTransparencyLabel.setText(_translate("MainWindow", "Original-Bild:"))
        self.detailMosaicImageLineEdit.setText(_translate("MainWindow", "D:\\Projekt\\Uni\\Medienverarbeitung\\res\\input.png"))
        self.detailMosaicWidthLabel.setText(_translate("MainWindow", "Breite:"))
        self.detailMosaicHeightLabel.setText(_translate("MainWindow", "Höhe:"))
        self.detailMosaicLabel.setText(_translate("MainWindow", "Detail-Mosaik:"))
        self.detailMosaicKeepAspectRatioCheckBox.setText(_translate("MainWindow", "Höhe automatisch bestimmen"))
        self.detailMosaicWidthLineEdit.setText(_translate("MainWindow", "256"))
        self.detailMosaicImageLabel.setText(_translate("MainWindow", "Bild:"))
        self.detailMosaicHeightLineEdit.setText(_translate("MainWindow", "144"))
        self.detailMosaicButton.setText(_translate("MainWindow", "erstellen"))
        self.detailMosaicElementMinSizeComboBox.setItemText(0, _translate("MainWindow", "32"))
        self.detailMosaicElementMinSizeComboBox.setItemText(1, _translate("MainWindow", "64"))
        self.detailMosaicElementMinSizeComboBox.setItemText(2, _translate("MainWindow", "128"))
        self.detailMosaicElementMinSizeComboBox.setItemText(3, _translate("MainWindow", "256"))
        self.detailMosaicElementMinSizeComboBox.setItemText(4, _translate("MainWindow", "512"))
        self.detailMosaicElementLabel.setText(_translate("MainWindow", "Elemente:"))
        self.detailMosaicElementMinSizeLabel.setText(_translate("MainWindow", "min. Breite/Höhe:"))
        self.detailMosaicElementMaxSizeComboBox.setCurrentText(_translate("MainWindow", "32"))
        self.detailMosaicElementMaxSizeComboBox.setItemText(0, _translate("MainWindow", "32"))
        self.detailMosaicElementMaxSizeComboBox.setItemText(1, _translate("MainWindow", "64"))
        self.detailMosaicElementMaxSizeComboBox.setItemText(2, _translate("MainWindow", "128"))
        self.detailMosaicElementMaxSizeComboBox.setItemText(3, _translate("MainWindow", "256"))
        self.detailMosaicElementMaxSizeComboBox.setItemText(4, _translate("MainWindow", "512"))
        self.detailMosaicElementMaxSizeLabel.setText(_translate("MainWindow", "max. Breite/Höhe:"))
        self.detailMosaicElementAllowedDeviationLabel.setText(_translate("MainWindow", "erlaubte Abweichung:"))
        self.detailMosaicElementAllowedDeviationLineEdit.setText(_translate("MainWindow", "50"))
        self.detailMosaicElementAllowedDeviationPercentageLabel.setText(_translate("MainWindow", "%"))
        self.detailMosaicUseEdgedetectionCheckBox.setText(_translate("MainWindow", "Kantenerkennung nutzen"))
        self.detailMosaicShowEdgesButton.setText(_translate("MainWindow", "Kanten anzeigen"))
        self.detailMosaicTransparencyLabel.setText(_translate("MainWindow", "Original-Bild:"))

