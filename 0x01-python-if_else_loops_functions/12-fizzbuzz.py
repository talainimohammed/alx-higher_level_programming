#!/usr/bin/python3
def fizzbuzz():
    x=''
    for nb in range(1, 101):
        if nb % 3 == 0 and nb % 5 == 0:
            x += "FizzBuzz "
        elif nb % 3 == 0:
            x += "Fizz "
        elif nb % 5 == 0:
            x += "Buzz "
        else:
            x += "{} ".format(nb)
    print(x, end='')
fizzbuzz()
