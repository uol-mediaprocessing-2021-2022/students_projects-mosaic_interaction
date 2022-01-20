import os
import shutil
import subprocess
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
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
        self.mosaicTabButton.clicked.connect(self.mosaicTabBtnListiner)
        self.detailMosaicTabButton.clicked.connect(self.detailMosaicTabBtnListiner)

        # library-page
        self.imageListViewModel = QtGui.QStandardItemModel()
        self.imageListView.setModel(self.imageListViewModel)

        self.importProgressBar.setVisible(False)

        self.importButton.clicked.connect(self.importBtnListener)
        self.faceDetectionCheckBox.clicked.connect(self.faceDetectionCheckBoxBtnListiner)

        self.minNeighborsLabel.setVisible(self.faceDetectionCheckBox.isChecked())
        self.minNeighborsLineEdit.setVisible(self.faceDetectionCheckBox.isChecked())

        self.deleteLibraryButton.clicked.connect(self.deleteLibraryBtnListiner)

        # mosaic-page
        self.mosaicButton.clicked.connect(self.mosaicBtnListener)

        self.mosaicKeepAspectRatioCheckBox.clicked.connect(self.mosaicKeepAspectRatioCheckBoxBtnListiner)

        self.mosaicHeightLineEdit.setVisible(not self.mosaicKeepAspectRatioCheckBox.isChecked())
        self.mosaicHeightLabel.setVisible(not self.mosaicKeepAspectRatioCheckBox.isChecked())

        self.mosaicBlendImageCheckBox.clicked.connect(self.mosaicBlendImageCheckBoxBtnListiner)
        self.mosaicBlendImageEvenRadioButton.clicked.connect(self.mosaicBlendImageRadioButtonBtnListiner)
        self.mosaicBlendImageRightRadioButton.clicked.connect(self.mosaicBlendImageRadioButtonBtnListiner)
        self.mosaicBlendImageLeftRadioButton.clicked.connect(self.mosaicBlendImageRadioButtonBtnListiner)
        self.mosaicBlendImageDownRadioButton.clicked.connect(self.mosaicBlendImageRadioButtonBtnListiner)
        self.mosaicBlendImageTopRadioButton.clicked.connect(self.mosaicBlendImageRadioButtonBtnListiner)

        self.mosaicBlendImageEvenRadioButton.setVisible(self.mosaicBlendImageCheckBox.isChecked())
        self.mosaicBlendImageRightRadioButton.setVisible(self.mosaicBlendImageCheckBox.isChecked())
        self.mosaicBlendImageLeftRadioButton.setVisible(self.mosaicBlendImageCheckBox.isChecked())
        self.mosaicBlendImageDownRadioButton.setVisible(self.mosaicBlendImageCheckBox.isChecked())
        self.mosaicBlendImageTopRadioButton.setVisible(self.mosaicBlendImageCheckBox.isChecked())

        self.mosaicTransparencyLabel.setVisible(
            self.mosaicBlendImageCheckBox.isChecked() and self.mosaicBlendImageEvenRadioButton.isChecked())
        self.mosaicTransparencySlider.setVisible(
            self.mosaicBlendImageCheckBox.isChecked() and self.mosaicBlendImageEvenRadioButton.isChecked())

        self.mosaicProgressBar.setVisible(False)

        # detailMosaic-page
        self.detailMosaicShowEdgesButton.clicked.connect(self.detailMosaicShowEdgesBtnListener)
        self.detailMosaicButton.clicked.connect(self.detailMosaicBtnListener)

        self.detailMosaicKeepAspectRatioCheckBox.clicked.connect(self.detailMosaicKeepAspectRatioCheckBoxBtnListiner)

        self.detailMosaicHeightLineEdit.setVisible(not self.detailMosaicKeepAspectRatioCheckBox.isChecked())
        self.detailMosaicHeightLabel.setVisible(not self.detailMosaicKeepAspectRatioCheckBox.isChecked())

        self.detailMosaicBlendImageCheckBox.clicked.connect(self.detailMosaicBlendImageCheckBoxBtnListiner)
        self.detailMosaicBlendImageEvenRadioButton.clicked.connect(self.detailMosaicBlendImageRadioButtonBtnListiner)
        self.detailMosaicBlendImageRightRadioButton.clicked.connect(self.detailMosaicBlendImageRadioButtonBtnListiner)
        self.detailMosaicBlendImageLeftRadioButton.clicked.connect(self.detailMosaicBlendImageRadioButtonBtnListiner)
        self.detailMosaicBlendImageDownRadioButton.clicked.connect(self.detailMosaicBlendImageRadioButtonBtnListiner)
        self.detailMosaicBlendImageTopRadioButton.clicked.connect(self.detailMosaicBlendImageRadioButtonBtnListiner)

        self.detailMosaicBlendImageEvenRadioButton.setVisible(self.detailMosaicBlendImageCheckBox.isChecked())
        self.detailMosaicBlendImageRightRadioButton.setVisible(self.detailMosaicBlendImageCheckBox.isChecked())
        self.detailMosaicBlendImageLeftRadioButton.setVisible(self.detailMosaicBlendImageCheckBox.isChecked())
        self.detailMosaicBlendImageDownRadioButton.setVisible(self.detailMosaicBlendImageCheckBox.isChecked())
        self.detailMosaicBlendImageTopRadioButton.setVisible(self.detailMosaicBlendImageCheckBox.isChecked())

        self.detailMosaicTransparencyLabel.setVisible(
            self.detailMosaicBlendImageCheckBox.isChecked() and self.detailMosaicBlendImageEvenRadioButton.isChecked())
        self.detailMosaicTransparencySlider.setVisible(
            self.detailMosaicBlendImageCheckBox.isChecked() and self.detailMosaicBlendImageEvenRadioButton.isChecked())

        self.detailMosaicProgressBar.setVisible(False)

        # Workaround: won't work, even if it is set by Ui_MainWindow ...
        self.detailMosaicElementMaxSizeComboBox.setCurrentText("512")

        # misc
        self.db = Database()

    def postInit(self):
        QApplication.processEvents()
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.showImageLibrary()
        QApplication.restoreOverrideCursor()

    # tab-buttons
    def bibTabBtnListiner(self):
        self.stackedWidget.setCurrentIndex(0)

    def mosaicTabBtnListiner(self):
        self.stackedWidget.setCurrentIndex(1)

    def detailMosaicTabBtnListiner(self):
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

    # mosaic-page
    def mosaicKeepAspectRatioCheckBoxBtnListiner(self, checked):
        self.mosaicHeightLineEdit.setVisible(not checked)
        self.mosaicHeightLabel.setVisible(not checked)

    def mosaicBlendImageCheckBoxBtnListiner(self, checked):
        self.mosaicBlendImageEvenRadioButton.setVisible(checked)
        self.mosaicBlendImageRightRadioButton.setVisible(checked)
        self.mosaicBlendImageLeftRadioButton.setVisible(checked)
        self.mosaicBlendImageDownRadioButton.setVisible(checked)
        self.mosaicBlendImageTopRadioButton.setVisible(checked)

        self.mosaicTransparencyLabel.setVisible(checked and self.mosaicBlendImageEvenRadioButton.isChecked())
        self.mosaicTransparencySlider.setVisible(checked and self.mosaicBlendImageEvenRadioButton.isChecked())

    def mosaicBlendImageRadioButtonBtnListiner(self, checked):
        self.mosaicTransparencyLabel.setVisible(
            self.mosaicBlendImageCheckBox.isChecked() and self.mosaicBlendImageEvenRadioButton.isChecked())
        self.mosaicTransparencySlider.setVisible(
            self.mosaicBlendImageCheckBox.isChecked() and self.mosaicBlendImageEvenRadioButton.isChecked())

    def mosaicBtnListener(self):
        self.mosaicProgressBar.setValue(0)
        self.mosaicProgressBar.setVisible(True)
        img = rgbImport(self.mosaicImageLineEdit.text())
        mosaicWidth = int(self.mosaicWidthLineEdit.text())
        mosaicHeight = self.getMosaicImageHeight(img,
                                                 self.mosaicKeepAspectRatioCheckBox,
                                                 mosaicWidth,
                                                 int(self.mosaicHeightLineEdit.text()))
        transparency = self.mosaicTransparencySlider.value()
        if self.mosaicBlendImageCheckBox.isChecked() \
                and self.mosaicBlendImageEvenRadioButton.isChecked() \
                and transparency == 100:
            elemSize = int(self.mosaicElementSizeComboBox.currentText())
            img = cv2.resize(img, (mosaicWidth * elemSize, mosaicHeight * elemSize))
            cv2.imwrite('output.jpeg', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            self.mosaicProgressBar.setVisible(False)
            self.showImg('output.jpeg')
            return

        destroyedImg = destroyImg(img,
                                  mosaicWidth,
                                  mosaicHeight)
        result = createMosaic(destroyedImg, np.array(self.db.getAllColorValuesWithIDs().fetchall()),
                              int(self.mosaicElementSizeComboBox.currentText()),
                              self.db, self.mosaicProgressBar)

        if self.mosaicBlendImageCheckBox.isChecked():
            if self.mosaicBlendImageEvenRadioButton.isChecked() and transparency > 0:
                result = addOriginalPicture(result, img, transparency)
            else:
                topdown = self.mosaicBlendImageTopRadioButton.isChecked() or self.mosaicBlendImageDownRadioButton.isChecked()
                inverted = self.mosaicBlendImageTopRadioButton.isChecked() or self.mosaicBlendImageLeftRadioButton.isChecked()
                result = fadeToOriginalPicture(result, img, topdown, inverted)


        cv2.imwrite('output.jpeg', result)
        self.mosaicProgressBar.setVisible(False)
        self.showImg('output.jpeg')

    # detailMosaic-page
    def detailMosaicKeepAspectRatioCheckBoxBtnListiner(self, checked):
        self.detailMosaicHeightLineEdit.setVisible(not checked)
        self.detailMosaicHeightLabel.setVisible(not checked)

    def detailMosaicBlendImageCheckBoxBtnListiner(self, checked):
        self.detailMosaicBlendImageEvenRadioButton.setVisible(checked)
        self.detailMosaicBlendImageRightRadioButton.setVisible(checked)
        self.detailMosaicBlendImageLeftRadioButton.setVisible(checked)
        self.detailMosaicBlendImageDownRadioButton.setVisible(checked)
        self.detailMosaicBlendImageTopRadioButton.setVisible(checked)

        self.detailMosaicTransparencyLabel.setVisible(checked and self.detailMosaicBlendImageEvenRadioButton.isChecked())
        self.detailMosaicTransparencySlider.setVisible(checked and self.detailMosaicBlendImageEvenRadioButton.isChecked())

    def detailMosaicBlendImageRadioButtonBtnListiner(self, checked):
        self.detailMosaicTransparencyLabel.setVisible(
            self.detailMosaicBlendImageCheckBox.isChecked() and self.detailMosaicBlendImageEvenRadioButton.isChecked())
        self.detailMosaicTransparencySlider.setVisible(
            self.detailMosaicBlendImageCheckBox.isChecked() and self.detailMosaicBlendImageEvenRadioButton.isChecked())

    def detailMosaicBtnListener(self):
        self.detailMosaicProgressBar.setValue(0)
        self.detailMosaicProgressBar.setVisible(True)
        img = rgbImport(self.detailMosaicImageLineEdit.text())
        mosaicWidth = int(self.detailMosaicWidthLineEdit.text())
        mosaicHeight = self.getMosaicImageHeight(img,
                                                 self.detailMosaicKeepAspectRatioCheckBox,
                                                 mosaicWidth,
                                                 int(self.detailMosaicHeightLineEdit.text()))

        transparency = self.detailMosaicTransparencySlider.value()
        if self.detailMosaicBlendImageCheckBox.isChecked() \
                and self.detailMosaicBlendImageEvenRadioButton.isChecked() \
                and transparency == 100:
            elemSize = int(self.detailMosaicElementMinSizeComboBox.currentText())
            img = cv2.resize(img, (mosaicWidth * elemSize, mosaicHeight * elemSize))
            cv2.imwrite('output.jpeg', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            self.detailMosaicProgressBar.setVisible(False)
            self.showImg('output.jpeg')
            return

        destroyedImg = destroyImg(img,
                         mosaicWidth,
                         mosaicHeight)
        result = createDetailMosaic(destroyedImg, np.array(self.db.getAllColorValuesWithIDs().fetchall()),
                                    int(self.detailMosaicElementMinSizeComboBox.currentText()),
                                    int(self.detailMosaicElementMaxSizeComboBox.currentText()),
                                    float(int(self.detailMosaicElementAllowedDeviationLineEdit.text()) / 100),
                                    self.db, self.detailMosaicProgressBar,
                                    self.detailMosaicUseEdgedetectionCheckBox.isChecked())

        if self.detailMosaicBlendImageCheckBox.isChecked():
            if self.detailMosaicBlendImageEvenRadioButton.isChecked() and transparency > 0:
                result = addOriginalPicture(result, img, transparency)
            else:
                topdown = self.detailMosaicBlendImageTopRadioButton.isChecked() or self.detailMosaicBlendImageDownRadioButton.isChecked()
                inverted = self.detailMosaicBlendImageTopRadioButton.isChecked() or self.detailMosaicBlendImageLeftRadioButton.isChecked()
                result = fadeToOriginalPicture(result, img, topdown, inverted)

        cv2.imwrite('output.jpeg', result)
        self.detailMosaicProgressBar.setVisible(False)
        self.showImg('output.jpeg')

    def detailMosaicShowEdgesBtnListener(self):
        img = rgbImport(self.detailMosaicImageLineEdit.text())
        img = destroyImg(img,
                         int(self.detailMosaicWidthLineEdit.text()),
                         self.getMosaicImageHeight(img,
                                                   self.detailMosaicKeepAspectRatioCheckBox,
                                                   int(self.detailMosaicWidthLineEdit.text()),
                                                   int(self.detailMosaicHeightLineEdit.text())))
        result = getEdges(img)
        cv2.imwrite('output.jpeg', result)
        self.showImg('output.jpeg')

    # misc
    def getMosaicImageHeight(self, img, keepAspectRatioCheckBox, mosaicWidth, mosaicHeight):
        if keepAspectRatioCheckBox.isChecked():
            height, width, channels = img.shape
            return int(height / (width / mosaicWidth))
        else:
            return mosaicHeight

    def showImg(self, path):
        imageViewerFromCommandLine = {'linux': 'xdg-open',
                                      'win32': 'explorer',
                                      'darwin': 'open'}[sys.platform]
        subprocess.run([imageViewerFromCommandLine, path])
