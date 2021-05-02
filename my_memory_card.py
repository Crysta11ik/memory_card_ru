#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox
from random import shuffle
prav = 0
neprav = 0
vse = 0
ratio = 0
glavlayout = QVBoxLayout()
app = QApplication([])
main_win = QWidget()
main_win.show()
main_win.setLayout(glavlayout)

RGroupBox2 = QGroupBox('Результат теста')
RGroupBox2.hide()
da = QLabel('Правильно/Неправильно')
otv = QLabel('Правильный ответ')

a = QLabel('какой национальности не существует?')
rbtn1 = QRadioButton('энцы')
rbtn2 = QRadioButton('смурфы')
rbtn3 = QRadioButton('чулымцы')
rbtn4 = QRadioButton('алеуты')

class Question():
    def __init__(self, question, rightanswer, wrong1, wrong2, wrong3):
        self.question = question
        self.rightanswer = rightanswer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

answers=[rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q: Question):
    shuffle(answers)
    a.setText(q.question)
    answers[0].setText(q.rightanswer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

q1 = Question("привет", 'привет', 'пока', 'пока', 'пока')
q2 = Question('какого цвета дверь', 'белый', 'егор', 'черный', 'зеленый')
f1 = Question('3+3', '6', '15', '4', '7')
f2 = Question('оцени тест', 'отлично', 'ужасно', 'плохо', 'отвратительно')
q = Question('сколько хромосом у человека', "46", "20", "28", "0")
f = Question('сколько', 'евразия', 'китай', 'россия', "тихий океан")
q3 = Question('как называется это приложение', 'memory card', 'я', 'бравл старс', 'python')

vopr_list = [q, f, q1, f1, q2, q3, f2]
i = 0

def show_q():
    RGroupBox.show()
    b.setText('Ответить')
    RGroupBox2.hide()
    layoutans4.addWidget(da)
    layoutans4.addWidget(otv)
    RGroupBox2.setLayout(layoutans4)

def show_r():
    a.setText('Результаты')
    RGroupBox2.show()
    b.setText('Следующий вопрос')
    RGroupBox.hide()
    layoutans4.addWidget(da)
    layoutans4.addWidget(otv)
    RGroupBox2.setLayout(layoutans4)

def show_cor(res):
    da.setText(res)
    otv.setText(answers[0].text())
    show_r()

def check_ans():
    global vse
    vse += 1
    if answers[0].isChecked():
        show_cor('Верно')
        global prav
        prav += 1
    else:
        show_cor('неверно')
        global neprav
        neprav += 1
    ratio = prav / vse
    print('Количество правильных:', prav)
    print('Количество неправильных:', neprav)
    print('Всего вопросов:', vse)
    print('Соотношение всех вопросов с правильными ответами:', ratio)

def next_q():
    global i
    ask(vopr_list[i])
    i += 1
    show_q()
    
def clickok():
    if b.text() == 'Ответить':
        check_ans()
    else:
        next_q()

b = QPushButton('Ответить')
RGroupBox = QGroupBox("Варианты ответов")

layoutans1 = QHBoxLayout()
layoutans2 = QVBoxLayout()
layoutans3 = QVBoxLayout()
layoutans4 = QVBoxLayout()
layoutans2.addWidget(rbtn1)
layoutans2.addWidget(rbtn2)
layoutans3.addWidget(rbtn3)
layoutans3.addWidget(rbtn4)
layoutans1.addLayout(layoutans2)
layoutans1.addLayout(layoutans3)

RGroupBox.setLayout(layoutans1)
glavlayout.addWidget(a, alignment = Qt.AlignCenter)
glavlayout.addWidget(RGroupBox, alignment = Qt.AlignCenter)
glavlayout.addWidget(RGroupBox2)
glavlayout.addWidget(b, alignment = Qt.AlignCenter)

b.clicked.connect(clickok)

app.exec_()