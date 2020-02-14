# -*- coding: utf-8 -*-
valor = int(input())

n = valor

cem = n // 100
n = n - cem * 100
cin = n // 50
n = n - cin * 50
vin = n // 20
n = n - vin * 20
dez = n // 10
n = n - dez * 10
cinc = n // 5
n = n - cin * 5
dois = n // 2
n = n - dois * 2
um = n // 1

print(valor)
print('{} nota(s) de R$ 100,00'.format(cem))
print('{} nota(s) de R$ 50,00'.format(cin))
print('{} nota(s) de R$ 20,00'.format(vin))
print('{} nota(s) de R$ 10,00'.format(dez))
print('{} nota(s) de R$ 5,00'.format(cinc))
print('{} nota(s) de R$ 2,00'.format(dois))
print('{} nota(s) de R$ 1,00'.format(um))
