#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))          # Sortie attendue: 3
print(add_integer(100, -2))       # Sortie attendue: 98
print(add_integer(2))             # Sortie attendue: 100
print(add_integer(100.3, -2))     # Sortie attendue: 98
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)                       # Sortie attendue: b must be an integer
try:
    print(add_integer(None))
except Exception as e:
    print(e)                       # Sortie attendue: a must be an integer
