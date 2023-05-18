#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    highest_score = max(a_dictionary, key=a_dictionary.get)
    return highest_score
