"""

Created on Wed May 19 14:24:35 2021 - BH, Brazil

@author: Davidson Prata

"""


# n = Número #

# f = Fatorial #

# nAtual = Número Atual #

def main():
    n = int(input("Digite o valor de n: "))
    f = 1
    nAtual = 1

    while nAtual <= n:
        f = f * nAtual
        nAtual = nAtual + 1

    print(f)


main()
