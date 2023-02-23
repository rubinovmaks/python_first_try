import string
ascii_letters = string.ascii_letters


text = input('Type text: ')
begin = ascii_letters.index(text[0])
end = ascii_letters.index(text[-1])
print(ascii_letters[begin:end+1])
