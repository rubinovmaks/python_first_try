lst = [0, 1, 0, 3, -12]
# lst = []
nulls = []
digits = []
for d in lst:
    if d:
        digits.append(d)
    else:
        nulls.append(d)
digits.extend(nulls)
print(digits)