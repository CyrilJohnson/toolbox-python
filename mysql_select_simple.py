#!/usr/bin/python
import MySQLdb
db_connect = MySQLdb.connect(host = 'mysql.khmel.org', port = 3306, user = 'khmel', passwd = 'password', db = 'khmel')
cursor = db_connect.cursor()
cursor.execute('SELECT * FROM test_table')
db_connect.commit()
sqlout = cursor.fetchall()
for item in sqlout:
    print(item)
db_cursor = cursor.close ()
db_connect.close()
