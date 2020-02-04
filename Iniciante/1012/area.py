# -*- coding: utf-8 -*-
A, B, C = input().split(' ')

A = float(A)
B = float(B)
C = float(C)
pi = 3.14159

triangle = (A * C) / 2
circle = pi * (C ** 2)
trapezium = ((A + B) * C) / 2
square = B * B
rectangle = A * B

print('''TRIANGULO: {:.3f}
CIRCULO: {:.3f}
TRAPEZIO: {:.3f}
QUADRADO: {:.3f}
RETANGULO: {:.3f}'''.format(triangle, circle, trapezium, square, rectangle))
