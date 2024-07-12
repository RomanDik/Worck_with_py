from random import choice
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from PySide6.QtCore import QSize

window_titles = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "Nuke",
]
class MainWindow(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.n_time_clicked=0
        self.setWindowTitle("Калькулятор")
        self.button = QPushButton("Не нажимать")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setFixedSize(QSize(400, 300))
        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Nuked!")
        new_window_title = choice(window_titles)
        print("setting title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("Window title changed to: %s" % window_title)
            
        if window_title == "Nuke":
            self.button.setDisabled(True)
           









if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()
    app.exec()