import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,QLineEdit,QLabel)

app = QApplication

window = QWidget()
window.setWindowTitle('greeting')

name_input = QLineEdit()
name_input.setPlaceholderText("Enter your name...")

input_field = QLineEdit()
button = QPushButton('Greet')
label = QLabel("")

def greet():
    name = name_input.text()
    label.setText(f'Hi {name}')

button.clicked.connect(greet)

layout = QVBoxLayout()
layout.addWidget(name_input)
layout.addWidget(button)
layout.addWidget(label)
window.setlayout(layout)
window.show()

sys.exit(app.exec_())

