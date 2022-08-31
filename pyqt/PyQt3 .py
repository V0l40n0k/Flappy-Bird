from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout,QPushButton,QHBoxLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle('My first app')
window.move(900,70)
window.resize(400,400)
window.show()

#Кнопки
button1 = QPushButton('PHP')
button2 = QPushButton('Python')
button3 = QPushButton('SQL')
button4 = QPushButton('JavaScript')
button5 = QPushButton('Pascal')
button6 = QPushButton('C++')
#Направляющие линии
v_line = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()

#Помещаем кнопки на линии

h_line1.addWidget(button1, alignment = Qt.AlignLeft)
h_line1.addWidget(button2, alignment = Qt.Alignleft)
h_line2.addWidget(button3, alignment = Qt.AlignLeft)
h_line3.addWidget(button4, alignment = Qt.AlignLeft)
h_line3.addWidget(button5, alignment = Qt.AlignRight)

v_line.addLayout(h_line1)
v_line.addLayout(h_line2)
v_line.addLayout(h_line3)

#Помещаем линии на окно
window.setLayout(v_line)


#Помещаем линии на окно
window.setLayout(h_line1)

app.exec_()
