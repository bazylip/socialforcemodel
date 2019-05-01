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

        buttonTest1.clicked.connect(self.action)
        buttonTest2.clicked.connect(self.action)
        buttonTest3.clicked.connect(self.action)
        buttonTest4.clicked.connect(self.action)
        buttonExit.clicked.connect(self.closeApp)

        self.setGeometry(500,500,1000,100)
        self.setWindowIcon(QIcon('test.png'))
        self.setWindowTitle("Model testing")
        self.show()


    def closeApp(self):
        self.close()


    def action(self):
        sender_=self.sender()
        try:
            if sender_.text()=="Test 1":
                QMessageBox.about(self,"Test message","Test 1 will start in a moment...")
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
