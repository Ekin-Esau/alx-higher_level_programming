#!/usr/bin/python3
def rearch_replace(my_list, search, replace):
    if len(my_list) == 0:
        return my_list
    for i in my_list:
        i.replace(search, replace)
    return my_list

