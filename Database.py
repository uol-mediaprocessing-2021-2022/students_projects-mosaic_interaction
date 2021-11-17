import os
import sqlite3

import mosaic


class Database:
    db_path = "mosaic.db"

    def __init__(self):
        self.connection = sqlite3.connect(self.db_path)

        cursor = self.newCursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS image (
                            image_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            img_original BLOB,
                            img_cropped BLOB,
                            color_r REAL,
                            color_g REAL,
                            color_b REAL);''')
        self.connection.commit()

    def __del__(self):
        self.connection.close()

    def saveImg(self, img_original, img_cropped, color, cursor):
        cursor.execute('''INSERT INTO image (img_original, img_cropped, color_r, color_g, color_b)
                                VALUES (?,?,?,?,?)''', (img_original, img_cropped, color[0], color[1], color[2]))

    def saveAllImgages(self, img_table):
        cursor = self.newCursor()
        for entry in img_table:
            cursor.execute('''INSERT INTO image (img_original, img_cropped, color_r, color_g, color_b)
                                            VALUES (?,?,?,?,?)''',
                           (sqlite3.Binary(entry[0]), sqlite3.Binary(entry[1]), entry[2][0], entry[2][1], entry[2][2]))
        self.connection.commit()


    def importAllImages(self, folderPath):
        cursor = self.newCursor()
        for filename in os.listdir(folderPath):
            img = mosaic.rgbImport(os.path.join(folderPath, filename))
            if img is not None:
                self.saveImg(img, mosaic.quadsize(img), mosaic.getColorValue(img), cursor)
        cursor.connection.commit()

    def newCursor(self):
        return self.connection.cursor()
