import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from login import LoginDialog  # Assuming you have a LoginDialog class defined
from NhanVien import Ui_NhanVienDialog  # Import the Ui_NhanVienDialog class
from BanHang import Ui_Dialog  # Import the Ui_Dialog class from the generated BanHang.py file
from SanPham import Ui_SanPhamDialog  # Import the Ui_SanPhamDialog class
from NCC import Ui_NhaCungCapDialog  # Import the Ui_NhaCungCapDialog class
from ChiTietHoaDon import Ui_ChiTietHoaDonDialog  # Import the Ui_ChiTietHoaDonDialog class
from ThongKe import Ui_ThongKeDialog  # Import the Ui_ThongKeDialog class

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 399)





        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 121, 381))
        self.listWidget.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                      "background-color: rgb(170, 170, 127);")
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(110, 0, 511, 91))
        self.listWidget_2.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                        "background-color: rgb(170, 170, 127);")
        self.listWidget_2.setObjectName("listWidget_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(120, 90, 501, 271))
        self.graphicsView.setAutoFillBackground(False)
        self.graphicsView.setObjectName("graphicsView")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 90, 501, 271))
        self.widget.setStyleSheet("background-image: url('./python/thucung.jpg'")
        # self.widget.setStyleSheet(
        #     "background-image: url('./python/thucung.jpg'); background-repeat: no-repeat; background-size: cover;")

        self.widget.setObjectName("widget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 110, 121, 20))
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(530, 10, 81, 20))
        self.pushButton_6.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 140, 121, 20))
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 170, 121, 20))
        self.pushButton_4.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 200, 121, 20))
        self.pushButton_5.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 230, 121, 20))
        self.pushButton_7.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 260, 121, 20))
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_2.setEnabled(False)  # Disable buttons that require login initially
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 618, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the login button to open the login form
        self.pushButton_6.clicked.connect(self.openLoginForm)

        # Connect the "BÁN HÀNG" button to open the BanHang form
        self.pushButton_2.clicked.connect(self.openBanHangForm)

        # Connect the "NHÂN VIÊN" button to open the Employee Information dialog
        self.pushButton_3.clicked.connect(self.openEmployeeDialog)

        # Connect the new buttons to their respective methods
        self.pushButton_4.clicked.connect(self.openSanPhamForm)
        self.pushButton_5.clicked.connect(self.openNhaCungCapForm)
        self.pushButton_7.clicked.connect(self.openChiTietHoaDonForm)
        self.pushButton_8.clicked.connect(self.openThongKeForm)

        # Initialize login status
        self.logged_in = False
        self.username = ""

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "QUẢN LÝ CỬA HÀNG THÚ CƯNG"))
        self.pushButton_2.setText(_translate("MainWindow", "BÁN HÀNG"))
        self.pushButton_6.setText(_translate("MainWindow", "ĐĂNG NHẬP"))
        self.pushButton_3.setText(_translate("MainWindow", "NHÂN VIÊN"))
        self.pushButton_4.setText(_translate("MainWindow", "SẢN PHẨM"))
        self.pushButton_5.setText(_translate("MainWindow", "NHÀ CUNG CẤP"))
        self.pushButton_7.setText(_translate("MainWindow", "CHI TIẾT HÓA ĐƠN"))
        self.pushButton_8.setText(_translate("MainWindow", "THỐNG KÊ"))

    def openLoginForm(self):
        self.loginDialog = QtWidgets.QDialog()
        self.ui = LoginDialog(self)  # Pass the reference of MainWindow to LoginDialog
        self.ui.setupUi(self.loginDialog)
        self.loginDialog.exec()

    def update_login_status(self, username):
        self.logged_in = True
        self.username = username
        self.label.setText(f"Xin chào, {username}")  # Change the label to greet the user
        self.pushButton_6.setText("ĐĂNG XUẤT")  # Change the "Login" button text to "ĐĂNG XUẤT"
        self.pushButton_6.clicked.disconnect()  # Disconnect the login action
        self.pushButton_6.clicked.connect(self.logout)  # Connect to logout action

        # Enable buttons that require login
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)

    def logout(self):
        reply = QtWidgets.QMessageBox.question(None, 'Message', 'Bạn có muốn đăng xuất không?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.logged_in = False
            self.username = ""
            self.label.setText("QUẢN LÝ CỬA HÀNG THÚ CƯNG")  # Reset the label text
            self.pushButton_6.setText("ĐĂNG NHẬP")  # Change the "Logout" button text back to "ĐĂNG NHẬP"
            self.pushButton_6.clicked.disconnect()  # Disconnect the logout action
            self.pushButton_6.clicked.connect(self.openLoginForm)  # Connect back to the login form

            # Disable buttons that require login
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(False)
            self.pushButton_4.setEnabled(False)
            self.pushButton_5.setEnabled(False)
            self.pushButton_7.setEnabled(False)
            self.pushButton_8.setEnabled(False)
        else:
            pass

    def openBanHangForm(self):
        if self.logged_in:  # Check if the user is logged in
            self.banHangDialog = QtWidgets.QDialog()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self.banHangDialog)
            self.banHangDialog.exec()
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'Bạn cần đăng nhập trước khi bán hàng!')

    def openEmployeeDialog(self):
        if self.logged_in:  # Check if the user is logged in
            self.employeeDialog = QtWidgets.QDialog()
            self.ui = Ui_NhanVienDialog()
            self.ui.setupUi(self.employeeDialog)
            self.employeeDialog.exec()
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'Bạn cần đăng nhập trước khi xem thông tin nhân viên!')

    def openSanPhamForm(self):
        if self.logged_in:  # Check if the user is logged in
            self.sanPhamDialog = QtWidgets.QDialog()
            self.ui = Ui_SanPhamDialog()
            self.ui.setupUi(self.sanPhamDialog)
            self.sanPhamDialog.exec()
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'Bạn cần đăng nhập trước khi xem thông tin sản phẩm!')

    def openNhaCungCapForm(self):
        if self.logged_in:  # Check if the user is logged in
            self.nhaCungCapDialog = QtWidgets.QDialog()
            self.ui = Ui_NhaCungCapDialog()
            self.ui.setupUi(self.nhaCungCapDialog)
            self.nhaCungCapDialog.exec()
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'Bạn cần đăng nhập trước khi xem thông tin nhà cung cấp!')

    def openChiTietHoaDonForm(self):
        if self.logged_in:  # Check if the user is logged in
            self.chiTietHoaDonDialog = QtWidgets.QDialog()
            self.ui = Ui_ChiTietHoaDonDialog()
            self.ui.setupUi(self.chiTietHoaDonDialog)
            self.chiTietHoaDonDialog.exec()
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'Bạn cần đăng nhập trước khi xem chi tiết hóa đơn!')

    def openThongKeForm(self):
        if self.logged_in:  # Check if the user is logged in
            self.thongKeDialog = QtWidgets.QDialog()
            self.ui = Ui_ThongKeDialog()
            self.ui.setupUi(self.thongKeDialog)
            self.thongKeDialog.exec()
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'Bạn cần đăng nhập trước khi xem thống kê!')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_main = Ui_MainWindow()
    ui_main.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
