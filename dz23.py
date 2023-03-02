# def popular_words (text, words):
#    pass

# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }


from typing import Dict, List

def popular_worlds(text: str, words: List) -> Dict:
    text = text.lower().split()
    dct = {}
    for word in words
        dct[word] = text.count(word)
    return dct

text = '''When I was One I had just begun When I was Two I was nearly new '''


print('OK')