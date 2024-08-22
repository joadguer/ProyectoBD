import mysql.connector
from mysql.connector import Error

def connect_to_database(username, clave):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user=username,
            password=clave
        )
        if connection.is_connected():
            print("Conectado exitosamente")
            return True
        else:
            return False
    except Error as e:
        print(f"Error: {e}")
        return False
    finally:
        if connection.is_connected():
            connection.close()
