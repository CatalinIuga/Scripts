import zipfile
import sys
from os import rmdir
from time import sleep

# TODO add better input check and man page + maybe more options

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
                rmdir(password.strip())
            except:
                continue
    else:
            print('Password was not found in the wordlist :(')
# sleep(5) # i was using it from outside terminal and i wanted to actualy see the result