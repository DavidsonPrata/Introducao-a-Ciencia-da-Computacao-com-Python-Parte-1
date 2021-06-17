"""

Created on Thu Jun 17 08:18:37 2021 - BH, Brazil

@author: Davidson Prata

"""


def NumeroEPrimo(n):
    numeroDivisores = 0

    for divisor in range(1, n + 1):
        if n % divisor == 0:
            numeroDivisores += 1

            if numeroDivisores > 2:
                return False
    return True


def ContarPrimos(nInicial, nFinal):
    quantidadeNumerosPrimos = 0

    for numeroCorrente in range(nInicial, nFinal + 1):
        if NumeroEPrimo(numeroCorrente):
            quantidadeNumerosPrimos += 1
    return quantidadeNumerosPrimos


def n_primos(n):
    return ContarPrimos(2, n)
