import keyword
import string

name = input('Type name: ')
punkt = string.punctuation.replace('_', '') + ' '
res = True
if name[0].isdigit():
    res = False
if name in keyword.kwlist:
    res = False
for i in punkt:
    if i in name:
        res = False
        break
if name != '_':
    if not name.islower():
        res = False

print(res)