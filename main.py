
from random import choice, randint
# from layout_colorwidget import Color
from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QMouseEvent,
    QPalette, 
    QColor
    )
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QFrame
)
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class CustomQPushButton(QPushButton):
    def __init__(self, text, parent):
        """
        Конструктор для создания кнопки с текстом и родительским виджетом.

        Parameters: 
        self: ссылка на текущий экземпляр класса. 
        text: строка, содержащая имя файла JSON для чтения. 
        parent: ссылка на родительские виджеты.

        Returns: 
        None.
        """
        super().__init__(text, parent=parent)
        self.setMouseTracking(True)
        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.full_formula = self.parent().full_formula
        self.alone_sign = self.parent().alone_sign
        self.full_formula.setText("0")
        self.alone_sign.setText("0")
       
    def mousePressEvent(self, e: QMouseEvent) -> None:
        """
        Обработчик события нажатия кнопки мыши.
        Обратыватывает ввод цифр, десятичного разделителя, знака плюс/минус, кнопки очистки поля, и кнопки равно.
        Проверяет длину полей, и если они превышают допустимые значения, не выполняет никаких действий.

        Parameters: 
        self: ссылка на текущий экземпляр класса. 
        e: объект QMouseEvent, который содержит информацию о событии нажатия кнопки мыши

        Returns: 
        None.
        """
        #Условие, при котором после превышения допустимого количества символов, остаються активны только кнопки С и CE
        if self.text() == 'C' or self.text() == 'CE': 
            pass                                      
        else:
            if len(str(self.full_formula.text())) > 40 or len(str(self.alone_sign.text())) > 40:
                return 0
            
        #Условие, при котором точка в одном числе может быть введена только один раз.
        if self.text() == ".":
            if "." in self.alone_sign.text():
                pass
            else:
                self.alone_sign.setText(self.alone_sign.text() + self.text())

        #Если число положительное, добавить - перед этим числом, если же минус уже стоит, то убрать его
        elif self.text() == "+/-":
            if not ("=" in self.alone_sign.text()): #Проверкана то, что перед кнопкой - не была нажата кнопка =
                if self.alone_sign.text()[0] == "-":
                    rem = float(self.alone_sign.text()) * -1
                    self.alone_sign.setText(str(rem))
                else:
                    self.alone_sign.setText("-" + self.alone_sign.text())

        #Если нажатая кнока является числом и перед этим не была нажата кнопка =, то добавить текст с копки в строку одиночного значения (self.alone_sign)
        elif str(self.text()).isdigit():
                if not ("=" in self.alone_sign.text() or (str(self.full_formula.text()[-1]).isdigit() and len(self.full_formula.text())>1)):
                    if self.alone_sign.text() == "0":
                        self.alone_sign.clear()
                    self.alone_sign.setText(self.alone_sign.text() + self.text())
        else:
            # стереть только строку одиночного значения (self.alone_sign)
            if self.text() == 'C':
                self.alone_sign.setText("0")
            # стереть строку одиночного значения (self.alone_sign) и строку всего выражения (self.full_formula)
            elif self.text() == 'CE':
                self.alone_sign.setText("0")
                self.full_formula.setText("0")
            #Если нажата кнопка =
            elif self.text() == '=':
                #Если после точки нет больше чифр, то добавить 0 во избежание непонятных ситуаций
                if self.alone_sign.text()[-1] == ".":
                    self.alone_sign.setText(self.alone_sign.text() + "0")
                #Если в строке всего выражения (self.full_formula) стоит 0, то очистить её.
                if self.full_formula.text() == "0":
                    self.full_formula.clear()
                #Условие, которое при повторном нажатии кнопки = повторяет с итоговым результатом последнюю проведенную операцию в строке всего выражения (self.full_formula)
                if "=" in self.alone_sign.text() and ("+" in self.full_formula.text() or "-" in self.full_formula.text() or "*" in self.full_formula.text() or "/" in self.full_formula.text()):
                    time_alone = ""
                    fin = 0
                    i = len(self.full_formula.text()) - 1
                    while fin == 0:
                        if self.full_formula.text()[i] == "+" or self.full_formula.text()[i] == "-" or self.full_formula.text()[i] == "*" or self.full_formula.text()[i] == "/":
                           time_alone = self.full_formula.text()[i] + time_alone
                           fin = 1
                        else:
                           time_alone = self.full_formula.text()[i] + time_alone
                           i -= 1
                    time_full = str(self.alone_sign.text())
                    time_full = time_full[1:]
                    time_full = time_full + time_alone
                    self.full_formula.setText(time_full)
                    self.alone_sign.setText("=" + str(eval(self.full_formula.text())))
                #Если значение полного выражения не содержит + или - или * или /, то повторно нажать = нельзя
                elif "=" in self.alone_sign.text():
                    pass
                #Условие добавления в строку всего выражения (self.full_formula) значения строки одиночного значения (self.alone_sign)
                elif len(self.alone_sign.text()) > 0:
                    if not self.alone_sign.text() == "0":
                        self.full_formula.setText(self.full_formula.text() + self.alone_sign.text())
                        self.alone_sign.setText("=" + str(eval(self.full_formula.text())))
                else:
                    if str(self.full_formula.text()[-1]).isdigit() or str(self.alone_sign.text()[-1]).isdigit():
                        self.full_formula.setText(self.full_formula.text() + self.alone_sign.text())
                        self.alone_sign.setText("=" + str(eval(self.full_formula.text())))
            else:
                    if self.alone_sign.text()[-1] == ".":
                        self.alone_sign.setText(self.alone_sign.text() + "0")
                    if "=" in self.alone_sign.text():
                        self.alone_sign.clear()
                    if self.full_formula.text() == "0":
                        self.full_formula.clear()
                    self.full_formula.setText(self.full_formula.text() + self.alone_sign.text() + self.text())
                    self.alone_sign.setText("0")

        return super().mousePressEvent(e)

