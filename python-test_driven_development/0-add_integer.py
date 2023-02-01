#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        return (int(a) + int(b))
    except Exception:
        if (not isinstance(a, (float, int))):
            raise TypeError("a must be an integer")
        if (not isinstance(b, (float, int))):
            raise TypeError("b must be an integer")
