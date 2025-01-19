
import mysql.connector
import time

connectionstart = time.time()
connection = mysql.connector.connect(
    user="****",
    password="****",
    host="mysql.metropolia.fi",
    port=3306,
    database="****",
    connection_timeout=60,
    autocommit = True
)
connectedtime = time.time()

def print_connection_time():
    print(f'Connected to the database in {connectedtime - connectionstart} seconds.')

def get_start_time():
    return connectedtime
