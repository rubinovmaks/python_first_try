

from typing import Union

def second_index(text: str, symbol: str) -> Union[int, None]:
    if text.count(symbol) < 2:
        return None
    return text.find(symbol, text.find(symbol) + 1)

assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", "h") is None
print("OK")