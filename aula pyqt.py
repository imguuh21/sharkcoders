import sys
from PyQt5.QtWidgets import QApplication,QLabel,QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('olá PyQt!')
window.setGeometry(100,100,300,100) #na ordem x,y,witdh,heigth

label = QLabel('<h1>bem vindo ao PyQt</h1>', parent=window)
label.move(50,20)#posição do elemento na ordem x y

window.show()
sys.exit(app.exec_())