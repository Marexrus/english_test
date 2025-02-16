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
        self.grid=QGridLayout(self)

        for i in range(len(Array)):
            self.row=i // 3
            self.col=i % 3
            self.label=QLabel(self)
            self.label.setText(f"{Array[i].Translate}-{Array[i].inf}-{Array[i].PastSimple}-{Array[i].PastPart}")
            self.label.setStyleSheet(verbLabel)
            self.grid.addWidget(self.label,self.row,self.col)
        
        self.setLayout(self.grid)

        self.setWindowTitle("Памятка")
        self.setGeometry(150, 150, window_size[0]+200, window_size[1]+100)
        self.setStyleSheet(background_window)
