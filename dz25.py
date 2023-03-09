from typing import Callable
def pow(x: int) -> int:
    return x ** 2

def some_gen(begin: int, end: int, func: Callable) -> int:

    for i in range(end):
        yield begin
        begin = func(begin)

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True
assert list(gen) == [2, 4, 16, 256]
print('OK')