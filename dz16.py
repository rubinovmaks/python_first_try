# say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"

def say_hi(name: str, age: int) -> str:
    res = f"Hi. My name is {name} and I'm {age} years old"
    return res

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
print('OK')