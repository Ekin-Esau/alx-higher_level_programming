#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set()
    for i, j in set_1, set_2:
        if i in set_1 and i not in set_2:
            set_3.add(i)
        if j in set_2 and j not in set_1:
            set_3.add(j)
    return set_3
