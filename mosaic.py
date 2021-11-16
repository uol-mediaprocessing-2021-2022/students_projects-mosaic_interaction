import cv2
import matplotlib.pyplot as plt
import math
import os
import numpy as np
import matplotlib

matplotlib.rcParams['figure.figsize'] = [12, 12]
matplotlib.rcParams['figure.dpi'] = 72

# Bild importieren mit RGB Konvertierung
def rgbImport(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


# Beliebiges Bild quadratisch zuschneiden
def quadsize(img):
    height, width, channels = img.shape

    if width > height:
        wStart = int((width - height) / 2)
        wEnd = wStart + height
        cropped_image = img[:, wStart:wEnd]
    else:
        hStart = int((height - width) / 2)
        hEnd = hStart + width
        cropped_image = img[hStart:hEnd, :]

    return cv2.resize(cropped_image, (256, 256))


# Komprimierungsansatz mittels dynamischer Verpixelung
def destroyImgDyn(img):
    height, width, channels = img.shape
    img = cv2.resize(img, (int(width / 12), int(height / 12)))
    return img


# Komprimierungsansatz auf feste Größe (TODO: auch Hochkanntbilder sollen unterstützt werden)
def destroyImgFix(img):
    img = cv2.resize(img, (128, 72))
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
def createMosaic(originImg, allCroppedImages, allColorValues):
    originImg = destroyImgFix(originImg)
    height, width, channels = originImg.shape
    col = []
    for y in range(height):
        row = []
        for x in range(width):
            minDif = 500
            for i in range(len(allColorValues)):
                value = allColorValues[i]
                dif = getColorDifference(value, originImg[y, x])
                if dif < minDif:
                    minDif = dif
                    minDifPosition = i
            row.append(allCroppedImages[minDifPosition])
        col.append(np.concatenate(row, axis=1))

    return cv2.cvtColor(np.concatenate(col, axis=0), cv2.COLOR_BGR2RGB)
