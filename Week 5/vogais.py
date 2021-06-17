"""

Created on Mon May 24 14:45:49 2021 - BH, Brazil

@author: Davidson Prata

"""


def vogal(vogal):

    if isinstance(vogal, str):
        vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        return vogal in vogais

    return False
