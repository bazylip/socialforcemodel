import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QMessageBox
from PyQt5.QtGui import QIcon

class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = 'Model testing'
        self.windowIcon = QIcon('qt/test.png')

        self.left = 600
        self.top = 380
        self.width = 400
        self.height = 400

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.windowIcon)

        self.setGeometry(self.left, self.top, self.width, self.height)


        menu = self.menuBar()

        test1 = menu.addMenu('Test 1')
        action1=test1.addAction("View description")
        action1.setShortcut("CTRL+1")
        action1.triggered.connect(lambda: self.fileContent("tests/testimo1.txt","1"))

        test4 = menu.addMenu('Test 4')
        action4 = test4.addAction("View description")
        action4.setShortcut("CTRL+2")
        action4.triggered.connect(lambda: self.fileContent("tests/testimo4.txt","4"))

        test6= menu.addMenu('Test 6')
        action6 = test6.addAction("View description")
        action6.setShortcut("CTRL+3")
        action6.triggered.connect(lambda: self.fileContent("tests/testimo6.txt","6"))

        test8 = menu.addMenu('Test 8')
        action8 = test8.addAction("View description")
        action8.setShortcut("CTRL+4")
        action8.triggered.connect(lambda: self.fileContent("tests/testimo8.txt","8"))

        test10 = menu.addMenu('Test10')
        action10 = test10.addAction("View description")
        action10.setShortcut("CTRL+5")
        action10.triggered.connect(lambda: self.fileContent("tests/testimo10.txt","10"))

        self.show()

    def fileContent(self,file,number):
        text = open(file, "r")
        if text.mode == "r":
            data=text.read()
        msg = QMessageBox(self)
        msg.setWindowTitle("Test "+number+" description")
        msg.setText(data)
        msg.show()

    def closeEvent(self, event):
        choice = QMessageBox.question(
            self, 'Exit message',
            "Are you sure?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No)

        if choice == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
