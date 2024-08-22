#!/usr/bin/python3

"""
method that determines if a given data set represents
a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    method definition
    """
    value = 0
    while value < len(data):
        byte = data[value]
        if byte < 0b10000000:
            value += 1
        elif byte < 0b11000000:
            return False
        elif byte < 0b11100000:
            if (value + 1 >= len(data) or
            data[value + 1] < 0b10000000 or
            data[value + 1] >= 0b11000000):
                return False
            value += 2
        elif byte < 0b11110000:
            if (value + 2 >= len(data) or
            data[value + 1] < 0b10000000 or
            data[value + 1] >= 0b11000000 or
            data[value + 2] < 0b10000000 or
            data[value + 2] >= 0b11000000):
                return False
            value += 2
        else:
            return False
        value += 1
    return True
