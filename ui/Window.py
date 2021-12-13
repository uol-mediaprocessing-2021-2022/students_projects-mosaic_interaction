import shutil
import subprocess
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow

from Database import Database
from mosaic import *
from ui.Ui_MainWindow import Ui_MainWindow


# pyuic5 -o ui/Ui_MainWindow.py main_window.ui
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # tab-buttons
        self.libraryTabButton.clicked.connect(self.bibTabBtnListiner)
        self.classicTabButton.clicked.connect(self.classicTabBtnListiner)
        self.partialTabButton.clicked.connect(self.partialTabBtnListiner)

        # library-page
        self.imageListViewModel = QtGui.QStandardItemModel()
        self.imageListView.setModel(self.imageListViewModel)

        self.importProgressBar.setVisible(False)

        self.importButton.clicked.connect(self.importBtnListener)
        self.faceDetectionCheckBox.clicked.connect(self.faceDetectionCheckBoxBtnListiner)

        self.minNeighborsLabel.setVisible(self.faceDetectionCheckBox.isChecked())
        self.minNeighborsLineEdit.setVisible(self.faceDetectionCheckBox.isChecked())

        self.deleteLibraryButton.clicked.connect(self.deleteLibraryBtnListiner)

        # classic-page
        self.classicButton.clicked.connect(self.classicBtnListener)

        self.keepAspectRatioCheckBox.clicked.connect(self.keepAspectRatioCheckBoxBtnListiner)

        self.mosaicHeightLineEdit.setVisible(not self.keepAspectRatioCheckBox.isChecked())
        self.mosaicHeightLabel.setVisible(not self.keepAspectRatioCheckBox.isChecked())

        self.classicProgressBar.setVisible(False)

        # misc
        self.db = Database()

        self.showImageLibrary()

    # tab-buttons
    def bibTabBtnListiner(self):
        self.stackedWidget.setCurrentIndex(0)

    def classicTabBtnListiner(self):
        self.stackedWidget.setCurrentIndex(1)

    def partialTabBtnListiner(self):
        self.stackedWidget.setCurrentIndex(2)

    # library page
    def importBtnListener(self):
        importPath = self.libraryLineEdit.text()

        if importPath.endswith('.mp4'):
            if os.path.exists('bib'):
                shutil.rmtree('bib')
            os.makedirs('bib')

            subprocess.run('ffmpeg -i ' + importPath + ' -vf fps=1/5 bib/out%d.png')
            self.db.importAllImages('bib',
                                    self.importProgressBar,
                                    self.faceDetectionCheckBox.isChecked(),
                                    int(self.minNeighborsLineEdit.text()))

        else:
            self.db.importAllImages(importPath,
                                    self.importProgressBar,
                                    self.faceDetectionCheckBox.isChecked(),
                                    int(self.minNeighborsLineEdit.text()))

        self.showImageLibrary()

    def faceDetectionCheckBoxBtnListiner(self, checked):
        self.minNeighborsLineEdit.setVisible(checked)
        self.minNeighborsLabel.setVisible(checked)

    def deleteLibraryBtnListiner(self):
        self.db.deleteLibrary()
        self.imageListViewModel.removeRows(0, self.imageListViewModel.rowCount())

    def showImageLibrary(self):
        self.imageListViewModel.removeRows(0, self.imageListViewModel.rowCount())
        cursor = self.db.getAllCroppedImages()
        for img_arr in cursor:
            img = self.db.decode(img_arr[0])

            image = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap.fromImage(image))

            item = QtGui.QStandardItem()
            item.setIcon(icon)

            self.imageListViewModel.appendRow(item)

        self.importProgressBar.setVisible(False)

    # classic-page
    def keepAspectRatioCheckBoxBtnListiner(self, checked):
        self.mosaicHeightLineEdit.setVisible(not checked)
        self.mosaicHeightLabel.setVisible(not checked)

    def classicBtnListener(self):
        self.classicProgressBar.setValue(0)
        self.classicProgressBar.setVisible(True)
        img = rgbImport(self.mosaicImageLineEdit.text())
        img = destroyImg(img,
                         int(self.mosaicWidthLineEdit.text()),
                         self.getMosaicImageHeight(img))
        result = createDetailMosaic(img, np.array(self.db.getAllColorValuesWithIDs().fetchall()),
                                    # self.elementSizeComboBox.currentText(),
                                    self.db, self.classicProgressBar)
        cv2.imwrite('output.jpeg', result)
        self.classicProgressBar.setVisible(False)

        imageViewerFromCommandLine = {'linux': 'xdg-open',
                                      'win32': 'explorer',
                                      'darwin': 'open'}[sys.platform]
        subprocess.run([imageViewerFromCommandLine, 'output.jpeg'])

    def getMosaicImageHeight(self, img):
        if self.keepAspectRatioCheckBox.isChecked():
            height, width, channels = img.shape
            return int(height / (width / int(self.mosaicWidthLineEdit.text())))
        else:
            return int(self.mosaicHeightLineEdit.text())
