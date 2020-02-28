import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="root", password="sparks123", port="3310", database="pythondb")

cur = myconn.cursor()
try:
    cur.execute("select * from employee")

    result = cur.fetchall()

    for x in result:
        print(x)
except:
    myconn.rollback()

myconn.close()
