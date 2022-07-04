#!/usr/bin/python3
def fizzbuzz():
    for c in range(1, 101):
        if c % 3 == 0 and c % 5 != 0:
            print("{}".format("Fizz"), end=" ")
        elif c % 3 != 0 and c % 5 == 0:
            print("{}".format("Buzz"), end=" ")
        elif c % 3 == 0 and c % 5 == 0:
            print("{}".format("FizzBuzz"), end=" ")
        else:
            print("{}".format(c), end=" ")
