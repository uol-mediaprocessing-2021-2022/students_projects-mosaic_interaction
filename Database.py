import os
import sqlite3

import cv2
import numpy as np
from PyQt5 import QtGui

import mosaic


class Database:
    db_path = "mosaic.db"

    def __init__(self):

        # sqlite3.register_adapter(np.int64, lambda val: int(val))
        # sqlite3.register_adapter(np.int32, lambda val: int(val))

        self.connection = sqlite3.connect(self.db_path)

        cursor = self.newCursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS image (
                            image_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            img_original TEXT,
                            img_cropped TEXT,
                            color_r REAL,
                            color_g REAL,
                            color_b REAL);''')
        self.connection.commit()

    def __del__(self):
        self.connection.close()

    def saveImg(self, img_original, img_cropped, color, cursor):
        cursor.execute('''INSERT INTO image (img_original, img_cropped, color_r, color_g, color_b)
                                VALUES (?,?,?,?,?)''', (self.encode(img_original), self.encode(img_cropped), color[0], color[1], color[2]))

    def importAllImages(self, folderPath):
        cursor = self.newCursor()
        for filename in os.listdir(folderPath):
            img = mosaic.rgbImport(os.path.join(folderPath, filename))
            if img is not None:
                self.saveImg(img, mosaic.quadsize(img), mosaic.getColorValue(img), cursor)
        cursor.connection.commit()

    def getAllCroppedImages(self):
        cursor = self.newCursor()
        cursor.execute('''SELECT img_cropped FROM image''')
        return cursor

    def getCroppedImagesWithIDByID(self, ids):
        cursor = self.newCursor()
        sql = "SELECT image_id, img_cropped FROM image WHERE image_id IN ({seq})".format(seq=','.join(['?'] * len(ids)))
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