import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,QTextEdit, QAction,QFileDialog,QMessageBox,QHBoxLayout,
QVBoxLayout,QPushButton,QLineEdit,QLabel)
from PyQt5.QtGui import QKeySequence

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("calculadora simples")
window.setGeometry(300, 300, 600, 400)


input_field = QLineEdit()
input_field.setPlaceholderText("Numero 1")

input_field2 = QLineEdit
input_field2.setPlaceholderText()


button = QPushButton("+")
button1 = QPushButton("-")
button2 = QPushButton("*")
button3 = QPushButton("%")
label = QLabel
layout = QVBoxLayout()
layout.addWidget(input_field)
layout.addWidget(QPushButton(button))
layout.addWidget(QPushButton(button2))
layout.addWidget(QPushButton(button3))


def somar():
    try:
        a = float(input_field.text())
        b = float(input_field2.text())

        resultado = a + b
        resultado_label.setText

window.show()
sys.exit(app.exec_())