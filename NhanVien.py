# Form implementation generated from reading ui file 'NhanVien.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_NhanVienDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(761, 477)
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setGeometry(QtCore.QRect(120, 80, 641, 31))
        self.frame.setStyleSheet("background-color: rgb(156, 156, 156);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 311, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 121, 481))
        self.widget.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.widget.setObjectName("widget")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 200, 121, 20))
        self.pushButton_5.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 170, 121, 20))
        self.pushButton_4.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 230, 121, 20))
        self.pushButton_7.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 260, 121, 20))
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 140, 121, 20))
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 110, 121, 20))
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_2 = QtWidgets.QFrame(parent=Dialog)
        self.frame_2.setGeometry(QtCore.QRect(120, 300, 641, 41))
        self.frame_2.setStyleSheet("background-color: rgb(156, 156, 156);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 161, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(110, 10, 151, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.btnTK = QtWidgets.QPushButton(parent=self.frame_2)
        self.btnTK.setGeometry(QtCore.QRect(300, 10, 131, 17))
        self.btnTK.setObjectName("btnTK")
        self.widget_2 = QtWidgets.QWidget(parent=Dialog)
        self.widget_2.setGeometry(QtCore.QRect(120, 0, 641, 81))
        self.widget_2.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(parent=self.widget_2)
        self.label.setGeometry(QtCore.QRect(190, 20, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_3 = QtWidgets.QFrame(parent=Dialog)
        self.frame_3.setGeometry(QtCore.QRect(120, 340, 641, 141))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 121, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(250, 10, 171, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(250, 40, 171, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(250, 70, 131, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 10, 151, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 40, 151, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 70, 151, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(90, 100, 151, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_13 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_13.setGeometry(QtCore.QRect(300, 10, 151, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_14.setGeometry(QtCore.QRect(300, 40, 151, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_15.setGeometry(QtCore.QRect(300, 70, 151, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.btnTNV = QtWidgets.QPushButton(parent=self.frame_3)
        self.btnTNV.setGeometry(QtCore.QRect(490, 30, 111, 21))
        self.btnTNV.setObjectName("btnTNV")
        self.btnSNV = QtWidgets.QPushButton(parent=self.frame_3)
        self.btnSNV.setGeometry(QtCore.QRect(490, 60, 111, 21))
        self.btnSNV.setObjectName("btnSNV")
        self.btnXNV = QtWidgets.QPushButton(parent=self.frame_3)
        self.btnXNV.setGeometry(QtCore.QRect(490, 90, 111, 21))
        self.btnXNV.setObjectName("btnXNV")
        self.tableWidget = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(120, 110, 641, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "DANH SÁCH THÔNG TIN NHÂN VIÊN"))
        self.pushButton_5.setText(_translate("Dialog", "NHÀ CUNG CẤP"))
        self.pushButton_4.setText(_translate("Dialog", "SẢN PHẨM"))
        self.pushButton_7.setText(_translate("Dialog", "CHI TIẾT HÓA ĐƠN"))
        self.pushButton_8.setText(_translate("Dialog", "THỐNG KÊ"))
        self.pushButton_3.setText(_translate("Dialog", "NHÂN VIÊN"))
        self.pushButton_2.setText(_translate("Dialog", "BÁN HÀNG"))
        self.label_3.setText(_translate("Dialog", "Tên nhân viên cần tìm:"))
        self.btnTK.setText(_translate("Dialog", "Tìm Kiếm"))
        self.label.setText(_translate("Dialog", "QUẢN LÝ CỬA HÀNG THÚ CƯNG"))
        self.label_4.setText(_translate("Dialog", "Mã Nhân Viên:"))
        self.label_5.setText(_translate("Dialog", "Tên Nhân Viên:"))
        self.label_6.setText(_translate("Dialog", "Địa Chỉ:"))
        self.label_7.setText(_translate("Dialog", "Lương:"))
        self.label_12.setText(_translate("Dialog", "EMAIL:"))
        self.label_13.setText(_translate("Dialog", "Ngày Sinh:"))
        self.label_14.setText(_translate("Dialog", "Giới Tính:"))
        self.btnTNV.setText(_translate("Dialog", "Thêm Nhân Viên"))
        self.btnSNV.setText(_translate("Dialog", "Sửa Nhân Viên"))
        self.btnXNV.setText(_translate("Dialog", "Xóa Nhân Viên"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "MaNV"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "TenNV"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Địa Chỉ"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Lương"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "EMAIL"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Ngày Sinh"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Giới Tính"))

        self.btnTNV.clicked.connect(self.them_nhan_vien)  # Kết nối nút với hàm xử lý
        self.btnSNV.clicked.connect(self.sua_nhan_vien)
        self.btnXNV.clicked.connect(self.xoa_nhan_vien)
        self.tableWidget.clicked.connect(self.fill_employee_data)
        self.btnTK.clicked.connect(self.search_employee)
        self.load_data_to_table()

    def fill_employee_data(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            ma_nv = self.tableWidget.item(selected_row, 0).text()
            ten_nv = self.tableWidget.item(selected_row, 1).text()
            dia_chi = self.tableWidget.item(selected_row, 2).text()
            luong = self.tableWidget.item(selected_row, 3).text()
            email = self.tableWidget.item(selected_row, 4).text()
            ngay_sinh = self.tableWidget.item(selected_row, 5).text()
            gioi_tinh = self.tableWidget.item(selected_row, 6).text()

            # Điền dữ liệu vào các QLineEdit tương ứng
            self.lineEdit_2.setText(ma_nv)
            self.lineEdit_3.setText(ten_nv)
            self.lineEdit_4.setText(dia_chi)
            self.lineEdit_8.setText(luong)
            self.lineEdit_13.setText(email)
            self.lineEdit_14.setText(ngay_sinh)
            self.lineEdit_15.setText(gioi_tinh)

    def load_data_to_table(self):
        host = 'localhost'
        database = 'QLCHTC'
        user = 'root'
        password = '123456789ab'

        try:
            # Connect to the database
            connection = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            if connection.is_connected():
                cursor = connection.cursor()

            # Lấy dữ liệu từ bảng nhanvien
                cursor.execute("SELECT * FROM NhanVien")
                records = cursor.fetchall()

                self.tableWidget.setRowCount(0)  # Xóa hết dữ liệu hiện tại trên tableWidget
                for row_number, row_data in enumerate(records):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(data))
                        self.tableWidget.setItem(row_number, column_number, item)

            connection.close()

        except mysql.connector.Error as error:
            QtWidgets.QMessageBox.warning(None, "Error", f"Lỗi: {error}")

    def them_nhan_vien(self):
        # Lấy dữ liệu từ các QLineEdit
        ma_nv = self.lineEdit_2.text()
        ten_nv = self.lineEdit_3.text()
        dia_chi = self.lineEdit_4.text()
        luong = self.lineEdit_8.text()
        email = self.lineEdit_13.text()
        ngay_sinh = self.lineEdit_14.text()
        gioi_tinh = self.lineEdit_15.text()

        # Kết nối đến CSDL MySQL
        host = 'localhost'
        database = 'QLCHTC'
        user = 'root'
        password = '123456789ab'

        try:
            # Connect to the database
            connection = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            if connection.is_connected():
                cursor = connection.cursor()

            # Thêm dữ liệu vào bảng nhanvien
                sql = "INSERT INTO nhanvien (MaNV, TenNV, DiaChi, Luong, Email, NgaySinh, GioiTinh) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                val = (ma_nv, ten_nv, dia_chi, luong, email, ngay_sinh, gioi_tinh)
                cursor.execute(sql, val)

                connection.commit()

                QtWidgets.QMessageBox.information(None, "Success", "Thêm nhân viên thành công!")

        except mysql.connector.Error as error:
            QtWidgets.QMessageBox.warning(None, "Error", f"Lỗi: {error}")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                cursor.close()
                connection.close()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_8.clear()
        self.lineEdit_13.clear()
        self.lineEdit_14.clear()
        self.lineEdit_15.clear()

        self.load_data_to_table()

    def xoa_nhan_vien(self):
        # Lấy mã nhân viên từ QLineEdit
        ma_nv = self.lineEdit_2.text()

        # Kết nối đến CSDL MySQL
        host = 'localhost'
        database = 'QLCHTC'
        user = 'root'
        password = '123456789ab'

        try:
            # Connect to the database
            connection = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            if connection.is_connected():
                cursor = connection.cursor()

            # Xóa dữ liệu từ bảng nhanvien
            sql = "DELETE FROM nhanvien WHERE MaNV = %s"
            val = (ma_nv,)
            cursor.execute(sql, val)

            connection.commit()

            QtWidgets.QMessageBox.information(None, "Success", "Xóa nhân viên thành công!")

        except mysql.connector.Error as error:
            QtWidgets.QMessageBox.warning(None, "Error", f"Lỗi: {error}")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                cursor.close()
                connection.close()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_8.clear()
        self.lineEdit_13.clear()
        self.lineEdit_14.clear()
        self.lineEdit_15.clear()
        self.load_data_to_table()

    def sua_nhan_vien(self):
        # Lấy mã nhân viên từ QLineEdit
        ma_nv = self.lineEdit_2.text()

        # Lấy dữ liệu mới từ các QLineEdit
        ten_nv = self.lineEdit_3.text()
        dia_chi = self.lineEdit_4.text()
        luong = self.lineEdit_8.text()
        email = self.lineEdit_13.text()
        ngay_sinh = self.lineEdit_14.text()
        gioi_tinh = self.lineEdit_15.text()

        # Kết nối đến CSDL MySQL
        host = 'localhost'
        database = 'QLCHTC'
        user = 'root'
        password = '123456789ab'

        try:
            # Connect to the database
            connection = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            if connection.is_connected():
                cursor = connection.cursor()

            # Cập nhật dữ liệu trong bảng nhanvien
            sql = "UPDATE nhanvien SET TenNV = %s, DiaChi = %s, Luong = %s, Email = %s, NgaySinh = %s, GioiTinh = %s WHERE MaNV = %s"
            val = (ten_nv, dia_chi, luong, email, ngay_sinh, gioi_tinh, ma_nv)
            cursor.execute(sql, val)

            connection.commit()

            QtWidgets.QMessageBox.information(None, "Success", "Cập nhật thông tin nhân viên thành công!")

        except mysql.connector.Error as error:
            QtWidgets.QMessageBox.warning(None, "Error", f"Lỗi: {error}")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                cursor.close()
                connection.close()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_8.clear()
        self.lineEdit_13.clear()
        self.lineEdit_14.clear()
        self.lineEdit_15.clear()
        self.load_data_to_table()

    def search_employee(self):
        ten_nv = self.lineEdit.text().strip()  # Lấy tên nhân viên cần tìm từ QLineEdit và loại bỏ khoảng trắng đầu cuối

        if ten_nv:
            host = 'localhost'
            database = 'QLCHTC'
            user = 'root'
            password = '123456789ab'

            try:
                # Connect to the database
                connection = mysql.connector.connect(
                    host=host,
                    database=database,
                    user=user,
                    password=password
                )
                if connection.is_connected():
                    cursor = connection.cursor()

                # Thực hiện truy vấn tìm kiếm
                sql = "SELECT * FROM nhanvien WHERE TenNV LIKE %s"
                val = ("%" + ten_nv + "%",)  # Tìm kiếm mọi từ chứa trong chuỗi tên_nhân_viên
                cursor.execute(sql, val)
                records = cursor.fetchall()

                self.tableWidget.setRowCount(0)  # Xóa hết dữ liệu hiện tại trên tableWidget
                for row_number, row_data in enumerate(records):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(data))
                        self.tableWidget.setItem(row_number, column_number, item)

                connection.close()

            except mysql.connector.Error as error:
                QtWidgets.QMessageBox.warning(None, "Error", f"Lỗi: {error}")

        else:
            QtWidgets.QMessageBox.warning(None, "Warning", "Vui lòng nhập tên nhân viên cần tìm!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_NhanVienDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
