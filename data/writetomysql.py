import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import datetime

def inserttoDB(idd, firs, last, pul,bp,bo):
    d = datetime.datetime.today()
    da = d.strftime("%Y-%m-%d %H:%M:%S")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='hw5DB',
                                             user='root',
                                             password='password')
        mySql_insert_query = """INSERT INTO healthstate (id, firstname, lastname, pulse,blood_pressure,blood_oxygen,date) 
                               VALUES 
                               (%s, %s, %s, %s,%s,%s,%s)"""

        recordTuple = (idd, firs, last, pul,bp,bo,da)

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into healthstate table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into healthstate table {}".format(error))

    finally:
        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")