"""

Created on Tue Jun  1 16:04:46 2021 - BH, Brazil

@author: Davidson Prata

"""


largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

linha = 0
coluna = 0

while linha < altura:
    while coluna < largura:
        print("#", end="")
        coluna = coluna + 1
    print()
    linha = linha + 1
    coluna = 0
