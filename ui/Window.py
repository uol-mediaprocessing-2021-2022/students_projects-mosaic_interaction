import subprocess
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow

import mosaic
from Database import Database
from mosaic import *
from ui.Ui_MainWindow import Ui_MainWindow


# pyuic5 -o ui/Ui_MainWindow.py main_window.ui
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.imageListViewModel = QtGui.QStandardItemModel()
        self.imageListView.setModel(self.imageListViewModel)

        self.libraryTabButton.clicked.connect(self.bibTabBtnListiner)
        self.classicTabButton.clicked.connect(self.classicTabBtnListiner)
        self.partialTabButton.clicked.connect(self.partialTabBtnListiner)

        self.importButton.clicked.connect(self.importBtnListener)

        self.classicButton.clicked.connect(self.classicBtnListener)

        self.db = Database()
        self.showImageLibrary(self.db.getAllCroppedImages())

    def bibTabBtnListiner(self):
        self.stackedWidget.setCurrentIndex(0)

    def classicTabBtnListiner(self):
        self.stackedWidget.setCurrentIndex(1)

    def partialTabBtnListiner(self):
        self.stackedWidget.setCurrentIndex(2)

    def importBtnListener(self):
        importPath = self.libraryLineEdit.text()

        if importPath.endswith(".mp4"):
            subprocess.run("ffmpeg -i " + importPath + " -vf fps=1/5 bib/out%d.png")
            self.db.importAllImages("bib")

        else:
            self.db.importAllImages(importPath)

        self.showImageLibrary(self.db.getAllCroppedImages())

    def showImageLibrary(self, cursor):
        for img_arr in cursor:
            img = self.db.decode(img_arr[0])

            image = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap.fromImage(image))

            item = QtGui.QStandardItem()
            item.setIcon(icon)

            self.imageListViewModel.appendRow(item)

    def classicBtnListener(self):
        img = destroyImgFix(rgbImport(self.mainImageLineEdit.text()))
        result = createMosaic(img, np.array(self.db.getAllColorValuesWithIDs().fetchall()), self.db)
        cv2.imwrite("output.jpeg", result)

        imageViewerFromCommandLine = {'linux': 'xdg-open',
                                      'win32': 'explorer',
                                      'darwin': 'open'}[sys.platform]
        subprocess.run([imageViewerFromCommandLine, "output.jpeg"])

