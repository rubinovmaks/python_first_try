digit = input('Type digit: ')

while len(digit) > 1:
    tmp = 1
    for i in digit:
        tmp = tmp * int(i)
    digit = str(tmp)
print(digit)