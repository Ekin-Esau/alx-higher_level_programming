#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return length, first_char
