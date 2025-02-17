import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMainWindow
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QFont,QIcon,QPixmap
from static.window import *
from static.styles import *
from windows.verbHelp import *
from windows.infinitive_window import *


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
        self.main_l.setText("Выберите тест")
        self.main_l.setFont(QFont("Times", 70))
        self.main_l.move(int((window_size[0] // 2) - (self.main_l.width() * 3)), 60)
        #self.main_l.setStyleSheet(default_text)

        self.button1 = QPushButton(self)
        self.button1.setText("Infinitive")
        self.button1.setFont(QFont("Times", 16))
        self.button1.setGeometry(90, 280, 320, 80)
        self.button1.setStyleSheet(button_style)
        self.button1.clicked.connect(self.openInfinitive)

        self.button2 = QPushButton(self)
        self.button2.setText("Past Simple")
        self.button2.setFont(QFont("Times", 16))
        self.button2.setGeometry(500, 280, 320, 80)
        self.button2.setStyleSheet(button_style)

        self.button3 = QPushButton(self)
        self.button3.setText("Past Participle")
        self.button3.setFont(QFont("Times", 16))
        self.button3.setGeometry(90, 400, 320, 80)
        self.button3.setStyleSheet(button_style)

        self.button4=QPushButton("Смешанный", self)
        self.button4.setFont(QFont("Times", 16))
        self.button4.setGeometry(500, 400, 320, 80)
        self.button4.setStyleSheet(button_style)

        self.verbButton=QPushButton("Неправильные глаголы", self)
        self.verbButton.setFont(QFont("Times", 8))
        self.verbButton.setGeometry((window_size[0] - 500) // 2, window_size[1] - 150, 500, 80)
        self.verbButton.setStyleSheet(button_style)
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
    
    def openInfinitive(self):
        self.infinitive_window = infinitive_window()
        self.infinitive_window.show()

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())