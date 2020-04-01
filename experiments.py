from math import *

x = 'a'
# print(ascii(x))
# print(f'x: {x:.3f}')
# print(f'ascii(x): {x!a}')
# print(locals().get('sqrt')(49))
# print(__builtins__)

def print_char_count(input_string):
    for i in range(65,124):
        count=0
        for ch in (input_string):
            if chr(i) == ch:
                count = count +1
        print(chr(i),count)
print(print_char_count("bilal"))
