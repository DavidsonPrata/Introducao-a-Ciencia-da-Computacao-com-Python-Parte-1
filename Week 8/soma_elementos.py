"""

Created on Wed Jun  9 14:27:08 2021 - BH, Brazil

@author: Davidson Prata

"""


def soma_elementos(numeros):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma


print(soma_elementos([1, 3, 5, 7, 9]))
