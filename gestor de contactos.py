import sys
import json
from PyQt5.QtWidgets import (QApplication,QMainWindow,
                             QWidget,QVBoxLayout,QHBoxLayout,QLineEdit,QPushButton,QTabWidget,
QTableWidgetItem)
contactos=[]
ficheiro_json =" ficheirojson"

def carregar_contacto():
    try:
        with open(ficheiro_json, "r", encoding="utf-8")as f:
            contactos.extend(json.load(f))
    except FileNotFoundError:
        pass
def guardar_contactos():
    with open(ficheiro_json,"w",encoding="utf-8")as f:
        json.dump(contactos,f,indent=4, ensure_ascii=False)

def atualizar_tabela():
    tabela.setRowCount(0)
    for i, c in enumerate(contactos):
        tabela.insertRow(i)
        tabela.setItem(i, 0,QTableWidgetItem(c["none"]))
        tabela.setItem(i, 1, QTableWidgetItem(c["telefone"]))
        tabela.setItem(i, 2,QTableWidgetItem(c["email"]))

def adicionar_contactos():
    nome = input_nome.text().strip()
    Telefone = input_telefone.text().strip()
    email = input_email.text().strip()

    if nome:
        contactos.append("nome",nome, "telefone", telefone,"Email:",email)


app = QApplication(sys.argv)
janela = QMainWindow()
janela.setWindowTitle("gestor de contactos")
janela.setGeometry(200, 200, 600, 400)

central =QWidget()
layout = QVBoxLayout()

tabela = QTabWidget()
tabela.setColumnCount(5)
tabela.setHorizontalHeaderLabels(["Nome","telefone","Email"])
tabela.cellClicked.connect(preencher_inputs)
layout.addWidget(tabela)

input_nome = QLineEdit()
input_telefone = QLineEdit()
input_email = QLineEdit
inputs_layout = QHBoxLayout()
inputs_layout.addWidget(input_nome)
inputs_layout.addWidget(input_telefone)
inputs_layout.addWidget(input_email)
layout.addLayout(inputs_layout)


btn_adicionar = QPushButton("Adcionar")
btn_editar = QPushButton("editar")
btn_remover = QPushButton("remover")

btn_adicionar.clicked.connect(adicionar_contacto)
btn_editar.clicked.connect(editar_contacto)
btn_remover.clicked.connect(remover_contacto)

botoes_layout = QHBoxLayout()
botoes_layout.addWidget(btn_adicionar)
botoes_layout.addWidget(btn_editar)
botoes_layout.addWidget(btn_remover)
layout.addLayout(botoes_layout)

central.setLayout(layout)
janela.setCentralWidget(central)

carregar_contactos()
atualizar_tabela()

janela.show()
sys.exit(app.exec())