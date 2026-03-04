import mysql.connector 
from dotenv import load_dotenv
import os

load_dotenv()


try:
    con = mysql.connector.connect(
    host=os.getenv('DB_HOST'), 
    database=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD')
    )
    cursor = con.cursor()
    cursor.execute("select database();")
    line_response = cursor.fetchone()
    print("Connected with database: ", line_response[0])

except mysql.connector as e:
     print(f"Error trying to connect to MySQL: {e}")

finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print(f"Connection with MySQL is ended")