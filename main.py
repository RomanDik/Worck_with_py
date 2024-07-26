from sympy import *
from math import sqrt
# для начала в терминале ввести .\.venv\Scripts\python.exe .\main.py
from random import choice, randint
# from layout_colorwidget import Color
from PySide6.QtCore import Qt,QEvent,QSize
from PySide6.QtGui import (
    QKeyEvent,
    QMouseEvent,
    QPalette, 
    QColor,
    QGuiApplication
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
    QFrame,
    QComboBox
)
Mem1 = 0
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class CustomQPushButton(QPushButton):
    def __init__(self, text, parent, if_eng:bool=False):
        super().__init__(text, parent=parent)
        self.setMouseTracking(True)
        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.full_formula = self.parent().full_formula
        self.alone_sign = self.parent().alone_sign
        self.full_formula.setText("")
        self.alone_sign.setText("")
        self.is_eng = if_eng  # указатель, что кнопка является частью инженерного режима
        
    
    def eng_toggle(self):
        """ Переключение видимости кнопок """
        if self.is_eng and self.isVisible():
            self.hide()
        elif self.is_eng and not self.isVisible():
            self.show()


    def keyPressEvent(self, e_1: QKeyEvent) -> None:
        """
        Обработчик события нажатия кнопки клавиатуры.
        Проверяет длину полей, и если они превышают допустимые значения, не выполняет никаких действий.

        Parameters: 
        self: ссылка на текущий экземпляр класса. 
        e_1: объект QKeyEvent, который содержит информацию о событии нажатия кнопки клавиатуры

        Returns: 
        None.
        """
        if not e_1.key() == Qt.Key_Delete and not e_1.key() == Qt.Key_Backspace:
            if len(str(self.full_formula.text())) > 65 or len(str(self.alone_sign.text())) > 65:
                return 0
        match e_1.key():
            case Qt.Key_1:
                self.full_formula.setText(self.full_formula.text() + "1")
            case Qt.Key_2:
                self.full_formula.setText(self.full_formula.text() + "2")
            case Qt.Key_3:
                self.full_formula.setText(self.full_formula.text() + "3")
            case Qt.Key_4:
                self.full_formula.setText(self.full_formula.text() + "4")
            case Qt.Key_5:
                self.full_formula.setText(self.full_formula.text() + "5")
            case Qt.Key_6:
                self.full_formula.setText(self.full_formula.text() + "6")
            case Qt.Key_7:
                self.full_formula.setText(self.full_formula.text() + "7")
            case Qt.Key_8:
                self.full_formula.setText(self.full_formula.text() + "8")
            case Qt.Key_9:
                self.full_formula.setText(self.full_formula.text() + "9")
            case Qt.Key_0:
                self.full_formula.setText(self.full_formula.text() + "0")
            case Qt.Key_Plus:
                self.full_formula.setText(self.full_formula.text() + "+")
            case Qt.Key_Minus:
                self.full_formula.setText(self.full_formula.text() + "-")
            case Qt.Key_Asterisk:
                self.full_formula.setText(self.full_formula.text() + "*")
            case Qt.Key_Slash:
                self.full_formula.setText(self.full_formula.text() + "/")
            case Qt.Key_Period:
                try:
                    if self.full_formula.text()[-1] == ".":
                        self.full_formula.setText(self.full_formula.text()[:(len(self.full_formula.text())-1)] + ",")
                    elif self.full_formula.text()[-1] == ",":
                        self.full_formula.setText(self.full_formula.text()[:(len(self.full_formula.text())-1)] + ".")
                    else:
                        self.full_formula.setText(self.full_formula.text() + ".")
                except:
                    pass
            case Qt.Key_Backspace:
                self.full_formula.setText(self.full_formula.text()[:(len(self.full_formula.text())-1)])
            case Qt.Key_Delete:
                self.full_formula.clear()
        try:
            x = float(sympify(self.full_formula.text()))
            if x % 1 == 0:
                self.alone_sign.setText(str(int(sympify(self.full_formula.text()))))
            else:
                self.alone_sign.setText(str(float(sympify(self.full_formula.text())))) 
        except:
                self.alone_sign.setText('err')
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        return super().keyPressEvent(e_1)
    def mousePressEvent(self, e: QMouseEvent) -> None:
        """
        Обработчик события нажатия кнопки мыши.
        Проверяет длину полей, и если они превышают допустимые значения, не выполняет никаких действий.

        Parameters: 
        self: ссылка на текущий экземпляр класса. 
        e: объект QMouseEvent, который содержит информацию о событии нажатия кнопки мыши

        Returns: 
        None.
        """
        global Mem1
        # Условие не выхода за пределы видимости поля ввода
        if not self.text() == 'C' and not self.text() == '<=':
            if len(str(self.full_formula.text())) > 65 or len(str(self.alone_sign.text())) > 65:
                return 0    
        # Кнопки удаления строки или символа
        if self.text() == "C" or self.text() == "<=":
            if self.text() == "C":
                self.full_formula.clear()
                self.alone_sign.clear()
            else:
                self.full_formula.setText(self.full_formula.text()[:(len(self.full_formula.text())-1)])
        
        # Пропуск кнопки смены режима
        elif self.text() == "Инжинерный" or self.text() == "Обычный":
            pass
        # Кнопки памяти
        elif self.text() == "MC": 
            Mem1 = 0
        elif self.text() == "MR": 
            self.full_formula.setText(self.full_formula.text() + str(Mem1))
        elif self.text() == "MS": 
            if not self.alone_sign.text() == "err":
                Mem1 = float(self.alone_sign.text())
        elif self.text() == "M+": 
                Mem1 +=  float(self.alone_sign.text())   
        elif self.text() == "M-": 
                Mem1 -=  float(self.alone_sign.text())
        # Точка если нажато в первый раз или последний символ , и наоборот. (запятая нужна для логарифма)
        elif self.text() == ". / ,":
            try:
                if self.full_formula.text()[-1] == ".":
                    self.full_formula.setText(self.full_formula.text()[:(len(self.full_formula.text())-1)] + ",")
                elif self.full_formula.text()[-1] == ",":
                    self.full_formula.setText(self.full_formula.text()[:(len(self.full_formula.text())-1)] + ".")
                else:
                    self.full_formula.setText(self.full_formula.text() + ".")
            except:
                pass
        # Рандомное число
        elif self.text() == "rand":
            self.full_formula.setText(self.full_formula.text() + str(randint(0,1000)))
        # добавляем скобку вместе с выводом логарифмов и корня для красоты и понимания.
        elif self.text() == "log" or self.text() == "ln" or self.text() == "sqrt":
            self.full_formula.setText(self.full_formula.text() + self.text() + "(")
        # Если нажато что-то из следующего: (изначально в формулу добавляются символы из-за счета в радианах)
        elif self.text() == "sin" or self.text() == "cos" or self.text() == "tan" or self.text() == "cot": 
            if self.text() == "sin":
                self.full_formula.setText(self.full_formula.text() + self.text() + "(pi/180*")
            if self.text() == "cos":
                self.full_formula.setText(self.full_formula.text() + self.text()+ "(pi/180*")
            if self.text() == "tan":
                self.full_formula.setText(self.full_formula.text() + self.text()+ "(pi/180*")
            if self.text() == "cot":
                self.full_formula.setText(self.full_formula.text() + self.text()+ "(pi/180*")
        # вывод напечатанного символа
        else:
            self.full_formula.setText(self.full_formula.text() + self.text())
        # попытки вычисления: удачно-вывод значения, неудачно-вывод err
        try:
            x = float(sympify(self.full_formula.text()))
            if x % 1 == 0:
                self.alone_sign.setText(str(int(sympify(self.full_formula.text()))))
            else:
                self.alone_sign.setText(str(float(sympify(self.full_formula.text())))) 
        except:
                self.alone_sign.setText('')

        return super().mousePressEvent(e)

