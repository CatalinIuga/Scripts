import zipfile
import pyfiglet
import sys
import os
import time

# TODO better input and maybe a manual page + possibly a default wordlist that is included with the script maybe...?

ascii_banner = pyfiglet.figlet_format("zCrack")
print(ascii_banner)

if len(sys.argv) < 3:
    print("You need to specify a wordlist and a zip file!")
    wordlist = input('Enter the wordlist path: ')
    zip_file = input('Enter the zipfile: ')
    if wordlist=='' or zip_file=='':
        exit()
elif len(sys.argv) > 3:
    print("Too many arguments!")
    exit()
else:
    wordlist = sys.argv[1]
    zip_file = zipfile.ZipFile(sys.argv[2])

with open(wordlist, 'r') as fi:
    passwords = fi.readlines()
    for password in passwords:
        try:
            zip_file.extractall(
                path='result', pwd=bytes(password.strip(), 'utf8'))
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
