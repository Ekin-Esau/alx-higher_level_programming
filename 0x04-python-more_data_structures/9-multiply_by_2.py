#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    list_values = list(new_dictionary.keys())
    for i in list_values:
        new_dictionary[i] *= 2
    return new_dictionary
