from PyQt5.QtWidgets import*
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()


        self.lbl1 = QLabel("Введите первое число:")
        self.lbl1.setStyleSheet("QLabel{font-size:15px; color:red;}")
        self.edit1 = QLineEdit()
        self.lbl2 = QLabel("Введите второе число:")
        self.lbl2.setStyleSheet("QLabel{font-size:15px; color:red;}")
        self.edit2 = QLineEdit()
        self.btn_plus = QPushButton("+")
        self.btn_minus = QPushButton("-")
        self.btn_multiply = QPushButton("*")
        self.btn_divide = QPushButton("/")
        self.lbl_result = QLabel("Результат:")
        self.btn_divide.setStyleSheet("QPushButton{font-size:10px; color:red;}")


        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()

        hbox1.addWidget(self.lbl1)
        hbox1.addWidget(self.edit1)
        hbox2.addWidget(self.lbl2)
        hbox2.addWidget(self.edit2)
        hbox3.addWidget(self.btn_plus)
        hbox3.addWidget(self.btn_minus)
        hbox3.addWidget(self.btn_multiply)
        hbox3.addWidget(self.btn_divide)
        hbox4.addWidget(self.lbl_result)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

        self.setLayout(vbox)


        self.btn_plus.clicked.connect(self.plus)
        self.btn_minus.clicked.connect(self.minus)
        self.btn_multiply.clicked.connect(self.multiply)
        self.btn_divide.clicked.connect(self.divide)

    def plus(self):

        num1 = float(self.edit1.text())
        num2 = float(self.edit2.text())


        result = num1 + num2


        self.lbl_result.setText(f"Результат: {result}")

    def minus(self):
        num1 = float(self.edit1.text())
        num2 = float(self.edit2.text())

        result = num1 - num2

        self.lbl_result.setText(f"Результат: {result}")

    def multiply(self):
        num1 = float(self.edit1.text())
        num2 = float(self.edit2.text())

        result = num1 * num2

        self.lbl_result.setText(f"Результат: {result}")

    def divide(self):
        num1 = float(self.edit1.text())
        num2 = float(self.edit2.text())

        result = num1 / num2

        self.lbl_result.setText(f"Результат: {result}")



app = QApplication(sys.argv)
calc = Calculator()
calc.show()
sys.exit(app.exec_())
