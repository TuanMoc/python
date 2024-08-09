from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_SanPhamDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(759, 431)
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
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setGeometry(QtCore.QRect(120, 80, 711, 351))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 641, 191))
        self.frame_2.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                   "background-color: rgb(182, 182, 182);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 141, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 131, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 141, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 211, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(110, 10, 151, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 40, 151, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 70, 151, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 100, 151, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 130, 151, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox = QtWidgets.QComboBox(parent=self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(110, 160, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(390, 100, 131, 17))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_9.setGeometry(QtCore.QRect(390, 130, 131, 17))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(390, 160, 131, 17))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_14 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(290, 30, 271, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_11 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(430, 30, 171, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(390, 70, 131, 17))
        self.pushButton_11.setObjectName("pushButton_11")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 190, 641, 161))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Connect to the database and populate comboBox
        self.populateComboBox()

        # Connect the "Thêm Sản Phẩm" button to the add_product method
        self.pushButton.clicked.connect(self.add_product)
        self.pushButton_9.clicked.connect(self.sua_san_pham)
        self.pushButton_10.clicked.connect(self.xoa_san_pham)
        self.pushButton_11.clicked.connect(self.tim_kiem_san_pham)
        self.tableWidget.clicked.connect(self.fill_product_data)

    def retranslateUi(self, Dialog):
        self.load_data()
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "QUẢN LÝ CỬA HÀNG THÚ CƯNG"))
        self.pushButton_5.setText(_translate("Dialog", "NHÀ CUNG CẤP"))
        self.pushButton_4.setText(_translate("Dialog", "SẢN PHẨM"))
        self.pushButton_7.setText(_translate("Dialog", "CHI TIẾT HÓA ĐƠN"))
        self.pushButton_8.setText(_translate("Dialog", "THỐNG KÊ"))
        self.pushButton_3.setText(_translate("Dialog", "NHÂN VIÊN"))
        self.pushButton_2.setText(_translate("Dialog", "BÁN HÀNG"))
        self.label_2.setText(_translate("Dialog", "Mã Sản Phẩm:"))
        self.label_3.setText(_translate("Dialog", "Tên Sản Phẩm:"))
        self.label_4.setText(_translate("Dialog", "Mô Tả:"))
        self.label_5.setText(_translate("Dialog", "Giá Tiền:"))
        self.label_6.setText(_translate("Dialog", "Số Lượng:"))
        self.label_7.setText(_translate("Dialog", "Mã Nhà Cung Cấp:"))
        self.pushButton.setText(_translate("Dialog", "Thêm Sản Phẩm"))
        self.pushButton_9.setText(_translate("Dialog", "Sửa Sản Phẩm"))
        self.pushButton_10.setText(_translate("Dialog", "Xóa Sản Phẩm"))
        self.label_14.setText(_translate("Dialog", "Nhập tên sản phẩm cần tìm:"))
        self.pushButton_11.setText(_translate("Dialog", "Tìm Kiếm Sản Phẩm"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "MaSP"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "TenSP"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Mô Tả"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Giá Tiền"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Số Lượng"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "MaNCC"))



    def load_data(self):
        try:
            # Attempt to connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789ab",
                database="QLCHTC"
            )
            print("Database connection successful")

            cursor = mydb.cursor()
            # Execute the query
            cursor.execute("SELECT MaSP, TenSP, MoTa, Gia, SoLuong, MaNCC FROM sanpham")
            rows = cursor.fetchall()
            print(f"Number of rows fetched: {len(rows)}")

            # Set row count to 0 before adding new rows
            self.tableWidget.setRowCount(0)

            # Insert data into the table
            for row in rows:
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                for column, value in enumerate(row):
                    self.tableWidget.setItem(rowPosition, column, QtWidgets.QTableWidgetItem(str(value)))
            print("Data loaded into the table")

            cursor.close()
            mydb.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")


        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def fill_product_data(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            ma_sp = self.tableWidget.item(selected_row, 0).text()
            ten_sp = self.tableWidget.item(selected_row, 1).text()
            mota = self.tableWidget.item(selected_row, 2).text()
            gia = self.tableWidget.item(selected_row, 3).text()
            soluong = self.tableWidget.item(selected_row, 4).text()
            ma_ncc = self.tableWidget.item(selected_row, 5).text()

            # Điền dữ liệu vào các QLineEdit và QComboBox tương ứng
            self.lineEdit.setText(ma_sp)
            self.lineEdit_2.setText(ten_sp)
            self.lineEdit_3.setText(mota)
            self.lineEdit_4.setText(gia)
            self.lineEdit_5.setText(soluong)
            index = self.comboBox.findText(ma_ncc, QtCore.Qt.MatchFlag.MatchFixedString)
            if index >= 0:
                self.comboBox.setCurrentIndex(index)

    def populateComboBox(self):
        # Connect to the database
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',  # replace with your MySQL username
                password='123456789ab',  # replace with your MySQL password
                database='QLCHTC'  # replace with your database name
            )
            cursor = connection.cursor()

            # Execute the query to get MaNCC from NhaCungCap
            cursor.execute("SELECT MaNCC FROM NhaCungCap")
            rows = cursor.fetchall()

            # Populate the comboBox with the fetched data
            for row in rows:
                self.comboBox.addItem(str(row[0]))  # Convert to string

            # Close the connection
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def add_product(self):
        # Get the data from the input fields
        maSP = self.lineEdit.text()
        tenSP = self.lineEdit_2.text()
        moTa = self.lineEdit_3.text()
        gia = self.lineEdit_4.text()
        soLuong = self.lineEdit_5.text()
        maNCC = self.comboBox.currentText()

        # Connect to the database
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',  # replace with your MySQL username
                password='123456789ab',  # replace with your MySQL password
                database='QLCHTC'  # replace with your database name
            )
            cursor = connection.cursor()

            # Insert the data into the SanPham table
            query = ("INSERT INTO SanPham (MaSP, TenSP, MoTa, Gia, SoLuong, MaNCC) "
                     "VALUES (%s, %s, %s, %s, %s, %s)")
            data = (maSP, tenSP, moTa, gia, soLuong, maNCC)
            cursor.execute(query, data)
            connection.commit()

            # Close the connection
            cursor.close()
            connection.close()

            # Clear the input fields
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.comboBox.setCurrentIndex(0)

            # Update the table view
            self.update_table_view()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def update_table_view(self):
        # Connect to the database
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',  # replace with your MySQL username
                password='123456789ab',  # replace with your MySQL password
                database='QLCHTC'  # replace with your database name
            )
            cursor = connection.cursor()

            # Fetch all products from the SanPham table
            cursor.execute("SELECT * FROM SanPham")
            rows = cursor.fetchall()

            # Update the tableWidget with the fetched data
            self.tableWidget.setRowCount(0)  # Clear existing data
            for row in rows:
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                for column, data in enumerate(row):
                    self.tableWidget.setItem(rowPosition, column, QtWidgets.QTableWidgetItem(str(data)))

            # Close the connection
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def sua_san_pham(self):
        # Lấy mã nhân viên từ QLineEdit
        maSP = self.lineEdit.text()

        # Lấy dữ liệu mới từ các QLineEdit

        tenSP = self.lineEdit_2.text()
        moTa = self.lineEdit_3.text()
        gia = self.lineEdit_4.text()
        soLuong = self.lineEdit_5.text()
        maNCC = self.comboBox.currentText()

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
            sql = "UPDATE SanPham SET TenSP = %s, MoTa = %s, Gia = %s, SoLuong = %s, MaNCC = %s WHERE MaSp = %s"
            val = (tenSP, moTa, gia, soLuong, maNCC, maSP)
            cursor.execute(sql, val)

            connection.commit()

            QtWidgets.QMessageBox.information(None, "Success", "Cập nhật thông tin sản phẩm thành công!")

        except mysql.connector.Error as error:
            QtWidgets.QMessageBox.warning(None, "Error", f"Lỗi: {error}")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                cursor.close()
                connection.close()
        self.load_data()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.comboBox.setCurrentIndex(0)

    def xoa_san_pham(self):
        # Lấy mã nhân viên từ QLineEdit
        ma_nv = self.lineEdit.text()

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
            sql = "DELETE FROM SanPham WHERE MaSP = %s"
            val = (ma_nv,)
            cursor.execute(sql, val)

            connection.commit()

            QtWidgets.QMessageBox.information(None, "Success", "Xóa sản phẩm thành công!")

        except mysql.connector.Error as error:
            QtWidgets.QMessageBox.warning(None, "Error", f"Lỗi: {error}")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                cursor.close()
                connection.close()
            self.load_data()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.comboBox.setCurrentIndex(0)

    def tim_kiem_san_pham(self):
        ten_sp = self.lineEdit_11.text()

        try:
            conn = mysql.connector.connect(
                host='localhost',
                database='QLCHTC',
                user='root',
                password='123456789ab'
            )
            cursor = conn.cursor()
            query = "SELECT MaSP, TenSP,  MoTa, Gia, SoLuong, MaNCC FROM SanPham WHERE TenSP LIKE %s"
            values = (f"%{ten_sp}%",)
            cursor.execute(query, values)
            rows = cursor.fetchall()

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(rows):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(None, "Error", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_SanPhamDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
