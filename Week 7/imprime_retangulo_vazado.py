"""

Created on Wed Jun  2 12:04:08 2021 - BH, Brazil

@author: Davidson Prata

"""


largura = int(input("Digite a largura: "))

altura = int(input("Digite a altura: "))

caractere = "#"


def r(largura, altura, caractere):

    linha_cheia = caractere * largura
    if largura > 2:
        linha_vazia = caractere + (" " * (largura - 2)) + caractere
    else:
        linha_vazia = linha_cheia

    if altura >= 1:
        print(linha_cheia)
    for i in range(altura - 2):
        print(linha_vazia)
    if altura >= 2:
        print(linha_cheia)


r(largura, altura, caractere)
