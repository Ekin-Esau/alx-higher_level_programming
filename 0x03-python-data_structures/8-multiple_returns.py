#!/usr/bin/python3
def multiple_returns(sentense):
    lenght = len(sentence)
    first_char = sentence[0]
    if len(sentence) == 0:
        return None
    return lenght, first_char
