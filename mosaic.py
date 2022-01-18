import math

import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication


# Bild importieren mit RGB Konvertierung
def rgbImport(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def get_faces(img, min_neighbors):
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    return face_cascade.detectMultiScale(img_gray, minNeighbors=min_neighbors)


# Beliebiges Bild quadratisch zuschneiden
def quadsize(img, size, crop_to_faces, min_neighbors):
    if crop_to_faces:
        faces = get_faces(img, min_neighbors)
        if len(faces) == 0:
            return quadsize_centered(img, size)

        face_centers = []
        for (x, y, w, h) in faces:
            face_centers.append([x + (w / 2), y + (h / 2)])

        face_centers = np.asarray(face_centers)
        crop_center = np.mean(face_centers, axis=0)
        return quadsize_centered_on_point(img, size, crop_center)

    else:
        return quadsize_centered(img, size)


def quadsize_centered(img, size):
    height, width, channels = img.shape
    return quadsize_centered_on_point(img, size, [width / 2, height / 2])


def quadsize_centered_on_point(img, size, center):
    height, width, channels = img.shape

    if width > height:
        w_start = int(center[0] - (height / 2))
        if w_start < 0:
            w_start = 0

        w_end = w_start + height
        if w_end > width:
            w_start = width - height
            w_end = width

        cropped_image = img[:, w_start:w_end]
    else:
        h_start = int(center[1] - (width / 2))
        if h_start < 0:
            h_start = 0

        h_end = h_start + width
        if h_end > height:
            h_start = height - width
            h_end = height

        cropped_image = img[h_start:h_end, :]

    return cv2.resize(cropped_image, (size, size))


# Komprimierungsansatz auf feste Größe
def destroyImg(img, width, height):
    img = cv2.resize(img, (width, height))
    return img


# Methode, die den durschnittlichen Farbwert eines Bildes liefert
def getColorValue(img):
    return img.mean(axis=0).mean(axis=0)


# Euklidische Distanz berechen (Farbunterschied)
def getColorDifference(color1, color2):
    return math.sqrt((int(color1[0]) - int(color2[0])) ** 2 + (int(color1[1]) - int(color2[1])) ** 2 + (
            int(color1[2]) - int(color2[2])) ** 2)


def getMosaicElementIDs(originImg, allColorValuesWithIDs, progressBar):
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

    return id_matrix


#  Erstellt das MosAIc
def createMosaic(originImg, allColorValuesWithIDs, elementSize, db, progressBar):
    id_matrix = getMosaicElementIDs(originImg, allColorValuesWithIDs, progressBar)
    croppedImagesWithIDs = np.array(db.getCroppedImagesWithIDByID(np.unique(id_matrix), elementSize))
    progressBarValue = progressBar.value()

    mosaic_img = []
    for id_matrix_row in id_matrix:
        mosaic_row = []
        for id in id_matrix_row:
            img_to_append = croppedImagesWithIDs[croppedImagesWithIDs[:, 0].astype(int) == id, 1][0]
            mosaic_row.append(img_to_append)
            progressBarValue += 1
            progressBar.setValue(progressBarValue)
            QApplication.processEvents()
        mosaic_img.append(np.concatenate(mosaic_row, axis=1))

    return cv2.cvtColor(np.concatenate(mosaic_img, axis=0), cv2.COLOR_BGR2RGB)


#  Erstellt das DetailMosAIc
def createDetailMosaic(originImg, allColorValuesWithIDs, minSize, maxSize, allowed_deviation, db, progressBar,
                       useEdgeDetection):
    if useEdgeDetection:
        edges = getEdges(originImg)
    else:
        edges = np.full((originImg.shape[0], originImg.shape[1]), 0)

    id_matrix = getMosaicElementIDs(originImg, allColorValuesWithIDs, progressBar)
    croppedImagesWithIDs = []

    for i in range(int(math.log2(maxSize / minSize)) + 1):
        croppedImagesWithIDs.append(np.array(db.getCroppedImagesWithIDByID(np.unique(id_matrix), minSize * (2 ** i))))

    progressBarValue = progressBar.value()

    id_matrix = np.expand_dims(id_matrix, axis=2)
    new_dim = np.full((len(id_matrix), len(id_matrix[0]), 1), minSize)  # size
    id_matrix = np.append(id_matrix, new_dim, axis=2)
    new_dim2 = np.full((len(id_matrix), len(id_matrix[0]), 1), 0)  # x/y value
    id_matrix = np.append(id_matrix, new_dim2, axis=2)
    id_matrix = np.append(id_matrix, new_dim2, axis=2)

    combineImages(id_matrix, maxSize, minSize, allowed_deviation, edges)

    mosaic_img = []
    for id_matrix_row in id_matrix:
        mosaic_row = []
        for id, size, y, x in id_matrix_row:
            croppedImagesToUse = croppedImagesWithIDs[int(math.log2(size / minSize))]
            img_to_append = croppedImagesToUse[croppedImagesToUse[:, 0].astype(int) == id, 1][0]
            y = int(y)
            x = int(x)
            img_to_append = img_to_append[y:(y + minSize), x:(x + minSize), ]
            mosaic_row.append(img_to_append)
            progressBarValue += 1
            progressBar.setValue(progressBarValue)
            QApplication.processEvents()
        mosaic_img.append(np.concatenate(mosaic_row, axis=1))

    return cv2.cvtColor(np.concatenate(mosaic_img, axis=0), cv2.COLOR_BGR2RGB)


def combineImages(id_matrix, img_size, min_img_size, allowed_deviation, edges):
    for row_idx, id_matrix_row in enumerate(id_matrix):
        for col_idx, [id, size, y, x] in enumerate(id_matrix_row):
            if row_idx + img_size / min_img_size > len(id_matrix) \
                    or col_idx + img_size / min_img_size > len(id_matrix_row):
                continue

            combinable, most_used_img_id = checkForCombinableImages(id_matrix, row_idx, col_idx, img_size, min_img_size,
                                                                    edges, allowed_deviation)
            if not combinable:
                continue

            for y in range(int(img_size / min_img_size)):
                for x in range(int(img_size / min_img_size)):
                    id_matrix[row_idx + y, col_idx + x, 0] = most_used_img_id
                    id_matrix[row_idx + y, col_idx + x, 1] = img_size
                    id_matrix[row_idx + y, col_idx + x, 2] = y * min_img_size
                    id_matrix[row_idx + y, col_idx + x, 3] = x * min_img_size

    if (img_size / 2) > min_img_size:
        combineImages(id_matrix, int(img_size / 2), min_img_size, allowed_deviation, edges)


def checkForCombinableImages(id_matrix, row, col, img_size, min_img_size, edges, allowed_deviation):
    dict = {}
    for r in range(int(img_size / min_img_size)):
        for c in range(int(img_size / min_img_size)):
            if id_matrix[row + r, col + c, 1] != min_img_size:
                return False, -1
            if edges[row + r, col + c] != 0:
                return False, -1

            id = id_matrix[row + r, col + c, 0]
            dict[id] = dict.get(id, 0) + 1

    amount_of_small_imgs = int(img_size ** 2 / min_img_size ** 2)
    return amount_of_small_imgs - max(dict.values()) <= allowed_deviation * amount_of_small_imgs, max(dict,
                                                                                                      key=dict.get)


def getEdges(img):
    return cv2.Canny(img.astype(np.uint8), 100, 250)


def addOriginalPicture(mosaic, img, percentage):
    height, width, channels = mosaic.shape
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (width, height))

    img = img.astype(float)
    mosaic = mosaic.astype(float)

    alpha = np.full_like(img, (percentage / 100))
    img = cv2.multiply(alpha, img)
    mosaic = cv2.multiply(1 - alpha, mosaic)
    return cv2.add(mosaic, img)
