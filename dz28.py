def is_prime(number: int) -> bool:
    i = 2
    while i < number // 2 + 1:
        if number % i == 0:
            return False
        i = i +1
    return  True



def prime_generator(border: int) -> int:
    tmp = 2
    yield tmp
    while tmp < border:
        tmp += 1
        if is_prime(tmp):
            yield tmp

from inspect import isgenerator

gen = prime_generator(1)

assert isgenerator(gen) == True, 'Test0'
print(list(prime_generator(10)))
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(30)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')