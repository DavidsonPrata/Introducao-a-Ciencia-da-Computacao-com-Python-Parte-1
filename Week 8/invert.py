"""

Created on Wed Jun  9 16:36:59 2021 - BH, Brazil

@author: Davidson Prata

"""

lista = []
x = 1
while x != 0:
    lista.append(int(input('Digite um numero inteiro: ')))
    if lista[-1] == 0:
        x = 0
tamanho = len(lista) - 2

for i in range(tamanho, -1, -1):
    print(lista[i])
