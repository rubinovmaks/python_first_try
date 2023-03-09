def is_even(digit: int) -> bool:
    return digit % 2 == 0
assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True
print('OK')