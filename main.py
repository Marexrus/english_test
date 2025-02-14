import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QTextEdit, QLineEdit

class MoodApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Тест")
        self.setGeometry(200, 200, 800, 600)

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MoodApp()
    ex.show()
    sys.exit(app.exec_())