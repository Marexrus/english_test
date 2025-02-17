from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QGridLayout
from static.window import *
from static.styles import *
from verbs.verbs import *

for el in Array:
   print(f"{el.inf}--{el.PastSimple}--{el.PastPart}--{el.Translate}")

print(len(Array))

class verbHelp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Памятка")
        self.setGeometry(150, 150, window_size[0]+200, window_size[1]+100)
        self.setStyleSheet(background_window)
        self.grid=QGridLayout(self)

        self.row=0
        self.col=0
        for i in range(len(Array)):
            self.row=i // 3
            self.col=i % 3
            self.label=QLabel(self)
            self.label.setText(f"{Array[i].Translate}-{Array[i].inf}-{Array[i].PastSimple}-{Array[i].PastPart}")
            self.label.setStyleSheet(verbLabel)
            self.grid.addWidget(self.label,self.row,self.col)
        
        self.backButton=QPushButton(self)
        self.backButton.setText("Назад")
        self.grid.addWidget(self.backButton,self.row,self.col+1)
        self.backButton.setStyleSheet(button_back_style)
        self.backButton.setFixedSize(150,60)
        self.backButton.clicked.connect(self.back)
        
        self.setLayout(self.grid)

    def back(self):
        self.hide()
