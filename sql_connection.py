import mysql.connector

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          # Change to your MySQL username
            password="root123",  # Change to your MySQL password
            database="employee"     # Change to your MySQL database name
        )
        return connection
    except Exception as e:
        print("Database connection error")
        print(e)
        return None