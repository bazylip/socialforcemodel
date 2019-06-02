from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import platform

class App(QWidget):
    def __init__(self, folderNumber, imagesAmount):
        super().__init__()
        self.title = 'Simulation 0/' + str(imagesAmount)
        self.imageNumber = 0
        self.folderNumber = folderNumber
        self.imagesAmount = imagesAmount
        self.initUI()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Right:
            if self.imageNumber < self.imagesAmount:
                if self.showImage(self.folderNumber, self.imageNumber + 1):
                    self.imageNumber = self.imageNumber + 1
                    self.setWindowTitle('Simulation ' + str(self.imageNumber) + '/' + str(self.imagesAmount))
                
        if key == Qt.Key_Left:
            if self.imageNumber > 0:
                if self.showImage(self.folderNumber, self.imageNumber - 1):
                    self.imageNumber = self.imageNumber - 1
                    self.setWindowTitle('Simulation ' + str(self.imageNumber) + '/' + str(self.imagesAmount))
                
        if key == Qt.Key_Escape:
                self.close()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label = QLabel(self)
        layout.addWidget(self.label)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('test.png'))
        self.setGeometry(400, 100, 200, 200)
        self.showImage(self.folderNumber, 0)
        self.show()

    def showImage(self, folderNumber, imageNumber):
        if platform.system() == 'Linux':
            directory = "./tmp/img" + str(folderNumber)
            pixmap = QPixmap(directory + "/" + str(imageNumber) + ".png")
        else:
            directory = "tmp/img" + str(folderNumber)
            imagelist = ["0.png","1.0.png","2.0.png","3.0.png","4.0.png","5.0.png","6.0.png","7.0.png","8.0.png","9.0.png",
                         "10.0.png","11.0.png","12.0.png","13.0.png","14.0.png","15.0.png","16.0.png","17.0.png","18.0.png",
                         "19.0.png","20.0.png"]
            pixmap = QPixmap(directory + '\\' + imagelist[imageNumber])
        if not pixmap.isNull():
            pixmapResized = pixmap.scaled(800, 600, Qt.KeepAspectRatio)
            self.label.setPixmap(pixmapResized)
            self.resize(600, 400)
        return not pixmap.isNull()
