#!/usr/bin/python
import MySQLdb,os,sys,time,datetime
from operator import itemgetter

class database:
    def __init__(self):
        self.db_host = '127.0.0.1'
        self.db_port = 3306
        self.db_user = 'test'
        self.db_pass = 'test'
        self.db_name = 'test'
        # Create DB connection
        self.db_connect = MySQLdb.connect(host = self.db_host, port = self.db_port, user = self.db_user, passwd = self.db_pass, db = self.db_name)
        # Create cursor
        self.cursor = self.db_connect.cursor()

    def request(self,sql):
        self.cursor.execute(sql)
        self.sqlout = self.cursor.fetchall()

    def __del__(self):
        # Close cursor
        self.cursor.close ()
        # Close DB
        self.db_connect.close()
        print 'Database connection closed'


class sql_creator:
    def sql_one_day_sum(self):
        self.sql_out = "SELECT * FROM my_table"

db = database()
sql_string = sql_creator()


###################
### change next line for real test
###################
#sql_string.sql_select_volumes(date_mod.local_time)
sql_string.sql_one_day_sum()
sql = sql_string.sql_out
db.request(sql)
sql_data = db.sqlout

##########
# SQLITE #
##########

import sqlite3
conn = sqlite3.connect('./example.db')
c = conn.cursor()
for item in sql_data:
    temp_insert = (str(item[0]),item[1],item[2],int(item[3]),int(item[4]),int(item[5]))
    print(temp_insert)
    try:
        c.executemany('INSERT INTO projects(date_day, project, user, seconds, seconds_pend, jobs) VALUES(?,?,?,?,?,?)', (temp_insert,) )
    except Exception as e:
        print(e)
conn.commit()
conn.close()
del db
