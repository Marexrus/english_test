from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtGui import QFont,QIcon,QPixmap
from PyQt5.QtCore import Qt,QSize

window_size = [900,700]

class presentSimple(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Памятка Present Simple")
        self.setFixedSize(window_size[0],window_size[1])
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.label = QLabel(self)
        pixmap = QPixmap("resources/PST.png")
        scaled_pixmap = pixmap.scaled(window_size[0], window_size[1], Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.label.setPixmap(scaled_pixmap)

        self.closeButton=QPushButton(self)
        self.closeButton.setGeometry(window_size[0]-80,window_size[1]-80,70,70)
        self.closeButton.setIcon(QIcon("resources/button_close.png"))
        self.closeButton.setIconSize(QSize(70,70))
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setStyleSheet("""QPushButton{border:0;}""")