# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# [1, 1, 1, 1] == [1, 1, 1]
# [6, 3, 7] == [6, 7 ,3]

import random


lst1 = [random.randint(1, 200) for i in range(random.randint(3, 10))]
print(lst1)
lst = [lst1[0], lst1[2], lst1[-2]]
print(lst)