#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        c = -number % 10
        return c
    else:
        c = number % 10
        return c
    print("{}".format(c))
    print('\n', end='')

