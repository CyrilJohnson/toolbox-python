#!/usr/bin/python
import MySQLdb

class database:
    def __init__(self):
        self.db_host = 'mysql.khmel.org'
        self.db_port = 3306
        self.db_user = 'khmel'
        self.db_pass = 'password'
        self.db_name = 'khmel'
        # Create Database connection
        try:
            self.db_connect = MySQLdb.connect(host = self.db_host, port = self.db_port, user = self.db_user, passwd = self.db_pass, db = self.db_name)
            # Create cursor
            self.cursor = self.db_connect.cursor()
        except MySQLdb.Error, e:
            print e.args
            print 'ERROR: %d: %s' % (e.args[0], e.args[1])
            sys.exit(1)

    def request(self,sql):
        self.cursor.execute(sql)
        self.sqlout = self.cursor.fetchall()

    def insert(self,sql):
        try:
            self.cursor.execute(sql)
            self.db_connect.commit()
        except MySQLdb.Error, e:
            print e.args
            print "ERROR: %d: %s" % (e.args[0], e.args[1])

    def __del__(self):
        # Close cursor
        self.cursor.close ()
        # Close DB
        self.db_connect.close()
        print 'Database connection closed'

class sql_creator:
    def sql_select(self,column):
        self.sql_out = "SELECT " + column + " FROM test_table"

# Create objects
db = database()
sql_string = sql_creator()

# Execute SQL request
sql_string.sql_select('*')
sql = sql_string.sql_out
db.request(sql)

# Print data
for item in db.sqlout:
    print(item)

del db
