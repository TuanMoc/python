# Dataconnection.py
import mysql.connector
from mysql.connector import Error

def connectdatabase():
    """Tạo và trả về kết nối cơ sở dữ liệu MySQL"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='QLCHTC',
            user='root',
            password='123456789ab'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def close_connection(connection):
    """Đóng kết nối cơ sở dữ liệu MySQL."""
    if connection.is_connected():
        connection.close()
