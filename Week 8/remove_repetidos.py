"""

Created on Wed Jun  9 13:24:29 2021 - BH, Brazil

@author: Davidson Prata

"""


def remove_repetidos(lista):
    x = []
    for y in lista:
        if y not in x:
            x.append(y)
    x.sort()
    return x


lista = [2, 4, 2, 2, 3, 3, 1]

lista = remove_repetidos(lista)
print(lista)
