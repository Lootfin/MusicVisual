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
pygame.init()
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
        self.r = 255
        self.g = 255
        self.b = 255

        self.setGeometry(120, 160, 120, 160)
        self.setWindowTitle('Конвертер')
        self.setBackgroundRole(10)
        self.move(150, 0)

    def initUI(self):
        self.sv_but = QPushButton('Open file', self)
        self.sv_but.resize(100, 50)
        self.sv_but.move(10, 10)

        self.btn_grp = QButtonGroup()
        self.btn_grp.setExclusive(True)
        self.btn_grp.addButton(self.sv_but)

        self.btn_grp.buttonClicked.connect(self.opn_file)

        self.start = QPushButton('Start', self)
        self.start.resize(100, 50)
        self.start.move(10, 70)
        self.start.clicked.connect(self.Konvert)
        self.show()


        self.laba = QLabel(self)
        self.laba.setText('filename')
        self.laba.move(200, 130)

        self.bush = True
        self.sizer = 100

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
        screen = pygame.display.set_mode((width, height))
        #pygame.mixer_music.load(self.msc)
       # pygame.mixer_music.play()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((0,0,0))
            pygame.draw.circle(screen, (self.r, self.g, self.b), (540, 450), self.sizer)
            self.pulsating()
            clock.tick(100)
            pygame.display.flip()

    def draw_poly(self, size):
        pygame.draw.circle(self.screen, self.change_color(self.tempo), (540, 450), size)
        #pause(0.2)

    def pulsating(self):
        if self.sizer > 300 or self.sizer < 100:
            self.bush = not self.bush
            self.r, self.g, self.b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        if self.bush:
            self.sizer += 5
        else:
            self.sizer -= 5

    def change_color(self, temp):
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