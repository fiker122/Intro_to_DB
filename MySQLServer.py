# MySQLServer.py

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    conn = mysql.connector.connect(
        host="localhost",       # change if needed
        user="root",            # your MySQL username
        password="yourpassword" # your MySQL password
    )

    if conn.is_connected():
        cursor = conn.cursor()
        # Create database, will not fail if it exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()