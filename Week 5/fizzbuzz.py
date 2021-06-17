"""

Created on Mon May 24 15:19:10 2021 - BH, Brazil

@author: Davidson Prata

"""


def x(n, div = 3):
    return True if n % div == 0 else False


def fizzbuzz(n):
    if x(n) and x(n, 5):
        return 'FizzBuzz'
    elif x(n) and not x(n, 5):
        return 'Fizz'
    elif not x(n) and x(n, 5):
        return 'Buzz'
    else:
        return n
