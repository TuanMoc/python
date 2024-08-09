from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error

class Ui_NhaCungCapDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(762, 422)
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
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setGeometry(QtCore.QRect(120, 80, 711, 411))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 371, 192))
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
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(240, 10, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 230, 641, 111))
        self.frame_2.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(170, 30, 151, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(30, 30, 251, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(430, 20, 151, 17))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 40, 151, 17))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_9.setGeometry(QtCore.QRect(430, 60, 151, 17))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(430, 80, 151, 17))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_8.raise_()
        self.lineEdit_6.raise_()
        self.pushButton.raise_()
        self.pushButton_6.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(380, 50, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(380, 80, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setGeometry(QtCore.QRect(380, 110, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setGeometry(QtCore.QRect(380, 140, 161, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        self.label_7.setGeometry(QtCore.QRect(390, 170, 161, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(430, 50, 151, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 80, 151, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(430, 110, 151, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(430, 140, 151, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(430, 170, 151, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.load_suppliers()

        self.pushButton_6.clicked.connect(self.add_supplier)  # Connect the button click to the function
        self.pushButton.clicked.connect(self.search_supplier)  # Connect the search button click to the search function

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_5.setText(_translate("Dialog", "NHÀ CUNG CẤP"))
        self.pushButton_4.setText(_translate("Dialog", "SẢN PHẨM"))
        self.pushButton_7.setText(_translate("Dialog", "CHI TIẾT HÓA ĐƠN"))
        self.pushButton_8.setText(_translate("Dialog", "THỐNG KÊ"))
        self.pushButton_3.setText(_translate("Dialog", "NHÂN VIÊN"))
        self.pushButton_2.setText(_translate("Dialog", "BÁN HÀNG"))
        self.label.setText(_translate("Dialog", "QUẢN LÝ CỬA HÀNG THÚ CƯNG"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "MaNCC"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "TenNCC"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "DiaChi"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "DienThoai"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Email"))
        self.label_2.setText(_translate("Dialog", "DANH SÁCH NHÀ CUNG CẤP"))
        self.label_8.setText(_translate("Dialog", "Nhập tên nhà cung cấp cần tìm:"))
        self.pushButton.setText(_translate("Dialog", "Tìm Kiếm Nhà Cung Cấp"))
        self.pushButton_6.setText(_translate("Dialog", "Thêm Nhà Cung Cấp"))
        self.pushButton_9.setText(_translate("Dialog", "Sửa Nhà Cung Cấp"))
        self.pushButton_10.setText(_translate("Dialog", "Xóa Nhà Cung Cấp"))
        self.label_3.setText(_translate("Dialog", "MaNCC:"))
        self.label_4.setText(_translate("Dialog", "TenNCC:"))
        self.label_5.setText(_translate("Dialog", "Địa Chỉ:"))
        self.label_6.setText(_translate("Dialog", "Điện Thoại:"))
        self.label_7.setText(_translate("Dialog", "Email:"))


        self.pushButton_9.clicked.connect(self.edit_supplier)  # Connect edit button click to edit function
        self.pushButton_10.clicked.connect(self.delete_supplier)  # Connect delete button click to delete function
        self.tableWidget.clicked.connect(self.fill_supplier_data)

    def fill_supplier_data(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            ma_ncc = self.tableWidget.item(selected_row, 0).text()
            ten_ncc = self.tableWidget.item(selected_row, 1).text()
            dia_chi = self.tableWidget.item(selected_row, 2).text()
            dien_thoai = self.tableWidget.item(selected_row, 3).text()
            email = self.tableWidget.item(selected_row, 4).text()

            # Điền dữ liệu vào các ô nhập liệu
            self.lineEdit.setText(ma_ncc)
            self.lineEdit_2.setText(ten_ncc)
            self.lineEdit_3.setText(dia_chi)
            self.lineEdit_4.setText(dien_thoai)
            self.lineEdit_5.setText(email)
    def add_supplier(self):
        # Get input values from the form
        ma_ncc = self.lineEdit.text()
        ten_ncc = self.lineEdit_2.text()
        dia_chi = self.lineEdit_3.text()
        dien_thoai = self.lineEdit_4.text()
        email = self.lineEdit_5.text()

        # Database connection parameters
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

                # SQL query to insert data into NhaCungCap table
                insert_query = """
                INSERT INTO NhaCungCap (MaNCC, TenNCC, DiaChi, DienThoai, Email)
                VALUES (%s, %s, %s, %s, %s)
                """
                record = (ma_ncc, ten_ncc, dia_chi, dien_thoai, email)
                cursor.execute(insert_query, record)
                connection.commit()

                QtWidgets.QMessageBox.information(None, 'Success', 'Nhà cung cấp đã được thêm thành công')

                # Clear input fields
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
                self.lineEdit_4.clear()
                self.lineEdit_5.clear()

                # Update the table view
                self.load_suppliers()

        except Error as e:
            print(f"Error: {e}")
            QtWidgets.QMessageBox.critical(None, 'Error', f"Error: {e}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def search_supplier(self):
        # Get the name of the supplier to search for
        search_name = self.lineEdit_6.text()

        # Database connection parameters
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
                # SQL query to search for suppliers by name
                search_query = """
                SELECT MaNCC, TenNCC, DiaChi, DienThoai, Email FROM NhaCungCap
                WHERE TenNCC LIKE %s
                """
                cursor.execute(search_query, ('%' + search_name + '%',))
                rows = cursor.fetchall()

                # Clear the table
                self.tableWidget.setRowCount(0)

                # Populate the table with search results
                for row in rows:
                    row_position = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_position)
                    for column, data in enumerate(row):
                        self.tableWidget.setItem(row_position, column, QtWidgets.QTableWidgetItem(str(data)))

        except Error as e:
            print(f"Error: {e}")
            QtWidgets.QMessageBox.critical(None, 'Error', f"Error: {e}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    def edit_supplier(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'Vui lòng chọn nhà cung cấp cần sửa')
            return

        ma_ncc = self.lineEdit.text()
        ten_ncc = self.lineEdit_2.text()
        dia_chi = self.lineEdit_3.text()
        dien_thoai = self.lineEdit_4.text()
        email = self.lineEdit_5.text()

        # Database connection parameters
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

                # SQL query to update data in NhaCungCap table
                update_query = """
                UPDATE NhaCungCap
                SET TenNCC = %s, DiaChi = %s, DienThoai = %s, Email = %s
                WHERE MaNCC = %s
                """
                record = (ten_ncc, dia_chi, dien_thoai, email, ma_ncc)
                cursor.execute(update_query, record)
                connection.commit()

                QtWidgets.QMessageBox.information(None, 'Success', 'Nhà cung cấp đã được sửa thành công')

                # Clear input fields
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
                self.lineEdit_4.clear()
                self.lineEdit_5.clear()

                # Update the table view
                self.load_suppliers()

        except Error as e:
            print(f"Error: {e}")
            QtWidgets.QMessageBox.critical(None, 'Error', f"Error: {e}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete_supplier(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'Vui lòng chọn nhà cung cấp cần xóa')
            return

        ma_ncc = self.tableWidget.item(selected_row, 0).text()

        # Database connection parameters
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

                # SQL query to delete data from NhaCungCap table
                delete_query = """
                DELETE FROM NhaCungCap
                WHERE MaNCC = %s
                """
                cursor.execute(delete_query, (ma_ncc,))
                connection.commit()

                QtWidgets.QMessageBox.information(None, 'Success', 'Nhà cung cấp đã được xóa thành công')

                # Update the table view
                self.load_suppliers()

        except Error as e:
            print(f"Error: {e}")
            QtWidgets.QMessageBox.critical(None, 'Error', f"Error: {e}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def edit_supplier(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'Vui lòng chọn nhà cung cấp cần sửa')
            return

        ma_ncc = self.lineEdit.text()
        ten_ncc = self.lineEdit_2.text()
        dia_chi = self.lineEdit_3.text()
        dien_thoai = self.lineEdit_4.text()
        email = self.lineEdit_5.text()

        # Database connection parameters
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

                # SQL query to update data in NhaCungCap table
                update_query = """
                UPDATE NhaCungCap
                SET TenNCC = %s, DiaChi = %s, DienThoai = %s, Email = %s
                WHERE MaNCC = %s
                """
                record = (ten_ncc, dia_chi, dien_thoai, email, ma_ncc)
                cursor.execute(update_query, record)
                connection.commit()

                QtWidgets.QMessageBox.information(None, 'Success', 'Nhà cung cấp đã được sửa thành công')

                # Clear input fields
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
                self.lineEdit_4.clear()
                self.lineEdit_5.clear()

                # Update the table view
                self.load_suppliers()

        except Error as e:
            print(f"Error: {e}")
            QtWidgets.QMessageBox.critical(None, 'Error', f"Error: {e}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete_supplier(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'Vui lòng chọn nhà cung cấp cần xóa')
            return

        ma_ncc = self.tableWidget.item(selected_row, 0).text()

        # Database connection parameters
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

                # SQL query to delete data from NhaCungCap table
                delete_query = """
                DELETE FROM NhaCungCap
                WHERE MaNCC = %s
                """
                cursor.execute(delete_query, (ma_ncc,))
                connection.commit()

                QtWidgets.QMessageBox.information(None, 'Success', 'Nhà cung cấp đã được xóa thành công')

                # Update the table view
                self.load_suppliers()

        except Error as e:
            print(f"Error: {e}")
            QtWidgets.QMessageBox.critical(None, 'Error', f"Error: {e}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def load_suppliers(self):
        # Database connection parameters
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
                cursor.execute("SELECT MaNCC, TenNCC, DiaChi, DienThoai, Email FROM NhaCungCap")
                rows = cursor.fetchall()

                # Clear the table
                self.tableWidget.setRowCount(0)

                # Populate the table with new data
                for row in rows:
                    row_position = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_position)
                    for column, data in enumerate(row):
                        self.tableWidget.setItem(row_position, column, QtWidgets.QTableWidgetItem(str(data)))

        except Error as e:
            print(f"Error: {e}")
            QtWidgets.QMessageBox.critical(None, 'Error', f"Error: {e}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_NhaCungCapDialog()
    ui.setupUi(Dialog)
    ui.load_suppliers()  # Load suppliers when the dialog is shown
    Dialog.show()
    sys.exit(app.exec())
