#!/usr/bin/python
import ftplib
host="example.com";
user="phn";
pw="PASSWORD";
file="phn.log";
s = ftplib.FTP(host,user,pw) # Connect
s.set_pasv(1)
s.delete(file) # delete the file
f = open(file, "rb") # file to send
s.storbinary("STOR phn.log", f) # Send the file
f.close() # Close file and FTP
s.quit()
