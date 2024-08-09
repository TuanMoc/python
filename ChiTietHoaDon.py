import Dataconnection
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ChiTietHoaDonDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(621, 393)
        self.pushButton_13 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(0, 200, 121, 20))
        self.pushButton_13.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_9 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 110, 121, 20))
        self.pushButton_9.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 140, 121, 20))
        self.pushButton_10.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_12 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(0, 260, 121, 20))
        self.pushButton_12.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_11 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(0, 230, 121, 20))
        self.pushButton_11.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_6 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 170, 121, 20))
        self.pushButton_6.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.listWidget_3 = QtWidgets.QListWidget(parent=Dialog)
        self.listWidget_3.setGeometry(QtCore.QRect(0, 0, 121, 391))
        self.listWidget_3.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                        "background-color: rgb(170, 170, 127);")
        self.listWidget_3.setObjectName("listWidget_3")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(220, 20, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.listWidget_4 = QtWidgets.QListWidget(parent=Dialog)
        self.listWidget_4.setGeometry(QtCore.QRect(110, 0, 511, 91))
        self.listWidget_4.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                        "background-color: rgb(170, 170, 127);")
        self.listWidget_4.setObjectName("listWidget_4")
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setGeometry(QtCore.QRect(120, 90, 531, 311))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 261, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(140, 20, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 70, 580, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)  # Set to the number of columns you want to display
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 20, 131, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.listWidget_4.raise_()
        self.listWidget_3.raise_()
        self.pushButton_13.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.pushButton_12.raise_()
        self.pushButton_11.raise_()
        self.pushButton_6.raise_()
        self.label_2.raise_()
        self.frame.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_3.clicked.connect(self.searchChiTietHoaDon)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_13.setText(_translate("Dialog", "NHÀ CUNG CẤP"))
        self.pushButton_9.setText(_translate("Dialog", "BÁN HÀNG"))
        self.pushButton_10.setText(_translate("Dialog", "NHÂN VIÊN"))
        self.pushButton_12.setText(_translate("Dialog", "THỐNG KÊ"))
        self.pushButton_11.setText(_translate("Dialog", "CHI TIẾT HÓA ĐƠN"))
        self.pushButton_6.setText(_translate("Dialog", "SẢN PHẨM"))
        self.label_2.setText(_translate("Dialog", "QUẢN LÝ CỬA HÀNG THÚ CƯNG"))
        self.label.setText(_translate("Dialog", "Tìm Kiếm Theo Mã HD:"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Tên SP"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Số Lượng"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Giá"))

        self.pushButton_3.setText(_translate("Dialog", "Tìm Kiếm"))

    def searchChiTietHoaDon(self):
        ma_sp = self.lineEdit.text()
        if not ma_sp:
            QtWidgets.QMessageBox.warning(None, 'Error', 'Vui lòng nhập mã hóa đơn cần tìm !.')
            return

        connection = Dataconnection.connectdatabase()
        query = "SELECT TenSP, SoLuong, Gia FROM ChiTietHoaDon WHERE MaSP = %s"
        cursor = connection.cursor()
        cursor.execute(query, (ma_sp,))
        results = cursor.fetchall()
        connection.close()
        if not results:
            QtWidgets.QMessageBox.information(None, 'Information', 'Hóa đơn này không có sản phẩm nào !.')

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(results):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ChiTietHoaDonDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
