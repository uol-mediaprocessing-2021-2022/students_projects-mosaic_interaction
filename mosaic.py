import math
import os

import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication


# Bild importieren mit RGB Konvertierung
def rgbImport(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


# Beliebiges Bild quadratisch zuschneiden
def quadsize(img, size):
    height, width, channels = img.shape

    if width > height:
        wStart = int((width - height) / 2)
        wEnd = wStart + height
        cropped_image = img[:, wStart:wEnd]
    else:
        hStart = int((height - width) / 2)
        hEnd = hStart + width
        cropped_image = img[hStart:hEnd, :]

    return cv2.resize(cropped_image, (size, size))


# Komprimierungsansatz mittels dynamischer Verpixelung
def destroyImgDyn(img):
    height, width, channels = img.shape
    img = cv2.resize(img, (int(width / 12), int(height / 12)))
    return img


# Komprimierungsansatz auf feste Größe (TODO: auch Hochkanntbilder sollen unterstützt werden)
def destroyImgFix(img, width, height):
    img = cv2.resize(img, (width, height))
    return img


# Methode, die den durschnittlichen Farbwert eines Bildes liefert
def getColorValueWRONG(img):
    img = cv2.resize(img, (1, 1))
    return img[0][0]


# Methode, die den durschnittlichen Farbwert eines Bildes liefert
def getColorValue(img):
    return img.mean(axis=0).mean(axis=0)


# Euklidische Distanz berechen (Farbunterschied)
def getColorDifference(color1, color2):
    return math.sqrt((int(color1[0]) - int(color2[0])) ** 2 + (int(color1[1]) - int(color2[1])) ** 2 + (
            int(color1[2]) - int(color2[2])) ** 2)


#  Funktion, die Bilder importiert
def getAllImages(folderPath):
    images = []
    for filename in os.listdir(folderPath):
        img = rgbImport(os.path.join(folderPath, filename))
        if img is not None:
            images.append(img)
    return images


# Schneidet alle Bilder zu
# wird derzeit nicht in der gui verwendet.
def cropAllImages(allImages):
    allCroppedImages = []
    for img in allImages:
        allCroppedImages.append(quadsize(img))
    return allCroppedImages


# Ermittelt die durchschnittlichen Farbwerte aller Bilder
def getAllColorValues(allImages):
    allColorValues = []
    for img in allImages:
        allColorValues.append(getColorValue(img))
    return allColorValues


#  Erstellt das MosAIc
def createMosaic(originImg, allColorValuesWithIDs, elementSize, db, progressBar):
    ids = allColorValuesWithIDs[:, 0]
    colorValues = allColorValuesWithIDs[:, 1:]
    height, width, channels = originImg.shape

    progressBar.setMaximum(height * width * 2)
    progressBarValue = 0

    id_matrix = []
    for y in range(height):
        id_matrix_row = []
        for x in range(width):
            minDif = 500
            for i in range(len(colorValues)):
                value = colorValues[i]
                dif = getColorDifference(value, originImg[y, x])
                if dif < minDif:
                    minDif = dif
                    minDifID = ids[i]

            id_matrix_row.append(minDifID)
            progressBarValue += 1
            progressBar.setValue(progressBarValue)
            QApplication.processEvents()
        if y == 0:
            id_matrix = id_matrix_row
        else:
            id_matrix = np.vstack([id_matrix, id_matrix_row])

    croppedImagesWithIDs = np.array(db.getCroppedImagesWithIDByID(np.unique(id_matrix), elementSize).fetchall())

    mosaic_img = []
    for id_matrix_row in id_matrix:
        mosaic_row = []
        for id in id_matrix_row:
            img_to_append = db.decode(croppedImagesWithIDs[croppedImagesWithIDs[:, 0].astype(int) == id, 1])
            mosaic_row.append(img_to_append)
            progressBarValue += 1
            progressBar.setValue(progressBarValue)
            QApplication.processEvents()
        mosaic_img.append(np.concatenate(mosaic_row, axis=1))

    return cv2.cvtColor(np.concatenate(mosaic_img, axis=0), cv2.COLOR_BGR2RGB)
