from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from static.window import *
from static.styles import *


class infinitive_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(" Инфинитив")
        self.setGeometry(150, 150, window_size[0]+200, window_size[1]+100)
        self.setStyleSheet(background_window)
