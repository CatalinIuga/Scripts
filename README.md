# SCRIPTS
## 1) zCrack
Python3 script to brute force .zip archive that are secured with passwords.
- Usage:\
    -> python3 zCrack.py {wordlist} {zip_archive}\
- You can use my 10k password list bellow if u dont have one already

## 2) decCaesar
Decode Caesar cipher. It iterates through all the possible 26 combinations of keys and find the most readable text it can find. 
- TODO -> both way shift and multiple languages check
- Usage:\
    -> python3 decCaesar.py ['text_to_decode']

## 3) opScanner
Find open ports of a cetrain host. You can specify a certain port or scan all all possible 65535 possible ports.
- TODO -> maybe add functionality for directory scan
- Usage:\
    -> python3 opScanner.py [host] [port]