class MainWindow(QMainWindow):  
    def __init__(self):
        """
        Конструктор для создания главного окна приложения.

        Parameters: 
        self: ссылка на текущий экземпляр класса. 

        Returns: 
        None.
        """
        super(MainWindow, self).__init__()
        # self.setFixedSize(QSize(650, 500))
        self.setWindowTitle("кальклюкатор")
        self.full_formula = QLabel()
        self.full_formula.setFixedWidth(300)
        self.full_formula.setAlignment(Qt.AlignRight)
        self.alone_sign = QLabel()
        self.alone_sign.setAlignment(Qt.AlignRight)
        self.alone_sign.setFixedWidth(300)
       
        
        #main widget
        main_widget = QWidget()
        main_widget.setLayout(QVBoxLayout())


        #labels
        labels_frame = QFrame()
        labels_frame.setLineWidth(3)
        labels_frame.setFrameStyle(QFrame.WinPanel | QFrame.Plain)
        labels_frame.setLayout(QVBoxLayout())
        labels_frame.layout().addWidget(self.full_formula, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame.layout().addWidget(self.alone_sign, alignment=Qt.AlignmentFlag.AlignRight)
        labels_frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        main_widget.layout().addWidget(labels_frame)

        labels_frame = QFrame()

        layout_butt = QGridLayout()

        layout_butt.addWidget(CustomQPushButton("1", self), 1, 0)
        layout_butt.addWidget(CustomQPushButton("4", self), 2, 0)
        layout_butt.addWidget(CustomQPushButton("7", self), 3, 0)
        layout_butt.addWidget(CustomQPushButton("+/-", self), 4, 0)
        layout_butt.addWidget(CustomQPushButton("C", self), 0, 1)
        layout_butt.addWidget(CustomQPushButton("2", self), 1, 1)
        layout_butt.addWidget(CustomQPushButton("5", self), 2, 1)
        layout_butt.addWidget(CustomQPushButton("8", self), 3, 1)
        layout_butt.addWidget(CustomQPushButton("0", self), 4, 1)
        layout_butt.addWidget(CustomQPushButton("CE", self), 0, 2)
        layout_butt.addWidget(CustomQPushButton("3", self), 1, 2)
        layout_butt.addWidget(CustomQPushButton("6", self), 2, 2)
        layout_butt.addWidget(CustomQPushButton("9", self), 3, 2)
        layout_butt.addWidget(CustomQPushButton(".", self), 4, 2)
        layout_butt.addWidget(CustomQPushButton("/", self), 0, 3)
        layout_butt.addWidget(CustomQPushButton("*", self), 1, 3)
        layout_butt.addWidget(CustomQPushButton("-", self), 2, 3)
        layout_butt.addWidget(CustomQPushButton("+", self), 3, 3)
        layout_butt.addWidget(CustomQPushButton("=", self), 4, 3)

        main_widget.layout().addLayout(layout_butt)
        self.setCentralWidget(main_widget)


if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()
    app.exec()
