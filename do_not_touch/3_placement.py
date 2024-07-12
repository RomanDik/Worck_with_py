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
    QWidget,
    QGridLayout
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

        layout = QGridLayout()

        layout.addWidget(Color('red'), 1, 1)
        layout.addWidget(Color('green'), 0, 0)
        layout.addWidget(Color('blue'), 2, 2)
        layout.addWidget(Color('purple'), 3, 3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()
    app.exec()