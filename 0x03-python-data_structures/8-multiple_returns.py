#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    first_char = sentence[0]
    if len(sentence) == 0:
        first_char = None
    print("Lenght: {:d} - First character: {}".format(lenght, first_char))
    return lenght, first_char
