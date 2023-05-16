#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    message_1 = "{} is divisible by 2"
    message_2 = "{} is not divisible by 2"
    for i in my_list:
        if i % 2 == 0:
            return message_1
        else:
            return message_2
