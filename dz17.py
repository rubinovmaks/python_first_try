

def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]
    if text[-1] != '.':
        text += '.'
    return text

assert correct_sentence("greetings, friends.") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("hello") == "Hello."
assert correct_sentence("greetings, friends.") == "Greetings, friends."
print('OK')
