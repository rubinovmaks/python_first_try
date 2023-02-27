import string


def is_palindrome(some_str: str) -> bool:
    text = some_str.lower().replace(' ', '')
    for i in string.punctuation:
        text = text.replace(i, '')
    return text == text[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True
assert is_palindrome('0P') == False
assert is_palindrome('a.') == True
print("ОК")