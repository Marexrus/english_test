from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit 
from static.window import *
from static.styles import *
from PyQt5.QtGui import QFont,QPixmap
from PyQt5.QtCore import Qt


class infinitive_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(" Инфинитив")
        self.setGeometry(500, 250, window_size[0], window_size[1])
        self.background=QLabel(self)
        self.pixmap = QPixmap("resources/background-questions.png")
        self.background.setPixmap(self.pixmap)
        self.background.setScaledContents(True)
        #self.setStyleSheet(background_window)

        self.QuestionL=QLabel(self)
        self.QuestionL.setText('Вопрос 1 из 15')
        self.QuestionL.setFont(QFont("Times", 40))
        self.QuestionL.setGeometry((window_size[0] - 900) // 2, 40, 900, 60)
        self.QuestionL.setStyleSheet("""background-color:#131313; color:white;""")
        self.QuestionL.setAlignment(Qt.AlignCenter)

        self.QuestionEnL=QLabel(self)
        self.QuestionEnL.setText('CHECK')
        self.QuestionEnL.setFont(QFont("Times", 35))
        self.QuestionEnL.setGeometry((window_size[0] - 900) // 2, 120, 900, 60)
        self.QuestionEnL.setStyleSheet("""background-color:#131313; color:white;""")
        self.QuestionEnL.setAlignment(Qt.AlignCenter)

        self.QuestionRusL=QLabel(self)
        self.QuestionRusL.setText('CHECK')
        self.QuestionRusL.setFont(QFont("Times", 30))
        self.QuestionRusL.setGeometry((window_size[0] - 900) // 2, 200, 900, 60)
        self.QuestionRusL.setStyleSheet("""background-color:rgba(19,19,19,0.75); color:white;""")
        self.QuestionRusL.setAlignment(Qt.AlignCenter)


        self.line=QLineEdit(self)
        self.line.setGeometry((window_size[0] - 700) // 2, 280, 700, 60)
        self.line.setStyleSheet("""font-size:40px;  border:0;""")
        self.line.setAlignment(Qt.AlignCenter)

        self.nextButton=QPushButton(self)
        self.nextButton.setText("Дальше")
        self.nextButton.move((window_size[0] - 200) // 2, 380)
        self.nextButton.setStyleSheet(button_next_style)
        self.nextButton.setFixedSize(200,70)
        self.nextButton.clicked.connect(self.next)


        self.backButton=QPushButton(self)
        self.backButton.setText("Назад")
        self.backButton.move(window_size[0]-160,window_size[1]-70 )
        self.backButton.setStyleSheet(button_back_style)
        self.backButton.setFixedSize(150,60)
        self.backButton.clicked.connect(self.back)
    
    def back(self):
        self.hide()
    
    def next(self):
        pass
