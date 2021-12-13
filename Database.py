import os
import sqlite3

import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication

import mosaic


class Database:
    db_path = "mosaic.db"

    def __init__(self):

        self.connection = sqlite3.connect(self.db_path)

        cursor = self.newCursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS image (
                            image_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            img_original TEXT,
                            img_cropped_32 TEXT,
                            img_cropped_64 TEXT,
                            img_cropped_128 TEXT,
                            img_cropped_256 TEXT,
                            color_r REAL,
                            color_g REAL,
                            color_b REAL);''')
        self.connection.commit()

    def __del__(self):
        self.connection.close()

    def saveImg(self, img_original, img_cropped_32, img_cropped_64, img_cropped_128, img_cropped_256, color, cursor):
        cursor.execute('''INSERT INTO image (img_original, img_cropped_32, img_cropped_64, img_cropped_128, img_cropped_256, color_r, color_g, color_b)
                                VALUES (?,?,?,?,?,?,?,?)''',
                       (self.encode(img_original), self.encode(img_cropped_32), self.encode(img_cropped_64),
                        self.encode(img_cropped_128), self.encode(img_cropped_256), color[0], color[1], color[2]))

    def importAllImages(self, folderPath, progressBar, crop_to_faces, min_neighbors):
        cursor = self.newCursor()
        listdir = os.listdir(folderPath)
        progressBar.setMaximum(len(listdir))
        img_counter = 0
        progressBar.setValue(img_counter)
        progressBar.setVisible(True)
        QApplication.processEvents()

        for filename in listdir:
            img = mosaic.rgbImport(os.path.join(folderPath, filename))
            if img is not None:
                self.saveImg(img,
                             mosaic.quadsize(img, 32, crop_to_faces, min_neighbors),
                             mosaic.quadsize(img, 64, crop_to_faces, min_neighbors),
                             mosaic.quadsize(img, 128, crop_to_faces, min_neighbors),
                             mosaic.quadsize(img, 256, crop_to_faces, min_neighbors),
                             mosaic.getColorValue(img),
                             cursor)
            img_counter += 1
            progressBar.setValue(img_counter)
            QApplication.processEvents()
        cursor.connection.commit()

    def getAllCroppedImages(self):
        cursor = self.newCursor()
        cursor.execute('''SELECT img_cropped_32 FROM image''')
        return cursor

    def getCroppedImagesWithIDByID(self, ids, elementSize):
        cursor = self.newCursor()
        if elementSize == 32:
            sql = "SELECT image_id, img_cropped_32 FROM image WHERE image_id IN ({seq})".format(seq=','.join(['?'] * len(ids)))
        elif elementSize == 64:
            sql = "SELECT image_id, img_cropped_64 FROM image WHERE image_id IN ({seq})".format(seq=','.join(['?'] * len(ids)))
        elif elementSize == 128:
            sql = "SELECT image_id, img_cropped_128 FROM image WHERE image_id IN ({seq})".format(seq=','.join(['?'] * len(ids)))
        else:
            sql = "SELECT image_id, img_cropped_256 FROM image WHERE image_id IN ({seq})".format(seq=','.join(['?'] * len(ids)))

        cursor.execute(sql, ids)
        return cursor

    def getAllOriginalImages(self):
        cursor = self.newCursor()
        cursor.execute('''SELECT img_original FROM image''')
        return cursor

    def getAllColorValuesWithIDs(self):
        cursor = self.newCursor()
        cursor.execute('''SELECT image_id, color_r, color_g, color_b FROM image''')
        return cursor

    def newCursor(self):
        return self.connection.cursor()

    def encode(self, img):
        img_encode = cv2.imencode('.png', img)[1]
        data_encode = np.array(img_encode)
        return data_encode.tostring()

    def decode(self, img_string):
        nparr = np.fromstring(img_string, np.uint8)
        return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    def deleteLibrary(self):
        cursor = self.newCursor()
        cursor.execute('''DELETE FROM image''')
        self.connection.commit()
