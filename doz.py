from PyQt5.Qt import *
import sys
from functools import partial


class Tic_toc_to(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('tic toc')
        self.setGeometry(200, 200, 400, 400)
        self.Vl = QVBoxLayout(self)
        self.Gl = QGridLayout()
        self.Vl.addLayout(self.Gl)
        self.HL1 = QHBoxLayout()
        self.HL2 = QHBoxLayout()
        self.Vl.addLayout(self.HL1)
        self.Vl.addLayout(self.HL2)


def restart():
    for i in range(3):
        for j in range(3):
            btns[i][j].clear()




p1 = 0
p2 = 0


def check_game():
    global p1
    global p2
    for i in range(3):
        if btns[i][0].text() == 'X' and btns[i][1].text() == 'X' and btns[i][2].text() == 'X' \
                or btns[0][i].text() == 'X' and btns[1][i].text() == 'X' and btns[2][i].text() == 'X' \
                or btns[0][0].text() == 'X' and btns[1][1].text() == 'X' and btns[2][2].text() == 'X' \
                or btns[0][2].text() == 'X' and btns[1][1].text() == 'X' and btns[2][0].text() == 'X':
            msg = QMessageBox()
            msg.setWindowTitle('<<<WIN>>>')
            msg.setGeometry(200, 200, 400, 400)
            msg.setStyleSheet('background')
            msg.show()
            msg.exec()
            p1 += 1
            play1.setText(str(p1))
        elif btns[i][0].text() == 'O' and btns[i][1].text() == 'O' and btns[i][2].text() == 'O' \
                or btns[0][i].text() == 'O' and btns[1][i].text() == 'O' and btns[2][i].text() == 'O' \
                or btns[0][0].text() == 'O' and btns[1][1].text() == 'O' and btns[2][2].text() == 'O' \
                or btns[0][2].text() == 'O' and btns[1][1].text() == 'O' and btns[2][0].text() == 'O':
            msg = QMessageBox()
            msg.setWindowTitle('<<<WIN>>>')
            msg.setGeometry(200, 200, 400, 400)
            msg.setStyleSheet('background')
            msg.show()
            msg.exec()
            p2 += 1
            play2.setText(str(p2))
        return
        restart()

player = ['X']
k = 1


def game(i, j):
    global k
    if btns[i][j].text() == '' and player[k - 1] == 'X':
        btns[i][j].setText('O')
        btns[i][j].setStyleSheet('background-colorDC143C;font-size:30px;')
        player.append('O')
        k += 1
    elif btns[i][j].text() == '' and player[k - 1] == 'O':
        btns[i][j].setText('X')
        btns[i][j].setStyleSheet('background-colorDC143C;font-size:30px;')
        player.append('X')
        k += 1
    check_game()



app = QApplication(sys.argv)
win = Tic_toc_to()
l1 = QLabel()
l1.setText('player1:')
win.HL1.addWidget(l1)
play1 = QLineEdit()
win.HL1.addWidget(play1)
l2 = QLabel()
l2.setText('player2:')
win.HL2.addWidget(l2)
play2 = QLineEdit()
win.HL2.addWidget(play2)
btns = [[QPushButton() for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        btns[i][j].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btns[i][j].setStyleSheet('background-color:#000080')
        win.Gl.addWidget(btns[i][j], i, j)
        btns[i][j].clicked.connect(partial(game, i, j))
win.show()
app.exec()
