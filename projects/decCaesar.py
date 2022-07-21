from string import ascii_lowercase
import sys
from time import sleep
from enchant.checker import SpellChecker

# TODO not bad can be better, esp the spell check

def is_valid(decoded):
    max_pct = decoded.split()
    check = SpellChecker('en_US')
    check.set_text(decoded)
    err_no = [eror for eror in check]
    return len(max_pct) - len(err_no)

def dict_sort(x):
    return dict(sorted(x.items(), key=lambda item: item[1]))
    

results = {}
to_dec = sys.argv[1].lower()
alp = ascii_lowercase
for i in range(0,26):
    aux = alp[i%26:] + alp[:i%26]
    dec = ''
    for l in to_dec:
        if l == ' ' or l.isnumeric():
            dec +=l
        else:
            dec+= alp[aux.find(l)]
    results[dec] = is_valid(dec)
results = dict_sort(results)
for d in results.keys():
    print(d,results[d])