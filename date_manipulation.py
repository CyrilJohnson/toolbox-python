#!/usr/bin/python
import sys
import time
import datetime

print("### Log check Python ###")
# Get date from log file
file_name="/var/log/syslog"
searched_string="TEST MESSAGE"
my_string = ""

with open(file_name, "rb") as f:
    first = f.readline()
    for last_line in f:
        pass

date_time_from_log = last_line[:15]
print("String from log file:     " + date_time_from_log)

# Convert Human date to EPOCH time in seconds
now = datetime.datetime.now()
year_now = " %d" % now.year
date_time = date_time_from_log + year_now
pattern = "%b %d %H:%M:%S %Y"
date_string_to_seconds = int(time.mktime(time.strptime(date_time, pattern)))
print("Date from log in seconds: " + str(date_string_to_seconds))

# Date now in EPOCH
date_time_now_in_seconds = int(time.time())
print("Date_time now in seconds: " + str(date_time_now_in_seconds))

# Result
result = date_time_now_in_seconds - date_string_to_seconds
print("It happend                " + str(result) + " seconds ago")
result_2 = int(result / 60)
print("It happend                " + str(result_2) + " minutes ago")
