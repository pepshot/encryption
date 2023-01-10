import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import support_func


class Window1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI-файлы/home_screen.ui', self)
        self.pushButton.clicked.connect(self.tap)

    def tap(self):
        self.w1 = WindowLogins()
        self.w1.show()
        self.close()


class WindowLogins(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI-файлы/logining.ui', self)

        self.donwland_users()

        self.pushButton_2.clicked.connect(self.new_user)
        self.pushButton.clicked.connect(self.registration)

    def new_user(self):
        self.w1 = WindowNewUser()
        self.w1.show()
        self.close()

    def donwland_users(self):
        con = sqlite3.connect('encryption.db')

        cur = con.cursor()

        result = cur.execute("""SELECT login FROM users""").fetchall()

        logins = []
        for gen in result:
            logins.append(gen[0])

        self.comboBox.addItems(logins)

        con.close()

    def registration(self):
        login = self.comboBox.currentText()
        password = self.lineEdit.text()

        con = sqlite3.connect('encryption.db')

        cur = con.cursor()

        result = cur.execute(f"""SELECT id_user, password FROM users
                        where login = '{login}'""").fetchall()

        true_password = str(result[0][1])
        id_user = str(result[0][0])

        con.close()
        print(password, true_password, id_user)

        if password == true_password:
            self.w1 = WindowUser(id_user)
            self.w1.show()
            self.close()
        else:
            self.statusBar().showMessage('Неправильный пароль!')
            self.lineEdit.clear()


class ProhodnoyNewUser(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI-файлы/prohodnoy_new_user.ui', self)

        self.pushButton.clicked.connect(self.wind)

    def wind(self):
        self.w1 = WindowLogins()
        self.w1.show()
        self.close()


class WindowNewUser(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI-файлы/new_user.ui', self)

        self.pushButton.clicked.connect(self.creat_user)
        self.pushButton_2.clicked.connect(self.backend)

    def backend(self):
        self.w = WindowLogins()
        self.w.show()
        self.close()

    def creat_user(self):
        try:
            login = str(self.lineEdit.text())
            password = str(self.lineEdit_2.text())
            print(login, password)
            if login == '' or password == '':
                raise
            elif login.isdigit():
                raise TypeError

            con = sqlite3.connect('encryption.db')

            cur = con.cursor()

            result = cur.execute(f"""insert into users(login, password)
            values ('{login}', '{password}')""").fetchall()

            con.commit()
            con.close()

            self.wind()
        except TypeError:
            self.statusBar().showMessage('Ошибка. Логин не может содержать в себе только цифры')
        except Exception:
            self.statusBar().showMessage('Ошибка')

    def wind(self):
        self.w1 = ProhodnoyNewUser()
        self.w1.show()
        self.close()


class WindowUser(QMainWindow):
    def __init__(self, id_user):
        super().__init__()
        uic.loadUi('UI-файлы/user.ui', self)

        self.id_user = int(id_user)
        print(self.id_user)

        self.pushButton.clicked.connect(self.wind)
        self.pushButton_2.clicked.connect(self.text_encrypt)
        self.pushButton_3.clicked.connect(self.text_not_encrypt)
        self.pushButton_4.clicked.connect(self.my_text)

    def wind(self):
        self.w1 = WindowLogins()
        self.w1.show()
        self.close()

    def text_encrypt(self):
        self.w1 = WindowTextEncrypt(self.id_user)
        self.w1.show()
        self.close()

    def text_not_encrypt(self):
        self.w1 = WindowTextNotEncrypt(self.id_user)
        self.w1.show()
        self.close()

    def my_text(self):
        self.w1 = WindowMyText(self.id_user)
        self.w1.show()
        self.close()


class WindowTextEncrypt(QMainWindow):
    def __init__(self, id_user):
        super().__init__()
        uic.loadUi('UI-файлы/text_encrypt.ui', self)

        self.id_user = id_user
        print(self.id_user)

        self.donwland_ciphers()

        self.pushButton.clicked.connect(self.wind)
        self.pushButton_2.clicked.connect(self.text_encrept)
        self.pushButton_3.clicked.connect(self.window_infa)

    def window_infa(self):
        self.w3 = WindowInformationEncryption()
        self.w3.show()

    def wind(self):
        self.w1 = WindowUser(self.id_user)
        self.w1.show()
        self.close()

    def text_encrept(self):
        cipher = self.comboBox.currentText()
        key = self.spinBox.text()
        text = self.plainTextEdit.toPlainText()
        key = int(key)

        d = False
        for i in text:
            if i.isdigit() or i.isalpha():
                d = True
                break
        if d:

            if cipher == 'Цезарь':
                for i in text:
                    if i.isalpha() and (65 <= ord(i) <= 90 or 97 <= ord(i) <= 122):
                        new_message = support_func.enc_Cesar_en(key, text)
                        break
                    if i.isalpha() and (1040 <= ord(i) <= 1071 or 1072 <= ord(i) <= 1103 or ord(i) in [1105, 1025]):
                        new_message = support_func.enc_Cesar_ru(key, text)
                        break
            elif cipher == 'Азбука Морзе':
                new_message = support_func.enc_Az_Morse(key, text)
            elif cipher == 'Двоичный код':
                new_message = support_func.enc_Bin_code(key, text)
            elif cipher == 'Транспонирование':
                new_message = support_func.enc_Transponir(key, text)

            con = sqlite3.connect('encryption.db')

            cur = con.cursor()

            name = cur.execute(f"""select id_cipher from ciphers
            where cipher_title = '{cipher}'""").fetchall()
            n = int(name[0][0])

            con.close()

            con = sqlite3.connect('encryption.db')

            cur = con.cursor()

            result = cur.execute(f"""insert into encry_message(message, id_user, id_cipher, id_key, new_message)
            values ('{text}', {self.id_user}, {n}, {key}, '{new_message}')""").fetchall()
            con.commit()

            nnn = cur.execute("""select id_message from encry_message""").fetchall()

            con.close()

            id_message = str(nnn[-1][0])
            support_func.write_txt(self.id_user, id_message)

            self.statusBar().showMessage('Сообщение сохранено')
            self.plainTextEdit_2.setPlainText(new_message)
        else:
            self.statusBar().showMessage('Ваше сообщение пусто')
            self.plainTextEdit_2.clear()

    def donwland_ciphers(self):
        con = sqlite3.connect('encryption.db')

        cur = con.cursor()

        result = cur.execute("""SELECT cipher_title FROM ciphers""").fetchall()

        ciphers = []
        for gen in result:
            ciphers.append(gen[0])
        self.comboBox.addItems(ciphers)

        con.close()


class WindowTextNotEncrypt(QMainWindow):
    def __init__(self, id_user):
        super().__init__()
        uic.loadUi('UI-файлы/text_not_encrypt.ui', self)

        self.id_user = id_user
        print(self.id_user)

        self.donwland_ciphers()

        self.pushButton.clicked.connect(self.wind)
        self.pushButton_2.clicked.connect(self.text_encrept)
        self.pushButton_3.clicked.connect(self.window_infa)

    def window_infa(self):
        self.w3 = WindowInformationEncryption()
        self.w3.show()

    def wind(self):
        self.w1 = WindowUser(self.id_user)
        self.w1.show()
        self.close()

    def text_encrept(self):
        cipher = self.comboBox.currentText()
        key = self.spinBox.text()
        text = self.plainTextEdit.toPlainText()
        key = int(key)

        if cipher == 'Цезарь':
            for i in text:
                if i.isalpha() and (65 <= ord(i) <= 90 or 97 <= ord(i) <= 122):
                    new_message = support_func.not_enc_Cesar_en(key, text)
                    break
                if i.isalpha() and (1040 <= ord(i) <= 1071 or 1072 <= ord(i) <= 1103 or ord(i) in [1105, 1025]):
                    new_message = support_func.not_enc_Cesar_ru(key, text)
                    break
        elif cipher == 'Азбука Морзе':
            new_message = support_func.not_enc_Az_Morse(key, text)
        elif cipher == 'Двоичный код':
            new_message = support_func.not_enc_Bin_code(key, text)
        elif cipher == 'Транспонирование':
            new_message = support_func.not_enc_Transponir(key, text)

        con = sqlite3.connect('encryption.db')

        cur = con.cursor()

        result = cur.execute(f"""SELECT id_message FROM encry_message
        where new_message = '{text}'""").fetchall()

        word = result[0][0]
        support_func.not_encr_write_txt(self.id_user, word)

        self.plainTextEdit_2.setPlainText(new_message)

    def donwland_ciphers(self):
        con = sqlite3.connect('encryption.db')

        cur = con.cursor()

        result = cur.execute("""SELECT cipher_title FROM ciphers""").fetchall()

        ciphers = []
        for gen in result:
            ciphers.append(gen[0])

        self.comboBox.addItems(ciphers)

        con.close()


class WindowMyText(QMainWindow):
    def __init__(self, id_user):
        super().__init__()
        uic.loadUi('UI-файлы/my_text.ui', self)

        self.id_user = id_user
        print(self.id_user)

        self.texting()

        self.pushButton.clicked.connect(self.wind)

    def wind(self):
        self.w1 = WindowUser(self.id_user)
        self.w1.show()
        self.close()

    def texting(self):
        names_ciphers = {
            '1': 'Цезарь', '2': 'Транспонирование', '3': 'Азбука морзе', '4': 'Двоичный код', '5': '',
        }
        con = sqlite3.connect('encryption.db')

        cur = con.cursor()

        result = cur.execute(f"""SELECT id_message, message, id_cipher, id_key,
                                new_message FROM encry_message
                                where id_user = {self.id_user}""").fetchall()

        con.close()

        textes = []
        for i in result:
            textes.append((str(i[0]), i[1], names_ciphers[str(i[2])], str(i[3]), i[4]))
        print(textes)

        title = ['ID Сообщения', 'Сообщение до шифрования', 'Шифр', 'Ключ', 'Зашифрованное сообщение']
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(title)

        index = 0
        for row in textes:
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            hh = 0
            for elem in row:
                self.tableWidget.setItem(
                    index, hh, QTableWidgetItem(elem))
                hh += 1
            index += 1
        self.tableWidget.resizeColumnsToContents()


class WindowInformationEncryption(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI-файлы/information_encryption.ui', self)

        self.pushButton.clicked.connect(self.closse)

    def closse(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window1()
    ex.show()
    sys.exit(app.exec_())