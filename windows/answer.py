from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QGridLayout
from static.window import *
from static.styles import *
from PyQt5.QtGui import QPalette, QColor, QFont
from modules.check import Array
#from verbs.verbs import *

for el in Array:
   print(f"{el.inf}--{el.PastSimple}--{el.PastPart}--{el.Translate}")

print(len(Array))

class AnswerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ответы")
        self.setGeometry(500, 50, window_size[0],window_size[1]+200)
        self.setFixedSize(window_size[0],window_size[1]+200)
        self.setStyleSheet(background_window)
        self.grid=QGridLayout(self,spacing=0)
        self.grid.setSpacing(0)

        self.row=0
        self.col=0
        self.correctAnswer=0
        for i in range(len(Array)):
            self.row=i // 2
            self.col=i % 2
            self.label=QLabel(self)
            self.label.setText("{}--{}".format(Array[i].question,Array[i].answer))
            self.label.setStyleSheet(verbLabel)
            self.label.setMaximumHeight(70)
            self.grid.addWidget(self.label,self.row,self.col)

            self.redColor=self.label.palette()
            self.redColor.setColor(QPalette.WindowText,QColor(255,0,0))
            self.greenColor=self.label.palette()
            self.greenColor.setColor(QPalette.WindowText,QColor(0,216,0))

            if Array[i].is_right:
                self.label.setPalette(self.greenColor)
                self.correctAnswer+=1
            if not Array[i].is_right:
                self.label.setPalette(self.redColor)
    
        self.backButton=QPushButton(self)
        self.backButton.setText("Назад")
        self.grid.addWidget(self.backButton,self.row,self.col+1)
        self.backButton.setStyleSheet(button_back_style)
        self.backButton.setFixedSize(150,60)
        self.backButton.clicked.connect(self.back)
        
        self.setLayout(self.grid)

        self.setWindowTitle("{} правильных ответов".format(self.correctAnswer))

    def back(self):
        self.hide()
