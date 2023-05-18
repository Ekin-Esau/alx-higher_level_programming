#!/usr/bin/python3
def best_score(a_dictionary):
    highest_score = max(a_dictionary, key=a_dictionary.get)
    return highest_score
