#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in my_list:
        if i % 2 == 0:
            print("{} is divisible by 2".format(i))
        else:
            print("{} is not divisible by 2".format(i))
