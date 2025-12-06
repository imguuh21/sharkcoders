import sys
import datetime
from PyQt5.QtWidgets import (QApplication,QMainWindow,QWidget,QVBoxLayout,QLabel,QPushButton,QTimeEdit,QMessageBox)
from PyQt5.QtCore import QTimer,QTime
#MAIN
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Relógio Digital")
window.setGeometry(300, 300, 600, 400)
#LAYOUT
central = QWidget()
layout = QVBoxLayout()

label_hora = QLabel()
label_hora.setStyleSheet("font-size: 32px; text-align: center")
layout.addWidget(label_hora)

label_alarme = QLabel("Alarme (nenhum alarme definido)")
layout.addWidget(label_alarme)

input_alarme = QTimeEdit()
input_alarme.setDisplayFormat("HH:mm")
layout.addWidget(input_alarme)


def atualizar_hora():
    agora = QTime.currentTime()
    texto_hora = agora.toString("HH:mm:ss")
    label_hora.setText(texto_hora)

    if 'alarme_hora' in globals():
        if alarme_hora and agora.toString("HH:mm") == alarme_hora.toString("HH:mm"):
            disparar_hora()


def disparar_hora():
    global alarme_hora
    QTimer.singleShot(1000, limpar_alarme)
    QMessageBox.information(window, "Alarme", "Alarme! Hora atingida")


def limpar_alarme():
    global alarme_hora
    alarme_hora = None
    alarme_hora.setText("Alarme: (Nenhum alarme definindo)")


def definir_alarme():
    global alarme_hora
    alarme_hora = input_alarme.time()
    label_alarme.setText("Alarme:" + alarme_hora.toString("HH:mm"))

btn_definir = QPushButton("definir alarme")
btn_definir.clicked.connect(definir_alarme)
layout.addWidget(btn_definir)

central.setLayout(layout)
window.setCentralWidget(central)


timer = QTimer()
timer.timeout.connect(atualizar_hora)
timer.start(1000)

atualizar_hora
window.show()
sys.exit(app.exec_())

