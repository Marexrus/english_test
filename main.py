import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QTextEdit, QLineEdit
from PyQt5.QtGui import QFont

window_size=[900,700]

button_style="""
            QPushButton {
                background-color: #7226EB; /* Зеленый цвет фона */
                border: none; /* Убираем границу */
                color: white; /* Белый цвет текста */
                padding: 15px 32px; /* Отступы внутри кнопки */
                text-align: center; /* Выравнивание текста по центру */
                text-decoration: none; /* Убираем подчеркивание текста */
                font-size: 40px; /* Размер шрифта */
                border-radius: 24px; /* Скругление углов */
            }
            QPushButton:hover {
                background-color: #571DB5; /* Цвет фона при наведении */
            }
            QPushButton:pressed {
                background-color: #3E3E3E; /* Цвет фона при нажатии */
            }
        """

class MoodApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Тест")
        self.setGeometry(300, 300,window_size[0],window_size[1])

        self.main_l=QLabel(self)
        self.main_l.setText("Выберите тест")
        self.main_l.setFont(QFont("Times", 60))
        self.main_l.move(int((window_size[0]/2)-(self.main_l.width()*1.8)),20)

        self.button1=QPushButton(self)
        self.button1.setText("Infinitive")
        self.button1.setFont(QFont("Times", 16))
        self.button1.setGeometry(150,200,300,80)
        self.button1.setStyleSheet(button_style)

        self.button2=QPushButton(self)
        self.button2.setText("Past Simple")
        self.button2.setFont(QFont("Times", 16))
        self.button2.setGeometry(450,200,300,80)
        self.button2.setStyleSheet(button_style)

        self.button3=QPushButton(self)
        self.button3.setText("Past Participle")
        self.button3.setFont(QFont("Times", 16))
        self.button3.setGeometry(150,400,300,80)
        self.button3.setStyleSheet(button_style)

        self.button4=QPushButton(self)
        self.button4.setText("Смешанный")
        self.button4.setFont(QFont("Times", 16))
        self.button4.setGeometry(450,400,300,80)
        self.button4.setStyleSheet(button_style)

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MoodApp()
    ex.show()
    sys.exit(app.exec_())