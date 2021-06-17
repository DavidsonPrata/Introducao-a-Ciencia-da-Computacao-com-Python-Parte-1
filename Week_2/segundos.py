# -*- coding: utf-8 -*-
"""
Created on Tue May 11 11:37:56 2021

@author: Davidson Prata
"""

s = int(input("Por favor, entre com o número de segundos que deseja converter:"))

a = s // 86400
s_res = s % 86400
b = s_res // 3600
s_res_2 = s_res % 3600
c = s_res_2 // 60
d = s_res_2 % 60

print(a, "dias,", b, "horas,", c, "minutos e", d, "segundos.")
