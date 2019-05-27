import sys, os
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QMessageBox, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
from testers.tester import Tester
from PyQt5.QtGui import QPixmap
from qt.p import App
import platform
if platform.system() == 'Linux':
    sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'testers'))
    from tester import Tester
else:
    from testers.tester import Tester

class Application(QMainWindow):

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
        action1 = test1.addAction("View description")
        action1.setShortcut("CTRL+1")
        action1.triggered.connect(lambda: self.fileContent("tests/testimo1.txt","1"))
        action1a = test1.addAction("Run test")
        action1a.setShortcut("CTRL+SHIFT+1")
        t1 = Tester(1)
        action1a.triggered.connect(lambda: t1.run())
        action1b = test1.addAction("View simulation")
        action1b.setShortcut("CTRL+F1")
        action1b.triggered.connect(lambda: self.windowTest())

        test4 = menu.addMenu('Test 4')
        action4 = test4.addAction("View description")
        action4.setShortcut("CTRL+2")
        action4.triggered.connect(lambda: self.fileContent("tests/testimo4.txt","4"))
        action2a = test4.addAction("Run test")
        action2a.setShortcut("CTRL+SHIFT+2")
        t4 = Tester(4)
        action2a.triggered.connect(lambda: t4.run())
        action2b = test4.addAction("View simulation")
        action2b.setShortcut("CTRL+F2")
        action2b.triggered.connect(lambda: self.windowTest())

        test6 = menu.addMenu('Test 6')
        action6 = test6.addAction("View description")
        action6.setShortcut("CTRL+3")
        action6.triggered.connect(lambda: self.fileContent("tests/testimo6.txt","6"))
        action3a = test6.addAction("Run test")
        action3a.setShortcut("CTRL+SHIFT+3")
        t6 = Tester(6)
        action3a.triggered.connect(lambda: t6.run())
        action3b = test6.addAction("View simulation")
        action3b.setShortcut("CTRL+F3")
        action3b.triggered.connect(lambda: self.windowTest())

        test8 = menu.addMenu('Test 8')
        action8 = test8.addAction("View description")
        action8.setShortcut("CTRL+4")
        action8.triggered.connect(lambda: self.fileContent("tests/testimo8.txt","8"))
        action4a = test8.addAction("Run test")
        action4a.setShortcut("CTRL+SHIFT+4")
        t8 = Tester(8)
        action4a.triggered.connect(lambda: t8.run())
        action4b = test8.addAction("View simulation")
        action4b.setShortcut("CTRL+F4")
        action4b.triggered.connect(lambda: self.windowTest())

        test10 = menu.addMenu('Test10')
        action10 = test10.addAction("View description")
        action10.setShortcut("CTRL+5")
        action10.triggered.connect(lambda: self.fileContent("tests/testimo10.txt","10"))
        action5a = test10.addAction("Run test")
        action5a.setShortcut("CTRL+SHIFT+5")
        t10 = Tester(10)
        action5a.triggered.connect(lambda: t10.run())
        action5b = test10.addAction("View simulation")
        action5b.setShortcut("CTRL+F5")
        action5b.triggered.connect(lambda: self.windowTest())

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

    #def keyPressEvent(self, e):
        #if e.key() == Qt.Key_Escape:
        #    self.close()

    def windowTest(self):
        self.w = App()
        self.w.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())
