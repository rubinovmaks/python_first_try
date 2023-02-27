from typing import List, Union

def find_unique_value(lst: List) -> Union[int, float, None]:
    for i in lst:
        if lst.count(i) == 1:
            return i

assert find_unique_value([1, 2, 1, 1]) == 2
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5
print("ОК")