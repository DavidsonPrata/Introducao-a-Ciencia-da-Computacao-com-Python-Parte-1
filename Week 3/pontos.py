# -*- coding: utf-8 -*-
"""
Created on Mon May 17 10:12:54 2021

@author: Davidson Prata
"""
import math

x1 = float(input('Entre com o valor de X1:'))
x2 = float(input('Entre com o valor de X2:'))
y1 = float(input('Entre com o valor de Y1:'))
y2 = float(input('Entre com o valor de Y2:'))

d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if d >= 10:
    print("longe")
else:
    print("perto")
