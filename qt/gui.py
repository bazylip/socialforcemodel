from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox, QMainWindow, QToolTip
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap

class WindowTest1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(250,300,1364,213)
        self.setWindowIcon(QIcon('test.png'))
        label = QLabel(self)
        pixmap = QPixmap("./testimo1/0.png")
        label.resize(pixmap.width(),pixmap.height())
        label.setPixmap(pixmap)
        self.setWindowTitle("Test 1")



class Application(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.interface()


    def interface(self):
        gridLayout=QGridLayout()

        buttonTest1 = QPushButton("Test 1",self)
        buttonTest2 = QPushButton("Test 2",self)
        buttonTest3 = QPushButton("Test 3",self)
        buttonTest4 = QPushButton("Test 4",self)
        buttonExit = QPushButton("Exit",self)

        boxLayout = QHBoxLayout()
        boxLayout.addWidget(buttonTest1)
        boxLayout.addWidget(buttonTest2)
        boxLayout.addWidget(buttonTest3)
        boxLayout.addWidget(buttonTest4)
        boxLayout.addWidget(buttonExit)

        gridLayout.addLayout(boxLayout,3,0,1,3)
        gridLayout.addWidget(buttonExit,3,0,1,3)

        self.setLayout(gridLayout)

        buttonTest1.clicked.connect(self.action)
        buttonTest2.clicked.connect(self.action)
        buttonTest3.clicked.connect(self.action)
        buttonTest4.clicked.connect(self.action)
        buttonExit.clicked.connect(self.closeApp)

        self.setGeometry(500,500,1000,100)
        self.setWindowIcon(QIcon('qt/test.png'))
        self.setWindowTitle("Model testing")
        self.show()

    def windowTest1(self):
        self.w = WindowTest1()
        self.w.show()
        self.hide()


    def closeApp(self):
        self.close()


    def action(self):
        sender_=self.sender()
        try:
            if sender_.text()=="Test 1":
                QMessageBox.about(self,"Test message","Test 1 will start in a moment...")
                self.windowTest1()
            if sender_.text()=="Test 2":
                QMessageBox.about(self,"Test message","Test 2 will start in a moment...")
            if sender_.text()=="Test 3":
                QMessageBox.about(self,"Test message","Test 3 will start in a moment...")
            if sender_.text()=="Test 4":
                QMessageBox.about(self,"Test message","Test 4 will start in a moment...")
            else:
                pass

        except ValueError:
            QMessageBox.warning(self,"Error",QMessageBox.Ok)


    def closeEvent(self,event):
        choice = QMessageBox.question(
            self,'Exit message',
            "Are you sure?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No)

        if choice == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


