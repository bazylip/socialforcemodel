from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Simulation'
        self.imagenumber = 0
        self.initUI()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Right:
            if self.imagenumber < 20:
                self.imagenumber = self.imagenumber+1
                self.showimage(self.imagenumber)
        if key == Qt.Key_Left:
            if self.imagenumber > 0:
                self.imagenumber = self.imagenumber-1
                self.showimage(self.imagenumber)
        
    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label = QLabel(self)
        layout.addWidget(self.label)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('test.png'))
        self.setGeometry(500, 500, 500, 500)
        self.showimage(0)
        self.show()

    def showimage(self,imagenumber):
        directory = "./tmp/img1"
        import platform
        if platform.system() == 'Linux':
            pixmap = QPixmap(directory + "/" + str(imagenumber) + ".png")
        else: 
            imagelist = ["0.png","1.0.png","2.0.png","3.0.png","4.0.png","5.0.png","6.0.png","7.0.png","8.0.png","9.0.png","10.0.png"]
            pixmap = QPixmap(directory + '\\' + imagelist[imagenumber])
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
