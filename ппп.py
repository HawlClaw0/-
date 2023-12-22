import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel
import sqlite3
from PyQt5.QtGui import QPixmap

SCREEN_SIZE = [1920, 1080]


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.info8 = None
        self.info7 = None
        self.second_form = None
        self.button17 = None
        self.button16 = None
        self.button15 = None
        self.button14 = None
        self.button13 = None
        self.button12 = None
        self.button11 = None
        self.button10 = None
        self.button9 = None
        self.button8 = None
        self.button7 = None
        self.button6 = None
        self.button5 = None
        self.button4 = None
        self.button3 = None
        self.button2 = None
        self.button1 = None
        self.info6 = None
        self.info5 = None
        self.info4 = None
        self.info3 = None
        self.info2 = None
        self.button18 = None
        self.info1 = None
        self.t = None
        self.image = None
        self.pixmap = None
        self.n33 = None
        self.trd_form = None
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle('Расположение мест')
        self.n33 = 0

        self.pixmap = QPixmap('sv-1-etazh.png')
        self.pixmap = self.pixmap.scaled(1700, 350)
        self.image = QLabel(self)
        self.image.move(120, 300)
        self.image.resize(2000, 400)
        self.image.setPixmap(self.pixmap)

        self.t = QLabel(self)
        self.t.setText('Информация по месту:')
        self.t.move(650, 25)
        self.t.resize(500, 40)
        self.t.setStyleSheet('font-size: 20pt')

        self.info1 = QLabel(self)
        self.info1.setText('')
        self.info1.move(650, 55)
        self.info1.resize(500, 40)
        self.info1.setStyleSheet('font-size: 20pt')

        self.info2 = QLabel(self)
        self.info2.setText('')
        self.info2.move(650, 85)
        self.info2.resize(500, 40)
        self.info2.setStyleSheet('font-size: 20pt')

        self.info3 = QLabel(self)
        self.info3.setText('')
        self.info3.move(650, 115)
        self.info3.resize(500, 40)
        self.info3.setStyleSheet('font-size: 20pt')

        self.info4 = QLabel(self)
        self.info4.setText('')
        self.info4.move(650, 145)
        self.info4.resize(500, 40)
        self.info4.setStyleSheet('font-size: 20pt')

        self.info5 = QLabel(self)
        self.info5.setText('')
        self.info5.move(650, 175)
        self.info5.resize(500, 40)
        self.info5.setStyleSheet('font-size: 20pt')

        self.info6 = QLabel(self)
        self.info6.setText('')
        self.info6.move(650, 205)
        self.info6.resize(500, 40)
        self.info6.setStyleSheet('font-size: 20pt')

        self.info7 = QLabel(self)
        self.info7.setText('')
        self.info7.move(650, 235)
        self.info7.resize(500, 40)
        self.info7.setStyleSheet('font-size: 20pt')

        self.info8 = QLabel(self)
        self.info8.setText('')
        self.info8.move(50, 130)
        self.info8.resize(500, 40)
        self.info8.setStyleSheet('font-size: 20pt')

        self.button1 = QPushButton('1', self)
        self.button1.move(519, 370)
        self.button1.resize(40, 178)

        self.button2 = QPushButton('2', self)
        self.button2.move(591, 370)
        self.button2.resize(40, 178)

        self.button3 = QPushButton('3', self)
        self.button3.move(632, 370)
        self.button3.resize(40, 178)

        self.button4 = QPushButton('4', self)
        self.button4.move(706, 370)
        self.button4.resize(40, 178)

        self.button5 = QPushButton('5', self)
        self.button5.move(746, 370)
        self.button5.resize(40, 178)

        self.button6 = QPushButton('6', self)
        self.button6.move(820, 370)
        self.button6.resize(40, 178)

        self.button7 = QPushButton('7', self)
        self.button7.move(861, 370)
        self.button7.resize(40, 178)

        self.button8 = QPushButton('8', self)
        self.button8.move(935, 370)
        self.button8.resize(40, 178)

        self.button9 = QPushButton('9', self)
        self.button9.move(976, 370)
        self.button9.resize(40, 178)

        self.button10 = QPushButton('10', self)
        self.button10.move(1048, 370)
        self.button10.resize(40, 178)

        self.button11 = QPushButton('11', self)
        self.button11.move(1090, 370)
        self.button11.resize(40, 178)

        self.button12 = QPushButton('12', self)
        self.button12.move(1162, 370)
        self.button12.resize(40, 178)

        self.button13 = QPushButton('13', self)
        self.button13.move(1204, 370)
        self.button13.resize(40, 178)

        self.button14 = QPushButton('14', self)
        self.button14.move(1277, 370)
        self.button14.resize(40, 178)

        self.button15 = QPushButton('15', self)
        self.button15.move(1317, 370)
        self.button15.resize(40, 178)

        self.button16 = QPushButton('16', self)
        self.button16.move(1390, 370)
        self.button16.resize(40, 178)

        self.button17 = QPushButton('купить место', self)
        self.button17.move(1500, 800)
        self.button17.resize(300, 60)
        self.button17.setStyleSheet('font-size: 20pt')

        self.button18 = QPushButton('отменить покупку', self)
        self.button18.move(1500, 900)
        self.button18.resize(300, 60)
        self.button18.setStyleSheet('font-size: 20pt')

        self.button1.clicked.connect(self.bt1)
        self.button2.clicked.connect(self.bt1)
        self.button3.clicked.connect(self.bt1)
        self.button4.clicked.connect(self.bt1)
        self.button5.clicked.connect(self.bt1)
        self.button6.clicked.connect(self.bt1)
        self.button7.clicked.connect(self.bt1)
        self.button8.clicked.connect(self.bt1)
        self.button9.clicked.connect(self.bt1)
        self.button10.clicked.connect(self.bt1)
        self.button11.clicked.connect(self.bt1)
        self.button12.clicked.connect(self.bt1)
        self.button13.clicked.connect(self.bt1)
        self.button14.clicked.connect(self.bt1)
        self.button15.clicked.connect(self.bt1)
        self.button16.clicked.connect(self.bt1)
        self.button17.clicked.connect(self.open_second_form)
        self.button18.clicked.connect(self.open_tr_form)

    def bt1(self):
        sender = self.sender()
        n_id = int(sender.text())
        self.n33 = n_id
        con = sqlite3.connect("trains.sqlite")
        cur = con.cursor()
        self.info1.setText(f'место:{n_id}')
        res = cur.execute(f"SELECT цена FROM места WHERE id = {n_id}").fetchone()
        for el in res:
            self.info2.setText(f'Цена:{str(el)}')
        res2 = cur.execute(f"SELECT наличие FROM места WHERE id = {n_id}").fetchone()
        for el in res2:
            self.info3.setText(f'Наличие:{str(el)}')
        res3 = cur.execute(f"SELECT id_поезда FROM места WHERE id = {n_id}").fetchone()
        for el in res3:
            self.info4.setText(f'Поезд:{str(el)}')
        res4 = cur.execute(f"SELECT время_выезда FROM места WHERE id = {n_id}").fetchone()
        for el in res4:
            self.info5.setText(f'Время отправки:{str(el)}')
        res5 = cur.execute(f"SELECT время_прибытия FROM места WHERE id = {n_id}").fetchone()
        for el in res5:
            self.info6.setText(f'Время прибытия:{str(el)}')
        res6 = cur.execute(f"SELECT в_пути FROM места WHERE id = {n_id}").fetchone()
        for el in res6:
            self.info7.setText(f'В пути:{str(el)}')
        res7 = cur.execute(f"SELECT откуда FROM места WHERE id = {n_id}").fetchone()
        res8 = cur.execute(f"SELECT куда FROM места WHERE id = {n_id}").fetchone()
        self.info8.setText(f'РЕЙС:{res7[0]} - {res8[0]}')
        con.close()

    def open_second_form(self):
        self.second_form = SecondForm(self, self.n33)
        self.second_form.show()

    def open_tr_form(self):
        self.trd_form = ThirdForm(self, self.n33)
        self.trd_form.show()


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.n = None
        self.inf = None
        self.button2 = None
        self.button1 = None
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Подтверждение')
        self.button1 = QPushButton('подтвердить', self)
        self.button1.move(50, 200)
        self.button1.resize(150, 40)
        self.button2 = QPushButton('отмена', self)
        self.button2.move(200, 200)
        self.button2.resize(150, 40)
        self.inf = QLabel(self)
        self.inf.setStyleSheet('font-size: 12pt')
        self.inf.setText(f'Вы хотите купить место номер {args[-1]}?')
        self.inf.move(70, 100)
        self.inf.resize(350, 40)

        self.button1.clicked.connect(self.bt1)
        self.button2.clicked.connect(self.bt2)
        self.n = int(args[-1])

    def bt1(self):
        con = sqlite3.connect("trains.sqlite")
        cur = con.cursor()
        cur.execute(f"UPDATE места SET наличие = 'продано' WHERE id = {self.n}")
        con.commit()
        con.close()
        SecondForm.close(self)

    def bt2(self):
        SecondForm.close(self)


class ThirdForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.n = None
        self.inf = None
        self.button2 = None
        self.button1 = None
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Отмена регистрации')
        self.button1 = QPushButton('подтвердить', self)
        self.button1.move(50, 200)
        self.button1.resize(150, 40)
        self.button2 = QPushButton('отмена', self)
        self.button2.move(200, 200)
        self.button2.resize(150, 40)
        self.inf = QLabel(self)
        self.inf.setStyleSheet('font-size: 12pt')
        self.inf.setText(f'Вы хотите отменить регистрацию на место номер {args[-1]}?')
        self.inf.move(7, 100)
        self.inf.resize(400, 40)

        self.button1.clicked.connect(self.bt1)
        self.button2.clicked.connect(self.bt2)
        self.n = int(args[-1])

    def bt1(self):
        con = sqlite3.connect("trains.sqlite")
        cur = con.cursor()
        cur.execute(f"UPDATE места SET наличие = 'есть' WHERE id = {self.n}")
        con.commit()
        con.close()
        ThirdForm.close(self)

    def bt2(self):
        ThirdForm.close(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())
