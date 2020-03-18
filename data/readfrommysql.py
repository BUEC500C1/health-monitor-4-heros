import mysql.connector
from mysql.connector import Error

def read():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='hw5DB',
                                             user='root',
                                             password='password')

        sql_select_Query = "select * from healthstate"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total number of rows in healthstate is: ", cursor.rowcount)

        print("\nPrinting each laptop record")
        for row in records:
            print("Id = ", row[0], )
            print("firstname = ", row[1])
            print("lastname  = ", row[2])
            print("pulse = ", row[3])
            print("blood pressure  = ", row[4])
            print("blood oxygen  = ", row[5])
            print("date  = ", row[6], '\n')

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def highbp():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='hw5DB',
                                             user='root',
                                             password='password')

        sql_select_Query = """SELECT * FROM healthstate 
        WHERE blood_pressure > 140"""
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total record of high blood pressure is: ", cursor.rowcount)

        for row in records:
            print("Id = ", row[0], )
            print("firstname = ", row[1])
            print("lastname  = ", row[2])
            print("pulse = ", row[3])
            print("blood pressure  = ", row[4])
            print("blood oxygen  = ", row[5])
            print("date  = ", row[6], '\n')

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def lowbp():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='hw5DB',
                                             user='root',
                                             password='password')

        sql_select_Query = """SELECT * FROM healthstate 
        WHERE blood_pressure < 90"""
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total record of low blood pressure is: ", cursor.rowcount)

        for row in records:
            print("Id = ", row[0], )
            print("firstname = ", row[1])
            print("lastname  = ", row[2])
            print("pulse = ", row[3])
            print("blood pressure  = ", row[4])
            print("blood oxygen  = ", row[5])
            print("date  = ", row[6], '\n')

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def findhistory(f,l):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='hw5DB',
                                             user='root',
                                             password='password')

        sql_select_Query = """SELECT * FROM healthstate 
        WHERE firstname = %s and lastname = %s"""
        cursor = connection.cursor()
        cursor.execute(sql_select_Query,(f,l))
        records = cursor.fetchall()
        print("Total number of records of" + f +' '+ l +"is: ", cursor.rowcount)

        for row in records:
            print("Id = ", row[0], )
            print("firstname = ", row[1])
            print("lastname  = ", row[2])
            print("pulse = ", row[3])
            print("blood pressure  = ", row[4])
            print("blood oxygen  = ", row[5])
            print("date  = ", row[6], '\n')

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def recordofpatient(f,l):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='hw5DB',
                                             user='root',
                                             password='password')

        sql_select_Query = """SELECT * FROM healthstate 
        WHERE firstname = %s and lastname = %s"""
        cursor = connection.cursor()
        cursor.execute(sql_select_Query,(f,l))
        records = cursor.fetchall()
        print("Total number of records of" + f +' '+ l +"is: ", cursor.rowcount)

        for row in records:
            print("Id = ", row[0], )
            print("firstname = ", row[1])
            print("lastname  = ", row[2])
            print("pulse = ", row[3])
            print("blood pressure  = ", row[4])
            print("blood oxygen  = ", row[5])
            print("date  = ", row[6], '\n')

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def lateststate(f,l):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='hw5DB',
                                             user='root',
                                             password='password')

        sql_select_Query = """SELECT m1.*
        FROM healthstate m1 LEFT JOIN healthstate m2
        ON (m1.firstname = m2.firstname = %s AND m1.lastname = m2.lastname = %s AND m1.id < m2.id)
        WHERE m2.id is NULL"""
        cursor = connection.cursor()
        cursor.execute(sql_select_Query,(f,l))
        records = cursor.fetchall()
        print(f+ ' ' + l + " latest health state is: ")
        for row in records:
            print("Id = ", row[0])
            print("firstname = ", row[1])
            print("lastname  = ", row[2])
            print("pulse = ", row[3])
            if row[4] > 100:
                print("high pulse")
            elif row[4] < 60:
                print("low pulse")
            print("blood pressure  = ", row[4])
            if row[4] > 140:
                print("high blood pressure")
            elif row[4] < 90:
                print("low blood pressure")
            print("blood oxygen  = ", row[5])
            if row[5] > 100:
                print("high blood oxygen")
            elif row[5] < 75:
                print("low blood oxygen")
            print("date  = ", row[6], '\n')

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

# if __name__ == '__main__':
#     lateststate('z','s')