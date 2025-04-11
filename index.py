from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUiType
import MySQLdb
import datetime
import sys
from xlsxwriter import Workbook

DB_CONFIG = {
    'host': 'localhost',
    'user': 'appuser',
    'password': 'app123',
    'db': 'library'
}

ui, _ = loadUiType('library.ui')
login_ui, _ = loadUiType('login.ui')


def get_db_connection():
    return MySQLdb.connect(**DB_CONFIG)


class Login(QWidget, login_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.handle_login)
        self.apply_theme('themes/darkorange.css')

    def apply_theme(self, path):
        try:
            with open(path, 'r') as f:
                self.setStyleSheet(f.read())
        except Exception:
            pass

    def handle_login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        try:
            db = get_db_connection()
            cur = db.cursor()
            cur.execute("SELECT * FROM users WHERE user_name=%s AND user_password=%s", (username, password))
            user = cur.fetchone()
            db.close()

            if user:
                self.main_app = MainApp()
                self.main_app.show()
                self.close()
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid username or password")
        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))


class MainApp(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.apply_theme('themes/darkorange.css')
        self.init_ui()
        self.load_initial_data()

    def apply_theme(self, path):
        try:
            with open(path, 'r') as f:
                self.setStyleSheet(f.read())
        except Exception:
            pass

    def init_ui(self):
        self.tabWidget.tabBar().setVisible(False)
        self.groupBox_3.hide()

        self.pushButton.clicked.connect(lambda: self.tabWidget.setCurrentIndex(0))
        self.pushButton_2.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))
        self.pushButton_26.clicked.connect(lambda: self.tabWidget.setCurrentIndex(2))
        self.pushButton_3.clicked.connect(lambda: self.tabWidget.setCurrentIndex(3))
        self.pushButton_4.clicked.connect(lambda: self.tabWidget.setCurrentIndex(4))

        self.pushButton_5.clicked.connect(lambda: self.groupBox_3.show())
        self.pushButton_17.clicked.connect(lambda: self.groupBox_3.hide())

        self.pushButton_19.clicked.connect(lambda: self.apply_theme('themes/darkorange.css'))
        self.pushButton_18.clicked.connect(lambda: self.apply_theme('themes/darkblue.css'))
        self.pushButton_21.clicked.connect(lambda: self.apply_theme('themes/darkgray.css'))
        self.pushButton_20.clicked.connect(lambda: self.apply_theme('themes/qdark.css'))

        self.pushButton_6.clicked.connect(self.add_day_operation)
        self.pushButton_29.clicked.connect(self.export_day_operations)

    def load_initial_data(self):
        self.load_day_operations()

    def add_day_operation(self):
        try:
            book_title = self.lineEdit.text()
            client_name = self.lineEdit_29.text()
            op_type = self.comboBox.currentText()
            days = self.comboBox_2.currentIndex() + 1
            today = datetime.date.today()
            return_date = today + datetime.timedelta(days=days)

            db = get_db_connection()
            cur = db.cursor()
            cur.execute("""
                INSERT INTO dayoperations (book_name, client, type, days, date, to_date)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (book_title, client_name, op_type, days, today, return_date))
            db.commit()
            db.close()
            self.statusBar().showMessage("New operation added")
            self.load_day_operations()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def load_day_operations(self):
        try:
            db = get_db_connection()
            cur = db.cursor()
            cur.execute("SELECT book_name, client, type, date, to_date FROM dayoperations")
            data = cur.fetchall()
            db.close()

            self.tableWidget.setRowCount(0)
            for row_idx, row_data in enumerate(data):
                self.tableWidget.insertRow(row_idx)
                for col_idx, item in enumerate(row_data):
                    self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def export_day_operations(self):
        try:
            db = get_db_connection()
            cur = db.cursor()
            cur.execute("SELECT book_name, client, type, date, to_date FROM dayoperations")
            data = cur.fetchall()
            db.close()

            wb = Workbook('day_operations.xlsx')
            sheet = wb.add_worksheet()
            headers = ['Book Title', 'Client Name', 'Type', 'From Date', 'To Date']
            for col, header in enumerate(headers):
                sheet.write(0, col, header)

            for row_idx, row_data in enumerate(data, start=1):
                for col_idx, item in enumerate(row_data):
                    sheet.write(row_idx, col_idx, str(item))
            wb.close()
            self.statusBar().showMessage("Report saved successfully")
        except Exception as e:
            QMessageBox.critical(self, "Export Error", str(e))


def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()