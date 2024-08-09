from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
from PyQt6.QtWidgets import QMessageBox, QDialog

class Ui_RegisterDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 200, 101, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 50, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 130, 141, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 100, 141, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 160, 141, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(self.register)  # Connect button to register method

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "MẬT KHẨU"))
        self.label_2.setText(_translate("Dialog", "TÊN ĐĂNG NHẬP"))
        self.pushButton_2.setText(_translate("Dialog", "ĐĂNG KÍ"))
        self.label.setText(_translate("Dialog", "ĐĂNG KÝ"))
        self.label_4.setText(_translate("Dialog", "XÁC THỰC MẬT KHẨU"))

    def register(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        confirm_password = self.lineEdit_3.text()

        # Check if any field is empty
        if not username or not password or not confirm_password:
            QMessageBox.warning(None, "Error", "Vui lòng điền đầy đủ thông tin!")
            return

        # Check if passwords match
        if password != confirm_password:
            QMessageBox.warning(None, "Error", "Mật khẩu xác thực không khớp!")
            return

        # Connect to MySQL database
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789ab",
                database="QLCHTC"
            )
            cursor = conn.cursor()

            # Create table if it doesn't exist
            cursor.execute('''CREATE TABLE IF NOT EXISTS NguoiDung
                              (TaiKhoan VARCHAR(255) PRIMARY KEY, MatKhau VARCHAR(255))''')

            # Insert user information into the database
            cursor.execute("INSERT INTO NguoiDung (TaiKhoan, MatKhau) VALUES (%s, %s)", (username, password))
            conn.commit()
            conn.close()

            # Registration successful
            QMessageBox.information(None, "Success", "Đăng ký thành công!")


            # Clear the registration form fields after successful registration
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")

        except mysql.connector.Error as e:
            # Handle MySQL errors
            QMessageBox.warning(None, "Error", "Tên đăng nhập đã tồn tại")

    def show_login_form(self):
        # Close current dialog and open a new login dialog
        self.dialog = QDialog()
        login_ui = Ui_LoginDialog()
        login_ui.setupUi(self.dialog)
        result = self.dialog.exec()
        if result == QDialog.Accepted:
            # Show main form or do whatever is needed after successful login
            self.show_main_form()  # Implement this method to show the main form

    def show_main_form(self):
        # Implement logic to show your main form here
        pass  # Placeholder; replace with actual logic


class Ui_LoginDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 50, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 100, 141, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 130, 141, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 200, 101, 21))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.login)  # Connect button to login method

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ĐĂNG NHẬP"))
        self.label_2.setText(_translate("Dialog", "TÊN ĐĂNG NHẬP"))
        self.label_3.setText(_translate("Dialog", "MẬT KHẨU"))
        self.pushButton.setText(_translate("Dialog", "ĐĂNG NHẬP"))

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        # Check if any field is empty
        if not username or not password:
            QMessageBox.warning(None, "Error", "Vui lòng điền đầy đủ thông tin!")
            return

        # Connect to MySQL database
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789ab",
                database="QLCHTC"
            )
            cursor = conn.cursor()

            # Check if user exists
            cursor.execute("SELECT * FROM NguoiDung WHERE TaiKhoan = %s AND MatKhau = %s", (username, password))
            user = cursor.fetchone()

            if user:
                QMessageBox.information(None, "Success", "Đăng nhập thành công!")
                Dialog.accept()  # Close login dialog upon successful login
            else:
                QMessageBox.warning(None, "Error", "Tên đăng nhập hoặc mật khẩu không đúng!")

            conn.close()

        except mysql.connector.Error as e:
            # Handle MySQL errors
            QMessageBox.warning(None, "Error", "Tên đăng nhập đã tồn tại")

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_RegisterDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
