#!/usr/bin/python3
def add_integer(a, b=98):
    if not(isinstance(a, (float, int))):
        raise("a must be an integer")
    if not(isinstance(b, (float, int))):
        raise("b must be an integer")
    return (int(a) + int(b))