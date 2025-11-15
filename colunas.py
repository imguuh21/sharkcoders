import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,QLineEdit,QLabel,QHBoxLayout)

left_layout = QHBoxLayout()







main_layout = QHBoxLayout()
main_layout.addlayout(left_layout)
main_layout.addlayout(right_layout)

window.setlayout(main_layout)
window.show()

sys.exit(app.exec_())