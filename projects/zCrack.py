import zipfile
import sys
import os
import time


if len(sys.argv) < 3:
    print("U need to specify a wordlist and a zip file!")
    exit()

wordlist = sys.argv[1]
zip_file = zipfile.ZipFile(sys.argv[2])

with open(wordlist, 'r') as fi:
    passwords = fi.readlines()
    for password in passwords:
        try:
            zip_file.extractall(path='result', pwd=bytes(password.strip(),'utf8'))
            print('SUCCESS: password is ' + password.strip())
            break
        except:
            print('TRYING: password ' + password.strip() + ' is invalid')
            try:
                os.rmdir(password.strip())
            except:
                print(password.strip())
print('Password was not found in the wordlist :(')
time.sleep(5)