from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Loading'
        self.initUI()
 
    def initUI(self):
        self.layout = QVBoxLayout()

        self.setWindowTitle(self.title)
        self.setGeometry(200, 200, 200, 200)
        
        self.label = QLabel()
        self.label.setText('Loading...')
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)
        self.layout.addStretch()
        self.setLayout(self.layout)
        
        self.show()

    def loading(self):
        label = QLabel()
        label.setText('Loading...')
        label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addStretch()
