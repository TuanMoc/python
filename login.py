from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
from dangki import Ui_RegisterDialog  # Import the registration dialog

class LoginDialog(object):
    def __init__(self, main_window):
        self.main_window = main_window

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(472, 390)
        self.Dialog = Dialog
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 140, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 170, 101, 21))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(170, 60, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 140, 141, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 200, 101, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 110, 141, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.open_register_form)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "MẬT KHẨU"))
        self.label_2.setText(_translate("Dialog", "TÊN ĐĂNG NHẬP"))
        self.pushButton.setText(_translate("Dialog", "ĐĂNG NHẬP"))
        self.label.setText(_translate("Dialog", "ĐĂNG NHẬP"))
        self.pushButton_2.setText(_translate("Dialog", "ĐĂNG KÍ"))

    def open_register_form(self):
        self.register_dialog = QtWidgets.QDialog()
        self.ui = Ui_RegisterDialog()
        self.ui.setupUi(self.register_dialog)
        self.register_dialog.exec()

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        # Connect to MySQL database
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789ab",
                database="QLCHTC"
            )
            cursor = conn.cursor()

            # Execute query to check if username and password exist in database
            cursor.execute("SELECT * FROM NguoiDung WHERE TaiKhoan = %s AND MatKhau = %s", (username, password))
            record = cursor.fetchone()

            if record:
                # Login successful
                QtWidgets.QMessageBox.information(None, "Thông báo", "Đăng nhập thành công!")
                self.main_window.update_login_status(username)  # Gửi tên đăng nhập về MainWindow
                self.Dialog.accept()  # Đóng dialog đăng nhập

            else:
                # Login failed
                QtWidgets.QMessageBox.warning(None, "Cảnh báo", "Đăng nhập thất bại. Vui lòng kiểm tra lại tên đăng nhập và mật khẩu!")

            cursor.close()
            conn.close()

        except mysql.connector.Error as e:
            # Handle MySQL errors
            QtWidgets.QMessageBox.warning(None, "Lỗi MySQL", f"Lỗi kết nối MySQL: {e}")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = LoginDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())