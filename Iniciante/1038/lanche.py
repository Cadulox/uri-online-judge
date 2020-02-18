# -*- coding: utf-8 -*-
X, Y = input().split(' ')

X = int(X)
Y = int(Y)

if X == 1:
    total = Y * 4
elif X == 2:
    total = Y * 4.5
elif X == 3:
    total = Y * 5
elif X == 4:
    total = Y * 2
else:
    total = Y * 1.5

print('Total: R$ {:.2f}'.format(total))
