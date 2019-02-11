import random
import sys
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets
from librosa import beat as bt
from PyQt5.QtWidgets import QWidget, QPushButton, QButtonGroup, QLabel
import librosa
import pygame
from time import sleep as pause

file = ''
clock = pygame.time.Clock()
class File(QWidget):


    def __init__(self):
        super().__init__()
        global file

        self.file = file
        self.title = 'Choose file'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.openFileNameDialog()
        self.show()


    def openFileNameDialog(self):
        pass
        global file
        options = QFileDialog.Options()

        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Choose file", "",
                                          "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            file = fileName
            self.close()


class MyWidget(QWidget):
    pass
    def __init__(self):
        super().__init__()
        self.initUI()
        self.r = 1
        self.g = 1
        self.b = 1

        self.setGeometry(600, 400, 600, 400)
        self.setWindowTitle('Конвертер')
        self.setBackgroundRole(10)
        self.move(150, 0)

    def initUI(self):
        self.sv_but = QPushButton('Open file', self)
        self.sv_but.resize(100, 100)
        self.sv_but.move(30, 100)

        self.btn_grp = QButtonGroup()
        self.btn_grp.setExclusive(True)
        self.btn_grp.addButton(self.sv_but)

        self.btn_grp.buttonClicked.connect(self.opn_file)

        self.start = QPushButton('Start', self)
        self.start.resize(80, 30)
        self.start.move(30, 50)
        self.start.clicked.connect(self.Konvert)
        self.show()

        self.laba = QLabel(self)
        self.laba.setText('filename')
        self.laba.move(200, 130)

    def opn_file(self):
        qwer = File()
        self.msc = file
        print(self.msc)
        self.y, self.sr = librosa.core.load(self.msc)
        self.tempo, self.beats = bt.beat_track(y=self.y, sr=self.sr)
        print('loading complete')
        return qwer

    def Konvert(self):
        pygame.init()
        self.size = width, height = 1080, 900
        self.screen = pygame.display.set_mode((width, height))
        while True:
            pygame.draw.circle(self.screen, self.change_color(self.tempo), (540, 450), 10)
            clock.tick(100)
            pygame.display.flip()

    def draw_poly(self, size):
        pygame.draw.circle(self.screen, self.change_color(self.tempo), (540, 450), size)
        #pause(0.2)

    def pulsating(self):
        self.draw_poly(50)
        self.draw_poly(55)
        self.draw_poly(60)
        self.draw_poly(65)
        self.draw_poly(70)
        self.draw_poly(65)
        self.draw_poly(60)
        self.draw_poly(55)
        self.draw_poly(50)

    def change_color(self, temp):
        return 255, 0, 0
        r, g, b = self.r, self.g, self.b
        if 60 <= temp < 100:
            if r == 0 or g == 0 or b == 0:
                (r, g, b) = (r + random.randint(10, 20), g + random.randint(10, 20), b + random.randint(10, 20))
            elif r == 255 or g == 255 or b == 255:
                (r, g, b) = (r - random.randint(10, 20), g - random.randint(10, 20), b - random.randint(10, 20))
            else:
                (r, g, b) = (r + random.randint(10, 20), g + random.randint(10, 20), b + random.randint(10, 20))
        elif temp >= 100:
            if r == 0 or g == 0 or b == 0:
                (r, g, b) = (r + random.randint(20, 30), g + random.randint(20, 30), b + random.randint(20, 30))
            elif r == 255 or g == 255 or b == 255:
                (r, g, b) = (r - random.randint(20, 30), g - random.randint(20, 30), b - random.randint(20, 30))
            else:
                (r, g, b) = (r + random.randint(20, 30), g + random.randint(20, 30), b + random.randint(20, 30))
        else:
            if r == 0 or g == 0 or b == 0:
                (r, g, b) = (r + random.randint(1, 10), g + random.randint(1, 10), b + random.randint(1, 10))
            elif r == 255 or g == 255 or b == 255:
                (r, g, b) = (r - random.randint(1, 10), g - random.randint(1, 10), b - random.randint(1, 10))
            else:
                (r, g, b) = (r + random.randint(1, 10), g + random.randint(1, 10), b + random.randint(1, 10))
        self.r, self.g, self.b = r, g, b
        return (r, g, b)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())