#!/usr/bin/python
import sqlite3
conn = sqlite3.connect('./example.db')
c = conn.cursor()
c.execute('CREATE TABLE projects (date_day TEXT, project TEXT, user TEXT, seconds INTEGER, seconds_pend INTEGER, jobs INTEGER, PRIMARY KEY (date_day, project, user) )')
conn.commit()
conn.close()

