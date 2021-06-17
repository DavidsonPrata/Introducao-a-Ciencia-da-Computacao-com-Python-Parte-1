"""

Created on Mon May 24 14:22:00 2021 - BH, Brazil

@author: Davidson Prata

"""


def numero_primo(n):

    x = 0

    for divisor in range(1, n + 1):
        if n % divisor == 0:
            x = x + 1
            if x > 2:
                return False

    return True


def maior_primo(n):
    if n < 2:
        return 0

    for numero_primo_2 in range(n, 2, -1):
        if numero_primo(numero_primo_2):
            return numero_primo_2
