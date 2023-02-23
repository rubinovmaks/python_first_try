

def common_elements() -> set:
    lst = [i for i in range(3, 99, 3)]
    lst2 = [i for i in range(5, 99) if i % 5 == 0]
    print(lst)
    print(lst2)
    res = set(lst).intersection(set(lst2))
    return res

print(common_elements())