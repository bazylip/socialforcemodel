from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class Application(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.interface()


    def interface(self):
        gridLayout=QGridLayout()

        buttonTest1=QPushButton("Test 1",self)
        buttonTest2=QPushButton("Test 2",self)
        buttonTest3=QPushButton("Test 3",self)
        buttonTest4=QPushButton("Test 4",self)
        buttonExit=QPushButton("Exit",self)

        boxLayout=QHBoxLayout()
        boxLayout.addWidget(buttonTest1)
        boxLayout.addWidget(buttonTest2)
        boxLayout.addWidget(buttonTest3)
        boxLayout.addWidget(buttonTest4)
        boxLayout.addWidget(buttonExit)

        gridLayout.addLayout(boxLayout,3,0,1,3)
        gridLayout.addWidget(buttonExit,3,0,1,3)

        self.setLayout(gridLayout)

        buttonExit.clicked.connect(self.closeApp)

        self.setGeometry(500,500,1000,100)
        self.setWindowIcon(QIcon('test.png'))
        self.setWindowTitle("Model testing")
        self.show()


    def closeApp(self):
        self.close()


    def closeEvent(self,event):
        choice=QMessageBox.question(
            self,'Exit message',
            "Are you sure?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No)

        if choice==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self,e):
        if e.key()==Qt.Key_Escape:
            self.close()



if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=Application()
    sys.exit(app.exec_())
