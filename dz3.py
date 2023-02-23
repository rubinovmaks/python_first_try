digit = int(input('Type 5-digits: '))
f, digit = divmod(digit, 10000)
a, digit = divmod(digit, 1000)
b, digit = divmod(digit, 100)
c, d = divmod(digit, 10)
digit = d*10000 + c*1000 + b*100 + a*10 + f
print(digit)