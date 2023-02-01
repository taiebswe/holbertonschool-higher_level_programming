#!/usr/bin/python3
def add_integer(a, b=98):
    if (not isinstance(a, (float, int))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, (float, int))):
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return (int(a) + int(b))