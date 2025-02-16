from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from static.window import *
from static.styles import *


class infinitive_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(" Инфинитив")
        self.setGeometry(500, 250, window_size[0], window_size[1])
        self.setStyleSheet(background_window)

        self.QuestionL=QLabel(self)
        self.QuestionL.setText('CHECK')

        self.backButton=QPushButton(self)
        self.backButton.setText("Назад")
        self.backButton.move(window_size[0]-160,window_size[1]-70)
        self.backButton.setStyleSheet(button_back_style)
        self.backButton.setFixedSize(150,60)
        self.backButton.clicked.connect(self.back)
    
    def back(self):
        self.hide()
