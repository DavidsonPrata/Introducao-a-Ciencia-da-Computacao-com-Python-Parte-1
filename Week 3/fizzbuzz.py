# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:47:48 2021

@author: Davidson Prata
"""

n = int(input("Digite aqui um número inteiro:"))

x = n % 3
y = n % 5

if x and y == 0:
    print("FizzBuzz")
else:
    print(n)
