#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if type(number) == int:
    nb = int(repr(number)[-1])
    if number < 0:
        nb = int("-" + str(nb))
    x = "Last digit of "
    y = " and is less than 6 and not 0"
    if nb > 5:
        print(x + str(number) + " is " + str(nb) + " and is greater than 5")
    elif nb < 6 and nb != 0:
        print(x + str(number) + " is " + str(nb) + y)
    else:
        print(x + str(number) + " is " + str(nb) + " and is 0")
else:
    print("TypeError")
