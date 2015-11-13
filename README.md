# Toolbox Python

Collections of different small Python scripts or scripts examples.

## mysql_select_extended.py

Extended example of select from MySQL database with OOP.

You will need to install MySQLdb.

## mysql_select_simple.py

Basic example of select from MySQL database.

You will need to install MySQLdb.

## sqlite_create_db.py

Creating sqlite database.

## sqlite_import_from_mysql.py

Example of select from mysql and insert to sqlite.

## ssh_expect.py

Example of expect usage for ssh login with password.

## aws_list.py

Example of boto usage to connect AWS.

You need to get boto from https://aws.amazon.com/sdk-for-python/

You need to get:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- REGION

## date_manipulation.py

Example script to manipulate dates in python. Script will take last line from file and will try to modify date.

It expects /var/log/syslog lines like:

```bash
Nov 12 15:17:01 test-srv ........
```

Usage:
```bash
chmod +x date_manipulation.py
./date_manipulation.py
```

Output example:
```
### Log check Python ###
String from log file:     Nov 13 12:30:11
Date from log in seconds: 1447414211
Date_time now in seconds: 1447414645
It happend                434 seconds ago
It happend                7 minutes ago
```

## ftp_upload_file.py

Example script to upload or replace file on FTP server.
