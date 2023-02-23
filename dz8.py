lst = [0, 1, 2, 3, 4, 7]
# lst = [6]
#lst = []
res = 0
if lst:
    res = sum(lst[::2]) * lst[-1]
print(res)