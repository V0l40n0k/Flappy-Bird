from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QVBoxLayout,QPushButton

app = QApplication([])
window = QWidget()
window.setWindowTitle('My first app')
window.move(900,70)
window.resize(400,200)
window.show()

button = QPushButton(' Strange Button')
line = QVBoxLayout()

line.addWidget(button, alignment=Qt.AlignCenter)
window.setLayout(line)

def show_text():
    title = QLabel('u so cool')
    line.addWidget(title, alignment=Qt.AlignCenter)
    window.setLayout(line)
    app.exec_()

button.clicked.connect(show_text)

app.exec_()
