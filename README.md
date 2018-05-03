# chrome_password_extractor

**Disclaimer: Please note that while I am the one who wrote this script, I am not in any way responsible for any individual who uses this for any unethical stuff.**

The chrome_password_extractor is a tool I've designed to grab saved passwords from an individual's google chrome browser.

There are three folders inside the repo in which you will find your executables and python source files. I used the pyinstaller module to freeze the source codes.

## Combined

The Executable present in Combined will essentially grab the login data file of Chrome, name it 'cleaned' and decrypt in and store it in a text file called 'a.txt'

## Obtainer

The Executable present in Obtained will essentially grab the google login data and store it. This is a better option to remain undeteced while using the hack as the owner will not be able to open the file and thus will be less suspicious of it and you can safely decrypt it later.

## Decrypter

The Executable present in the Decrypter will ask you for the name of the file you need to decrypt. Just copy the file file obtained in by the obtainer script into the folder and execute the scipt and you will obtain a txt file 'a.txt' which will contain all the passwords.