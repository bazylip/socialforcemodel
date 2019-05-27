from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSlot

class App(QWidget):
    def __init__(self, results = []):
        super().__init__()
        self.results = results
        self.title = 'Results'
        self.imagenumber = 0
        self.initUI()

        
    def initUI(self):
        vbox = QVBoxLayout()
        
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('test.png'))
        self.setGeometry(400, 200, 500, 180)
        
        for i in range(1,6):
            label = QLabel()
            label.setText("Result " + str(i) + ": " + str(self.results[i-1]))
            
            if self.results[i-1]:
                label.setStyleSheet('color: green')
            else:
                label.setStyleSheet('color: red')
            
            label.setAlignment(Qt.AlignLeft)
        
            button = self.createButton(i)

            hbox = QHBoxLayout()
            hbox.addWidget(label)
            
            hbox.addWidget(button)
            vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.show()

    def createButton(self, number):
        button = QPushButton("See results " + str(number), self)
        button.clicked.connect(lambda: self.buttonClick(number))
        return button

    @pyqtSlot()
    def buttonClick(self, number):
        print(number)
