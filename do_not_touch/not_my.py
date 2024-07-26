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
    QFrame,
    QSizePolicy
)
# class Color(QWidget):

#     def __init__(self, color):
#         super(Color, self).__init__()
#         self.setAutoFillBackground(True)
#         palette = self.palette()
#         palette.setColor(QPalette.Window, QColor(color))
#         self.setPalette(palette)

class CustomQPushButton(QPushButton):
    def __init__(self, text, parent):
        super().__init__(text, parent=parent)
        self.setMouseTracking(True)
        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.label1 = self.parent().label1
        self.label2 = self.parent().label2
        self.label3 = self.parent().label3
        self.label4 = self.parent().label4
        self.label5 = self.parent().label5
        self.label6 = self.parent().label6
        self.label7 = self.parent().label7
        self.label8 = self.parent().label8
        self.label9 = self.parent().label9
        self.label10 = self.parent().label10
        self.label11 = self.parent().label11
        self.label12 = self.parent().label12
        self.label13 = self.parent().label13
        self.label14 = self.parent().label14
        self.label15 = self.parent().label15
        self.label16 = self.parent().label16
        self.label17 = self.parent().label17
        self.label18 = self.parent().label18
        self.label19 = self.parent().label19
        self.label20 = self.parent().label20
        
       
    def mousePressEvent(self, e: QMouseEvent) -> None:
        

        return super().mousePressEvent(e)

class MainWindow(QMainWindow):  
    def __init__(self):
        super(MainWindow, self).__init__()
        # self.setFixedSize(QSize(650, 500))
        self.setWindowTitle("...")
        self.full_formula = QLabel()
        self.full_formula.setFixedWidth(300)
        self.full_formula.setAlignment(Qt.AlignRight)
        self.alone_sign = QLabel()
        self.alone_sign.setAlignment(Qt.AlignRight)
        self.alone_sign.setFixedWidth(300)
        self.label1 = QLabel()
        self.label2 = QLabel()
        self.label3 = QLabel()
        self.label4 = QLabel()
        self.label5 = QLabel()
        self.label6 = QLabel()
        self.label7 = QLabel()
        self.label8 = QLabel()
        self.label9 = QLabel()
        self.label10 = QLabel()
        self.label11 = QLabel()
        self.label12 = QLabel()
        self.label13 = QLabel()
        self.label14 = QLabel()
        self.label15 = QLabel()
        self.label16 = QLabel()
        self.label17 = QLabel()
        self.label18 = QLabel()
        self.label19 = QLabel()
        self.label20 = QLabel()
        #main widget
        main_widget = QWidget()
        main_widget.setLayout(QHBoxLayout())

        #labels
        labels_frame = QFrame()
        labels_frame.setLineWidth(3)
        labels_frame.setFrameStyle(QFrame.WinPanel | QFrame.Plain)
        labels_frame.setLayout(QVBoxLayout())
        labels_frame.layout().addWidget(self.label1, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame.layout().addWidget(self.label2, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame.layout().addWidget(self.label3, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame.layout().addWidget(self.label4, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame.layout().addWidget(self.label5, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame.layout().addWidget(self.label6, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame.layout().addWidget(self.label7, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame.layout().addWidget(self.label8, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame.layout().addWidget(self.label9, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame.layout().addWidget(self.label10, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        main_widget.layout().addWidget(labels_frame)


        labels_frame = QFrame()

        layout_butt = QGridLayout()
        layout_butt.addWidget(CustomQPushButton("1-ввести", self), 1, 0)
        layout_butt.addWidget(CustomQPushButton("2-ввести", self), 2, 0)
        layout_butt.addWidget(CustomQPushButton("3-ввести", self), 3, 0)
        layout_butt.addWidget(CustomQPushButton("4-ввести", self), 4, 0)
        layout_butt.addWidget(CustomQPushButton("5-ввести", self), 5, 0)
        layout_butt.addWidget(CustomQPushButton("6-ввести", self), 6, 0)
        layout_butt.addWidget(CustomQPushButton("7-ввести", self), 7, 0)
        layout_butt.addWidget(CustomQPushButton("8-ввести", self), 8, 0)
        layout_butt.addWidget(CustomQPushButton("9-ввести", self), 9, 0)
        layout_butt.addWidget(CustomQPushButton("10-ввести", self), 10, 0)
        layout_butt.addWidget(CustomQPushButton("->", self), 1, 1)
        layout_butt.addWidget(CustomQPushButton("->", self), 2, 1)
        layout_butt.addWidget(CustomQPushButton("->", self), 3, 1)
        layout_butt.addWidget(CustomQPushButton("->", self), 4, 1)
        layout_butt.addWidget(CustomQPushButton("->", self), 5, 1)
        layout_butt.addWidget(CustomQPushButton("->", self), 6, 1)
        layout_butt.addWidget(CustomQPushButton("->", self), 7, 1)
        layout_butt.addWidget(CustomQPushButton("->", self), 8, 1)
        layout_butt.addWidget(CustomQPushButton("->", self), 9, 1)
        layout_butt.addWidget(CustomQPushButton("->", self), 10, 1)
    

        main_widget.layout().addLayout(layout_butt)
        labels_frame2 = QFrame()
        labels_frame2.setLineWidth(3)
        labels_frame2.setFrameStyle(QFrame.WinPanel | QFrame.Plain)
        labels_frame2.setLayout(QVBoxLayout())
        labels_frame2.layout().addWidget(self.label11, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame2.layout().addWidget(self.label12, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame2.layout().addWidget(self.label13, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame2.layout().addWidget(self.label14, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame2.layout().addWidget(self.label15, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame2.layout().addWidget(self.label16, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame2.layout().addWidget(self.label17, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame2.layout().addWidget(self.label18, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame2.layout().addWidget(self.label19, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame2.layout().addWidget(self.label20, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        main_widget.layout().addWidget(labels_frame2)
        self.setCentralWidget(main_widget)


if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()
    app.exec()