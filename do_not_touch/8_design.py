from random import choice, randint
# from layout_colorwidget import Color
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import (
    QMouseEvent,
    QKeySequence, 
    QAction, 
    QPalette, 
    QColor, 
    QIcon
    )
from PySide6.QtWidgets import (
    QMenu,
    QApplication,
    QListWidget,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDialog,
    QDialogButtonBox,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QTabWidget,
    QToolBar, 
    QStatusBar,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QGridLayout,
    QStackedLayout,
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
        # self.setFixedSize(QSize(650, 500))
        self.setWindowTitle("кальклюкатор")
        self.x = '0'
        self.num = 0
        self.label1 = QLabel()
        self.label1.setAlignment(Qt.AlignRight)
        self.label2 = QLabel()
        self.label2.setAlignment(Qt.AlignRight)

        labels = QVBoxLayout()
        labels.addWidget(self.label1)
        labels.addWidget(self.label2)

        layout_butt = QGridLayout()
        

        button_1 = QPushButton("1")
        button_2 = QPushButton("2")
        button_3 = QPushButton("3")
        button_4 = QPushButton("4")
        button_5 = QPushButton("5")
        button_6 = QPushButton("6")
        button_7 = QPushButton("7")
        button_8 = QPushButton("8")
        button_9 = QPushButton("9")
        button_10 = QPushButton("+")
        button_11 = QPushButton("-")
        button_12 = QPushButton("=")
        button_13 = QPushButton("*")
        button_14 = QPushButton("/")
        button_15 = QPushButton("0")
        button_16 = QPushButton("C")
        button_17 = QPushButton("+/-")
        button_18 = QPushButton(".")

        button_1.clicked.connect(self.the_button_1_was_clicked)
        button_2.clicked.connect(self.the_button_2_was_clicked)
        button_3.clicked.connect(self.the_button_3_was_clicked)
        button_4.clicked.connect(self.the_button_4_was_clicked)
        button_5.clicked.connect(self.the_button_5_was_clicked)
        button_6.clicked.connect(self.the_button_6_was_clicked)
        button_7.clicked.connect(self.the_button_7_was_clicked)
        button_8.clicked.connect(self.the_button_8_was_clicked)
        button_9.clicked.connect(self.the_button_9_was_clicked)
        button_10.clicked.connect(self.the_button_10_was_clicked)
        button_11.clicked.connect(self.the_button_11_was_clicked)
        button_12.clicked.connect(self.the_button_12_was_clicked)
        button_13.clicked.connect(self.the_button_13_was_clicked)
        button_14.clicked.connect(self.the_button_14_was_clicked)
        button_15.clicked.connect(self.the_button_15_was_clicked)
        button_16.clicked.connect(self.the_button_16_was_clicked)
        button_17.clicked.connect(self.the_button_17_was_clicked)
        button_18.clicked.connect(self.the_button_18_was_clicked)

        layout_butt.addWidget(button_1, 1, 0)
        layout_butt.addWidget(button_4, 2, 0)
        layout_butt.addWidget(button_7, 3, 0)
        layout_butt.addWidget(button_17, 4, 0)
        layout_butt.addWidget(button_2, 1, 1)
        layout_butt.addWidget(button_5, 2, 1)
        layout_butt.addWidget(button_8, 3, 1)
        layout_butt.addWidget(button_15, 4, 1)
        layout_butt.addWidget(button_16, 0, 2)
        layout_butt.addWidget(button_3, 1, 2)
        layout_butt.addWidget(button_6, 2, 2)
        layout_butt.addWidget(button_9, 3, 2)
        layout_butt.addWidget(button_18, 4, 2)
        layout_butt.addWidget(button_14, 0, 3)
        layout_butt.addWidget(button_13, 1, 3)
        layout_butt.addWidget(button_11, 2, 3)
        layout_butt.addWidget(button_10, 3, 3)
        layout_butt.addWidget(button_12, 4, 3)

        widget1 = QWidget()
        widget1.setLayout(layout_butt)
        widget2 = QWidget()
        widget2.setLayout(labels)

        self.setMenuWidget(widget2)
        self.setCentralWidget(widget1)

        # self.setCentralWidget(self.input)

    def the_button_1_was_clicked(self):
        if self.x == "0":
            self.x = "1"
            self.label2.setText(self.x)
            self.num = 1
        else:
            self.x = self.x + "1"
            self.label2.setText(self.x)
            self.num = self.num + 1
    def the_button_2_was_clicked(self):
        if self.x == "0":
            self.x = "2"
            self.label2.setText(self.x)
        else:
            self.x = self.x + "2"
            self.label2.setText(self.x)
    def the_button_3_was_clicked(self):
        if self.x == "0":
            self.x = "3"
            self.label2.setText(self.x)
        else:
            self.x = self.x + "3"
            self.label2.setText(self.x)
    def the_button_4_was_clicked(self):
        if self.x == "0":
            self.x = "4"
            self.label2.setText(self.x)
        else:
            self.x = self.x + "4"
            self.label2.setText(self.x)
    def the_button_5_was_clicked(self):
        if self.x == "0":
            self.x = "5"
            self.label2.setText(self.x)
        else:
            self.x = self.x + "5"
            self.label2.setText(self.x)
    def the_button_6_was_clicked(self):
        if self.x == "0":
            self.x = "6"
            self.label2.setText(self.x)
        else:
            self.x = self.x + "6"
            self.label2.setText(self.x)
    def the_button_7_was_clicked(self):
        if self.x == "0":
            self.x = "7"
            self.label2.setText(self.x)
        else:
            self.x = self.x + "7"
            self.label2.setText(self.x)
    def the_button_8_was_clicked(self):
        if self.x == "0":
            self.x = "8"
            self.label2.setText(self.x)
        else:
            self.x = self.x + "8"
            self.label2.setText(self.x)
    def the_button_9_was_clicked(self):
        if self.x == "0":
            self.x = "9"
            self.label2.setText(self.x)
        else:
            self.x = self.x + "9"
            self.label2.setText(self.x)
    def the_button_10_was_clicked(self):
            self.x = self.x + "+"
            self.label2.setText(self.x)
    def the_button_11_was_clicked(self):
            self.x = self.x + "-"
            self.label2.setText(self.x)
    def the_button_12_was_clicked(self):
            self.x = self.x + "="
            self.label2.setText(self.x)
    def the_button_13_was_clicked(self):
            self.x = self.x + "*"
            self.label2.setText(self.x)
    def the_button_14_was_clicked(self):
            self.x = self.x + "/"
            self.label2.setText(self.x)
    def the_button_15_was_clicked(self):
        if self.x == "0":
            self.label2.setText(self.x)
        else:
            self.x = self.x + "0"
            self.label2.setText(self.x)
    def the_button_16_was_clicked(self):
            self.x = "0"
            self.label2.setText(self.x)
    def the_button_17_was_clicked(self):
        if self.x == "0":
            self.label2.setText(self.x)
        else:
            self.x = self.x * (-1)
            self.label2.setText(self.x)
    def the_button_18_was_clicked(self):
            self.x = self.x + "."
            self.label2.setText(self.x)


if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()
    app.exec()