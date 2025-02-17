from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QGridLayout
from static.window import *
from static.styles import *
from PyQt5.QtGui import QPalette, QColor
#from verbs.verbs import *

Array=[]

for el in Array:
   print(f"{el.inf}--{el.PastSimple}--{el.PastPart}--{el.Translate}")

print(len(Array))

class AnswerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Памятка")
        self.setGeometry(500, 250, window_size[0],window_size[1])
        self.setFixedSize(window_size[0],window_size[1])
        self.setStyleSheet(background_window)
        self.grid=QGridLayout(self)

        self.row=0
        self.col=0
        for i in range(len(Array)):
            self.row=i // 3
            self.col=i % 3
            self.label=QLabel(self)
            self.label.setText(Array[i][0])
            self.label.setStyleSheet(verbLabel)
            self.grid.addWidget(self.label,self.row,self.col)

            self.redColor=self.label.pallet()
            self.redColor.setColor(QPalette.windowText,QColor(255,0,0))
            self.greenColor=self.label.pallet()
            self.greenColor.setColor(QPalette.windowText,QColor(0,255,0))

            if Array[1][1]:
                self.label.setPalette(self.greenColor)
            if not Array[1][1]:
                self.label.setPalette(self.redColor)
        
        self.backButton=QPushButton(self)
        self.backButton.setText("Назад")
        self.grid.addWidget(self.backButton,self.row,self.col+1)
        self.backButton.setStyleSheet(button_back_style)
        self.backButton.setFixedSize(150,60)
        self.backButton.clicked.connect(self.back)
        
        self.setLayout(self.grid)

    def back(self):
        self.hide()
