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
    return (len(max_pct) - len(err_no))/len(max_pct)*100


if len(sys.argv) <= 1:
    print('Enter a string to decript ')
    inp = input()
    if len(inp) == 0:
        print('Emplty string not accepted!')
        exit()
elif len(sys.argv) >= 3:
    print('Too many arguments. If the string contains whitespaces make sure to use \'\' or ""')
    exit()
else:
    inp = sys.argv[1]

result_string = []
result_succes_r8 = []
to_dec = inp.lower()
alp = ascii_lowercase
for i in range(0, 26):
    aux = alp[i % 26:] + alp[:i % 26]
    dec = ''
    for l in to_dec:
        if l == ' ' or l.isnumeric():
            dec += l
        else:
            dec += alp[aux.find(l)]
    result_string.append(dec)
    result_succes_r8.append(is_valid(dec))

if(max(result_succes_r8) == 0):
    print('The resulted string dosent look readable. Perhaps the \' \' was swapped for another letter.')
    print('Possible solutions are:')
else:
    print('Found valid english words in the following solutions:')
print('<------------------------------------->\nWord\tValidation percentage\n<------------------------------------->')
for i in range(len(result_string)):
    best = result_succes_r8.index(max(result_succes_r8))
    print(result_string.pop(best), result_succes_r8.pop(best), sep='\t\t')
