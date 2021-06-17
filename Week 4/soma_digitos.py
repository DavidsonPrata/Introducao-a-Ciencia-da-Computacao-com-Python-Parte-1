"""

Created on Thu May 20 14:15:57 2021 - BH, Brazil

@author: Davidson Prata

"""

# n = É o número inteiro de entrada pelo usuário #

# s = É a soma do resultado final e é definida como 0 #

# r = É o resto de n #


n = int(input("Numero: "))

s = 0

while (n != 0):
    r = n % 10
    n = (n - r)//10
    s = s + r

print(s)
