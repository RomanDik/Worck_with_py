from random import choice
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget, 
    QPushButton
)
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(400, 300))
        self.setWindowTitle("Калькулятор")
        self.label = QLabel("Nuke click")
        self.setCentralWidget(self.label)

  

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("NukePress LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("NukePress MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("NukePress RIGHT")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("NukeRelease LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("NukeRelease MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("NukeRelease RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("NukeDouble LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("NukeDouble MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("NukeDouble RIGHT")



if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()
    app.exec()