
def add_one(lst: list) -> list:
    tmp = ''
    for i in lst:
        tmp += str(i)
    tmp = str(int(tmp) + 1)
    res = []
    for i in tmp:
        res.append(int(i))
    return res


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5]
assert add_one([9, 9, 9, 9]) == [1, 0, 0, 0, 0]
assert add_one([0]) == [1]
assert add_one([9]) == [1, 0]
print("ОК")