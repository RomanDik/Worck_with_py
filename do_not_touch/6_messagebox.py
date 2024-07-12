from random import choice
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

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class MainWindow(QMainWindow):  
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(QSize(650, 500))
        self.setWindowTitle("кальклюкатор")
# //////////////////////////////////////////////////////////////////////
        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):

        button = QMessageBox.critical(
            self,
            "Oh dear!",
            "Something went very wrong.",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard,
        )

        if button == QMessageBox.Discard:
            print("Discard!")
        elif button == QMessageBox.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")
    
# //////////////////////////////////////////////////////////////////////
if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()
    app.exec()