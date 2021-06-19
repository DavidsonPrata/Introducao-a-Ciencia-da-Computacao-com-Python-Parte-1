"""

Created on Wed Jun  9 15:29:05 2021 - BH, Brazil

@author: Davidson Prata

"""


def maior_elemento(n):
    m = 0
    for x in n:
        if x > m or m == 0:
            m = x
    return m


print(maior_elemento([-12, -27, -90]))
