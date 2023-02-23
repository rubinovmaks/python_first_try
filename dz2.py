digit = int(input('Type digit: '))
a, digit = divmod(digit, 1000)
b, digit = divmod(digit, 100)
c, d = divmod(digit, 10)

print(a)
print(b)
print(c)
print(d)
