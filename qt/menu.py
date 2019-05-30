import sys, os
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QGroupBox, QApplication, QWidget, QPushButton, QAction, QMessageBox, QLabel, QVBoxLayout, QHBoxLayout, QDialog, QFormLayout, QLineEdit, QDialogButtonBox
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import pyqtSlot, Qt
from testers.tester import Tester
from qt.view import App as View
from qt.loading import App as Loading
from qt.results import App as Results
import time
import platform
if platform.system() == 'Linux':
    sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'testers'))
    from tester import Tester
else:
    from testers.tester import Tester

class Application(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'Model testing'
        self.windowIcon = QIcon('qt/test.png')

        self.left = 450
        self.top = 150
        self.width = 100
        self.height = 100

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.windowIcon)

        self.setGeometry(self.left, self.top, self.width, self.height)
        
        vbox = QVBoxLayout()


        title = QLabel()
        title.setText("WALIDATOR")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        vbox.addWidget(title)
        
        repetitionBox = QHBoxLayout()
        self.textbox = QLineEdit(self)
        self.textbox.setFixedWidth(100)
        repetitionInfo = QLabel()
        repetitionInfo.setText("Number of repetitions")
        repetitionBox.addWidget(repetitionInfo)
        repetitionBox.addWidget(self.textbox)
        vbox.addLayout(repetitionBox)

        imageAmountBox = QHBoxLayout()
        self.imagebox = QLineEdit(self)
        self.imagebox.setFixedWidth(100)
        imageAmountInfo = QLabel()
        imageAmountInfo.setText("Number of images")
        imageAmountBox.addWidget(imageAmountInfo)
        imageAmountBox.addWidget(self.imagebox)
        vbox.addLayout(imageAmountBox)

        for i in [1, 4, 6, 8, 10]:
            buttonRun = self.createRunButton(i)
            buttonInfo = self.createInfoButton(i)

            label = QLabel()
            label.setText("Test IMO"+str(i))
        
            hbox = QHBoxLayout()
            hbox.addWidget(label)
            hbox.addWidget(buttonRun)
            hbox.addWidget(buttonInfo)
            vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.show()

    def createRunButton(self, number):
        button = QPushButton(" Run")
        button.clicked.connect(lambda: self.runTest(number))
        icon = QIcon('qt/go.png')
        button.setIcon(icon)
        return button

    def createInfoButton(self, number):
        button = QPushButton("See info")
        button.clicked.connect(lambda: self.fileContent("tests/testimo" + str(number) + ".txt", number))
        return button

    @pyqtSlot()
    def fileContent(self, f, number):
        text = open(f, "r")
        if text.mode == "r":
            data=text.read()
        msg = QMessageBox(self)
        msg.setWindowTitle("Test IMO" + str(number) + " description")
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

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Escape:
            self.close()

    
    def windowLoadingOpen(self):
        self.w = Loading()
        self.w.show()
    
    def windowLoadingClose(self):
        self.w.close()

    def windowResults(self, results, repetitions, images):
        self.w = Results(results, repetitions, images)
        self.w.show()

    @pyqtSlot()
    def runTest(self, testNumber):
        print('Running...')
        
        #self.windowLoadingOpen()
        start = time.perf_counter()
        results = self.runTester(testNumber, int(self.textbox.text()), int(self.imagebox.text()))
        end = time.perf_counter()
        print("Elapsed time: ", end-start, "s")
        #self.windowLoadingClose()
        self.windowResults(results, int(self.textbox.text()), int(self.imagebox.text()))

        print('Done!')
    
    def runTester(self, testNumber, repetitions, images):
        t = Tester(testNumber, repetitions, images)
        return t.run()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())
