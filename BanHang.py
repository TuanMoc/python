
import mysql.connector
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import QtCore, QtGui, QtWidgets
from InHoaDon import Ui_InHoaDon




class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(731, 481)
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setGeometry(QtCore.QRect(120, 80, 321, 151))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(parent=self.frame)
        self.label_10.setGeometry(QtCore.QRect(10, 100, 51, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 40, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 100, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")


        self.lineEdit_30 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_30.setGeometry(QtCore.QRect(70, 180, 113, 20))
        self.lineEdit_30.setObjectName("lineEdit_30")

        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 70, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(200, 10, 111, 17))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 40, 111, 20))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(200, 70, 111, 17))
        self.pushButton_9.setObjectName("pushButton_9")
        self.frame_4 = QtWidgets.QFrame(parent=Dialog)
        self.frame_4.setGeometry(QtCore.QRect(440, 80, 291, 401))
        self.frame_4.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_13 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_13.setGeometry(QtCore.QRect(90, 0, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.frame_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(110, 30, 151, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_13.setGeometry(QtCore.QRect(170, 60, 91, 17))
        self.pushButton_13.setObjectName("pushButton_13")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.frame_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 80, 291, 321))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.frame_3 = QtWidgets.QFrame(parent=Dialog)
        self.frame_3.setGeometry(QtCore.QRect(120, 400, 321, 81))
        self.frame_3.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(parent=self.frame_3)
        self.comboBox.setGeometry(QtCore.QRect(90, 10, 91, 20))
        self.comboBox.setObjectName("comboBox")
        self.label_11 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_5 = QtWidgets.QDateEdit(parent=self.frame_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(72, 40, 125, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_12 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(200, 10, 101, 16))
        self.label_12.setObjectName("label_12")

        self.label_120 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_120.setGeometry(QtCore.QRect(260, 10, 101, 16))
        self.label_120.setObjectName("label_120")

        self.pushButton_11 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_11.setGeometry(QtCore.QRect(200, 30, 101, 17))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_12.setGeometry(QtCore.QRect(200, 60, 101, 17))
        self.pushButton_12.setObjectName("pushButton_12")
        self.widget_2 = QtWidgets.QWidget(parent=Dialog)
        self.widget_2.setGeometry(QtCore.QRect(120, 0, 611, 81))
        self.widget_2.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(parent=self.widget_2)
        self.label.setGeometry(QtCore.QRect(130, 20, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(parent=Dialog)
        self.frame_2.setGeometry(QtCore.QRect(120, 230, 321, 171))
        self.frame_2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"background-color: rgb(0, 255, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 321, 131))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(120, 10, 81, 20))
        self.pushButton_10.setObjectName("pushButton_10")
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_13.clicked.connect(self.tim_kiem_san_pham)
        self.pushButton_9.clicked.connect(self.add_product)
        self.pushButton.clicked.connect(self.create_invoice)
        self.tableWidget_2.clicked.connect(self.fill_product_data)
        self.pushButton_11.clicked.connect(self.calculate_total)

        self.pushButton_12.clicked.connect(self.save_invoice)
        self.pushButton_10.clicked.connect(self.delete_selected_product)
        self.pushButton_6.clicked.connect(self.InHoaDon)
        self.load_maNV()
        self.lamMoiNgay()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Mã Hóa Đơn"))
        self.label_4.setText(_translate("Dialog", "Tên Sản Phẩm"))
        self.label_5.setText(_translate("Dialog", "Số Lượng"))
        self.label_10.setText(_translate("Dialog", "Đơn Giá"))
        self.pushButton.setText(_translate("Dialog", "Tạo Hóa Đơn"))
        self.pushButton_6.setText(_translate("Dialog", "In Hóa Đơn"))
        self.pushButton_9.setText(_translate("Dialog", "Thêm Hóa Đơn"))
        self.label_13.setText(_translate("Dialog", "Danh Sách Thú Cưng"))
        self.label_14.setText(_translate("Dialog", "Nhập tên thú cưng cần tìm:"))
        self.pushButton_13.setText(_translate("Dialog", "Tìm Kiếm"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "MaSP"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "TenSP"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Mô Tả"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Giá"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Số Lượng"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "NCC"))
        self.label_3.setText(_translate("Dialog", "Mã Nhân Viên"))
        self.label_11.setText(_translate("Dialog", "Ngày Lập"))
        self.label_120.setText(_translate("Dialog", "0VND"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p>Tổng Tiền:                                </p></body></html>"))
        self.pushButton_11.setText(_translate("Dialog", "Tính Tiền Hóa Đơn"))
        self.pushButton_12.setText(_translate("Dialog", "Thanh Toán"))
        self.label.setText(_translate("Dialog", "QUẢN LÝ CỬA HÀNG THÚ CƯNG"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Mã Sản Phẩm"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Tên Sản Phẩm"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Số Lượng"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Giá Bán"))
        self.pushButton_10.setText(_translate("Dialog", "Xóa cart"))
        self.pushButton_5.setText(_translate("Dialog", "NHÀ CUNG CẤP"))
        self.pushButton_4.setText(_translate("Dialog", "SẢN PHẨM"))
        self.pushButton_7.setText(_translate("Dialog", "CHI TIẾT HÓA ĐƠN"))
        self.pushButton_8.setText(_translate("Dialog", "THỐNG KÊ"))
        self.pushButton_3.setText(_translate("Dialog", "NHÂN VIÊN"))
        self.pushButton_2.setText(_translate("Dialog", "BÁN HÀNG"))
        self.load_data()

    def InHoaDon(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InHoaDon()
        self.ui.setupUi(self.window)
        self.window.show()
    def fill_product_data(self):
        selected_row = self.tableWidget_2.currentRow()
        if selected_row >= 0:
            ma_sp = self.tableWidget_2.item(selected_row, 0).text()
            ten_sp = self.tableWidget_2.item(selected_row, 1).text()

            gia = self.tableWidget_2.item(selected_row, 3).text()


            # Điền dữ liệu vào các QLineEdit và QComboBox tương ứng

            self.lineEdit_2.setText(ten_sp)

            self.lineEdit_3.setText(gia)
            self.lineEdit_30.setText(ma_sp)

    def calculate_total(self):
        total_amount = 0.0

        # Iterate through each row in the table widget
        for row in range(self.tableWidget.rowCount()):
            soLuong_item = self.tableWidget.item(row, 2)  # "SoLuong" column
            gia_item = self.tableWidget.item(row, 3)  # "Gia" column

            if soLuong_item and gia_item:
                try:
                    soLuong = int(soLuong_item.text())
                    gia = float(gia_item.text())
                    total_amount += soLuong * gia
                except ValueError:
                    pass  # Handle the case where the cell text is not a valid number

        # Display the total amount (e.g., in a QLabel)
        self.label_120.setText(f"{total_amount:.2f}")
    def load_maNV(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='123456789ab',
                database='QLCHTC'
            )
            cursor = connection.cursor()

            # Truy vấn để lấy danh sách Mã Nhân Viên từ bảng NhanVien
            cursor.execute("SELECT MaNV FROM NhanVien")
            result = cursor.fetchall()

            # Đổ dữ liệu vào QComboBox (ccb)
            for row in result:
                self.comboBox.addItem(str(row[0]))

            # Đóng kết nối
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
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
            self.tableWidget_2.setRowCount(0)

            # Insert data into the table
            for row in rows:
                rowPosition = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(rowPosition)
                for column, value in enumerate(row):
                    self.tableWidget_2.setItem(rowPosition, column, QtWidgets.QTableWidgetItem(str(value)))
            print("Data loaded into the table")

            cursor.close()
            mydb.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def delete_selected_product(self):
        # Get the selected row
        selected_row = self.tableWidget.currentRow()

        if selected_row == -1:
            QtWidgets.QMessageBox.warning(None, "Warning", "No row selected!")
            return

        # Get MaHD and MaSP from the selected row
        maHD = self.lineEdit.text() # Assuming MaHD is in the first column
        maSP_item = self.tableWidget.item(selected_row, 0)  # Assuming MaSP is in the second column

        if not maHD or not maSP_item:
            QtWidgets.QMessageBox.warning(None, "Warning", "Invalid row selection!")
            return


        maSP = maSP_item.text()

        # Connect to the database
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',  # replace with your MySQL username
                password='123456789ab',  # replace with your MySQL password
                database='QLCHTC'  # replace with your database name
            )
            cursor = connection.cursor()

            # Delete the data from the ChiTietHoaDon table
            delete_query = ("DELETE FROM ChiTietHoaDon WHERE MaHD = %s AND MaSP = %s")
            cursor.execute(delete_query, (maHD, maSP))
            connection.commit()

            # Close the connection
            cursor.close()
            connection.close()

            # Remove the row from the table widget
            self.tableWidget.removeRow(selected_row)

            # Optionally, recalculate the total amount if applicable
            self.calculate_total()
            self.load_data()

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(None, "Database Error", f"Error: {err}")
    def tim_kiem_san_pham(self):
        ten_sp = self.lineEdit_6.text()

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

            self.tableWidget_2.setRowCount(0)
            for row_number, row_data in enumerate(rows):
                self.tableWidget_2.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(None, "Error", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

    def lamMoiNgay(self):
        # Implement clearing input fields
        self.lineEdit_5.setDate(QtCore.QDate.currentDate())

    def add_product(self):
        # Get the data from the input fields
        maHD = self.lineEdit.text()
        masp =self.lineEdit_30.text()
        tenSP = self.lineEdit_2.text()
        soLuong = self.lineEdit_4.text()
        gia = self.lineEdit_3.text()


        if not maHD or not tenSP or not soLuong or not gia:
            QtWidgets.QMessageBox.warning(None, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
            return False

            # Kiểm tra nếu số lượng là số nguyên dương
        if not soLuong.isdigit() or int(soLuong) <= 0:
            QtWidgets.QMessageBox.warning(None, "Lỗi", "Số lượng phải là số nguyên dương hợp lệ.")
            return False

        # Connect to the database
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',  # replace with your MySQL username
                password='123456789ab',  # replace with your MySQL password
                database='QLCHTC'  # replace with your database name
            )
            cursor = connection.cursor()
            cursor.execute("SELECT SoLuong FROM SanPham WHERE MaSP = %s", (masp,))
            ket_qua = cursor.fetchone()

            if ket_qua is not None:
                soluong_hienco = ket_qua[0]

                # Kiểm tra số lượng yêu cầu với số lượng hiện có
                if int(soLuong) > soluong_hienco:
                    QtWidgets.QMessageBox.warning(None, "Lỗi", "Số lượng yêu cầu vượt quá số lượng hiện có trong kho.")
                    cursor.close()
                    connection.close()
                    return False
            # Insert the data into the SanPham table
            query = ("INSERT INTO ChiTietHoaDon (MaHD,MaSP,TenSP,SoLuong,Gia) "
                     "VALUES (%s,%s, %s, %s, %s)")
            data = (maHD,masp,tenSP,soLuong,gia)
            cursor.execute(query, data)
            connection.commit()

            # Close the connection
            cursor.close()
            connection.close()
            self.update_table_widget(masp, tenSP, soLuong, gia)
            self.load_data()
            self.lineEdit_30.clear()
            self.lineEdit_2.clear()
            self.lineEdit_4.clear()
            self.lineEdit_3.clear()




        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def update_table_widget(self, masp, tenSP, soLuong, gia):
        # Determine the current row count
        current_row_count = self.tableWidget.rowCount()

        # Insert a new row at the end
        self.tableWidget.insertRow(current_row_count)

        # Set the data for each column in the new row

        self.tableWidget.setItem(current_row_count, 0, QtWidgets.QTableWidgetItem(masp))
        self.tableWidget.setItem(current_row_count, 1, QtWidgets.QTableWidgetItem(tenSP))
        self.tableWidget.setItem(current_row_count, 2, QtWidgets.QTableWidgetItem(soLuong))
        self.tableWidget.setItem(current_row_count, 3, QtWidgets.QTableWidgetItem(gia))
    def create_invoice(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='123456789ab',
                database='QLCHTC'
            )
            cursor = connection.cursor()

            # Truy vấn để lấy MaHD lớn nhất từ bảng HoaDon
            cursor.execute("SELECT MAX(MaHD) FROM HoaDon")
            max_maHD = cursor.fetchone()[0]  # Lấy giá trị MaHD lớn nhất

            # Nếu không có dữ liệu, gán max_maHD = 0
            if max_maHD is None:
                max_maHD = 0

            # Tăng max_maHD lên 1 để làm MaHD mới
            new_maHD = max_maHD + 1

            # Hiển thị new_maHD lên QLineEdit
            self.lineEdit.setText(str(new_maHD))

            # Đóng kết nối
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def save_invoice(self):
        # Lấy MaHD và MaNV từ các trường nhập liệu
        maHD = int (self.lineEdit.text())
        maNV = int(self.comboBox.currentText())


        # Tính tổng tiền từ widget bảng
        total_amount = self.label_120.text()
        if not maHD or not maNV:
            QtWidgets.QMessageBox.warning(None, 'Lỗi', 'Vui lòng nhập đủ thông tin MaHD và MaNV.')
            return


        current_date = self.lineEdit_5.date().toString(QtCore.Qt.DateFormat.ISODate)

        # Thiết lập kết nối
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # thay bằng tên người dùng MySQL của bạn
            password='123456789ab',  # thay bằng mật khẩu MySQL của bạn
            database='QLCHTC'  # thay bằng tên cơ sở dữ liệu của bạn
        )
        cursor = connection.cursor()

        try:
            # Thêm dữ liệu vào bảng HoaDon
            query = ("INSERT INTO HoaDon (MaHD, MaNV, NgayLap, TongTien) "
                     "VALUES (%s, %s, %s, %s)")
            data = (maHD, maNV, current_date, total_amount)

            cursor.execute(query, data)
            connection.commit()

            # Thông báo cho người dùng về thao tác thành công
            QtWidgets.QMessageBox.information(None, 'Thành công', 'Đã lưu hóa đơn thành công.')

            # Cập nhật lại bảng
            self.refresh_table()
            self.lineEdit_30.clear()
            self.lineEdit_2.clear()
            self.lineEdit_4.clear()
            self.lineEdit_3.clear()
            self.lineEdit.clear()

        except mysql.connector.Error as error:
            # Xử lý lỗi khi thêm vào cơ sở dữ liệu
            QtWidgets.QMessageBox.warning(None, 'Lỗi', f'Lỗi khi lưu hóa đơn: {error}')

        finally:
            # Đóng kết nối
            cursor.close()
            connection.close()

    def refresh_table(self):
        # Xóa tất cả các hàng hiện có trong bảng
        self.tableWidget.setRowCount(0)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
