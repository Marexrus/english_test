import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMainWindow
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QFont,QIcon,QPixmap
from static.window import *
from static.styles import *
from windows.verbHelp import *
from windows.mixed_window import *


class InfinitiveWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Infinitive Test")
        self.setGeometry(300, 300, window_size[0], window_size[1])

        self.label = QLabel("Это окно для теста Infinitive", self)
        self.label.setFont(QFont("Times", 40))
        self.label.move(100,100)


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Тест")
        self.setGeometry(500, 250, window_size[0],window_size[1])
        self.setFixedSize(window_size[0],window_size[1])
        self.background=QLabel(self)
        self.pixmap = QPixmap("resources/background.png")
        self.background.setPixmap(self.pixmap)
        self.background.setScaledContents(True)
    
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.main_l = QLabel(self)
        self.main_l.setText("Тест на знание времен")
        self.main_l.setFont(QFont("Times", 50))
        self.main_l.move((window_size[0] - 670) // 2, 60)
        #self.main_l.setStyleSheet(default_text)

        self.button4=QPushButton("Начать тест", self)
        self.button4.setFont(QFont("Times", 14))
        self.button4.setGeometry(260, 205, 380, 110)
        self.button4.setStyleSheet(button_style_go)
        self.button4.clicked.connect(self.openMixed)

        self.button4=QPushButton("Present S1mple", self)
        self.button4.setFont(QFont("Times", 14))
        self.button4.setGeometry(120, 400, 290, 80)
        self.button4.setStyleSheet(button_style)
        self.button4.clicked.connect(self.openPresentSimple)

        self.button4=QPushButton("Past Simple", self)
        self.button4.setFont(QFont("Times", 14))
        self.button4.setGeometry(490, 400, 290, 80)
        self.button4.setStyleSheet(button_style)
        self.button4.clicked.connect(self.openPastSimple)

        self.button4=QPushButton("Present Perfect", self)
        self.button4.setFont(QFont("Times", 14))
        self.button4.setGeometry((window_size[0] - 320) // 2, window_size[1] - 200, 320, 80)
        self.button4.setStyleSheet(button_style)
        self.button4.clicked.connect(self.openPresentPerfect)

        self.verbButton=QPushButton("Неправильные глаголы", self)
        self.verbButton.setFont(QFont("Times", 8))
        self.verbButton.setGeometry((window_size[0] - 420) // 2, window_size[1] - 100, 420, 80)
        self.verbButton.setStyleSheet(button_style)
        self.button4.setFont(QFont("Times", 40))
        self.verbButton.clicked.connect(self.openVerbHelp)

        self.closeButton=QPushButton(self)
        self.closeButton.setGeometry(window_size[0]-80,window_size[1]-80,70,70)
        self.closeButton.setIcon(QIcon("resources/button_close.png"))
        self.closeButton.setIconSize(QSize(70,70))
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setStyleSheet("""QPushButton{border:0;}""")

    def openVerbHelp(self):
        self.verbHelp = verbHelp()
        self.verbHelp.show()
    
    def openMixed(self):
        self.mixedWindow = mixed_window()
        self.mixedWindow.show()
        
    def openPresentSimple(self):
        self.presentSimpleWindow = ...
        self.presentSimpleWindow.show()

    def openPastSimple(self):
        self.pastSimpleWindow = ...
        self.pastSimpleWindow.show()
    
    def openPresentPerfect(self):
        self.presentPerfectWindow = ...
        self.presentPerfectWindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())