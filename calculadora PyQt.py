import sys
from PyQt5.QtWidgets import (QApplication, QWidget,QTextEdit, QAction,QFileDialog,QMessageBox,QHBoxLayout,
QVBoxLayout,QPushButton,QLineEdit,QLabel)
from PyQt5.QtGui import QKeySequence

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("calculadora simples")
window.setGeometry(300, 300, 600, 400)


input1 = QLineEdit()
input1.setPlaceholderText("Numero 1")

input2 = QLineEdit()
input2.setPlaceholderText("numero 2")




def somar():
    try:
        a = float(input1.text())
        b = float(input2.text())

        resultado = a + b
        resultado_label.setText(f"Resultado: {resultado}")

    except ValueError:
        resultado_label.setText("erro introduz numero valido")

def subtrair():
    try:
        a = float(input1.text())
        b = float(input2.text())

        resultado = a - b
        resultado_label.setText(f"Resultado: {resultado}")

    except ValueError:
        resultado_label.setText("erro introduz numero valido")

def multiplicar():
    try:
        a = float(input1.text())
        b = float(input2.text())

        resultado = a * b
        resultado_label.setText(f"Resultado: {resultado}")

    except ValueError:
        resultado_label.setText("erro introduz numero valido")


def dividir():
    try:
        a = float(input1.text())
        b = float(input2.text())

        resultado = a / b
        resultado_label.setText(f"Resultado: {resultado}")
    except ValueError:
        resultado_label.setText("erro introduz numero valido")




button_soma = QPushButton("+")
button_sub = QPushButton("-")
button_multiplicar = QPushButton("*")
button_dividir = QPushButton("/")
resultado_label = QLabel("Resultado:")

button_soma.clicked.connect(somar)
button_sub.clicked.connect(subtrair)
button_multiplicar.clicked.connect(multiplicar)
button_dividir.clicked.connect(dividir)

layout = QVBoxLayout()
layout.addWidget(input1)
layout.addWidget(input2)
layout.addWidget(button_soma)
layout.addWidget(button_sub)
layout.addWidget(button_multiplicar)
layout.addWidget(button_dividir)
layout.addWidget(resultado_label)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())