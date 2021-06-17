"""

Created on Thu May 20 17:30:38 2021 - BH, Brazil

@author: Davidson Prata

"""

n = int(input("Digite um número: "))

n1 = n

resto1 = n % 10

while n // 10 != 0:

    n = n // 10

    resto = n % 10

    if resto == resto1:
        print("sim")

        n = n1

        break

    resto1 = resto

if n // 10 == 0:
    print("não")