class ClickableLabel(QLabel):
    
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)

    def mousePressEvent(self, event):
        """Позволяет скопировать содержимое виджета"""
        if event.button() == Qt.LeftButton:
            clipboard = QGuiApplication.clipboard()
            clipboard.setText(self.text())
            print("Скопированно:", self.text())
class MainWindow(QMainWindow):  
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(QSize(550, 300))
        self.setWindowTitle("кальклюкатор")
        
        self.full_formula = ClickableLabel()
        self.full_formula.setFixedWidth(450)
        self.full_formula.setAlignment(Qt.AlignRight)
        self.alone_sign = ClickableLabel()
        self.alone_sign.setAlignment(Qt.AlignRight)
        self.alone_sign.setFixedWidth(450)
       
        
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
        layout_butt.addWidget(CustomQPushButton("log", self, True), 0, 0)
        layout_butt.addWidget(CustomQPushButton("ln", self,True), 1, 0)
        layout_butt.addWidget(CustomQPushButton("sin", self,True), 2, 0)
        layout_butt.addWidget(CustomQPushButton("cos", self,True), 3, 0)
        layout_butt.addWidget(CustomQPushButton("tan", self,True), 4, 0)
        layout_butt.addWidget(CustomQPushButton("cot", self,True), 5, 0)
        layout_butt.addWidget(CustomQPushButton("sqrt", self), 0, 1)
        layout_butt.addWidget(CustomQPushButton("**", self), 1, 1)
        layout_butt.addWidget(CustomQPushButton("1", self), 2, 1)
        layout_butt.addWidget(CustomQPushButton("4", self), 3, 1)
        layout_butt.addWidget(CustomQPushButton("7", self), 4, 1)
        layout_butt.addWidget(CustomQPushButton("rand", self), 5, 1)
        layout_butt.addWidget(CustomQPushButton("%", self), 0, 2)
        layout_butt.addWidget(CustomQPushButton("C", self), 1, 2)
        layout_butt.addWidget(CustomQPushButton("2", self), 2, 2)
        layout_butt.addWidget(CustomQPushButton("5", self), 3, 2)
        layout_butt.addWidget(CustomQPushButton("8", self), 4, 2)
        layout_butt.addWidget(CustomQPushButton("0", self), 5, 2)
        layout_butt.addWidget(CustomQPushButton("(", self), 0, 3)
        layout_butt.addWidget(CustomQPushButton("<=", self), 1, 3)
        layout_butt.addWidget(CustomQPushButton("3", self), 2, 3)
        layout_butt.addWidget(CustomQPushButton("6", self), 3, 3)
        layout_butt.addWidget(CustomQPushButton("9", self), 4, 3)
        layout_butt.addWidget(CustomQPushButton(". / ,", self), 5, 3)
        layout_butt.addWidget(CustomQPushButton(")", self), 0, 4)
        layout_butt.addWidget(CustomQPushButton("/", self), 1, 4)
        layout_butt.addWidget(CustomQPushButton("*", self), 2, 4)
        layout_butt.addWidget(CustomQPushButton("-", self), 3, 4)
        layout_butt.addWidget(CustomQPushButton("+", self), 4, 4)
        layout_butt.addWidget(CustomQPushButton("pi", self), 5, 4)
        switcher = CustomQPushButton("Инжинерный", self)
        switcher.clicked.connect(lambda: [button.eng_toggle() for button in self.findChildren(CustomQPushButton)])
        switcher.clicked.connect(lambda: switcher.setText('Обычный') if switcher.text() == "Инжинерный" else\
                                 switcher.setText("Инжинерный"))
        layout_butt.addWidget(switcher, 0, 5)
        layout_butt.addWidget(CustomQPushButton("MC", self), 1, 5)
        layout_butt.addWidget(CustomQPushButton("MR", self), 2, 5)
        layout_butt.addWidget(CustomQPushButton("MS", self), 3, 5)
        layout_butt.addWidget(CustomQPushButton("M+", self), 4, 5)
        layout_butt.addWidget(CustomQPushButton("M-", self), 5, 5)

        main_widget.layout().addLayout(layout_butt)
        self.setCentralWidget(main_widget)
    
            

if __name__ == "__main__":
    app = QApplication([])
    
    window = MainWindow()
    window.show()
    app.exec()
