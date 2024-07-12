from random import choice
from PySide6.QtCore import Qt,QSize
from PySide6.QtGui import QMouseEvent, QAction, QPalette, QColor
from PySide6.QtWidgets import (
    QMenu,
    QApplication,
    QListWidget,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QHBoxLayout,
    QWidget
)
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):  
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("кальклюкатор")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        combobox = QComboBox()

        combobox.addItems(["One", "Two", "Three"])
        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        combobox.currentIndexChanged.connect(self.index_changed)

        # The same signal can send a text string
        combobox.currentTextChanged.connect(self.text_changed)

       
        layout1.addLayout( layout2 )
        # layout1.addWidget(combobox)
        layout1.addWidget(Color('green'))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))

        layout1.addLayout( layout3 )

        widget = QWidget()
        widget.setLayout(layout1)
        self.setMenuWidget( combobox)
        self.setCentralWidget(widget)

    def index_changed(self, index):  # index is an int stating from 0
            print(index)

    def text_changed(self, text):  # text is a str
            print(text)
if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()
    app.exec()