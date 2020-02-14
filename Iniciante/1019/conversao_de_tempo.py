# -*- coding: utf-8 -*-
n = int(input())

h = n // 60 ** 2
n = n - h * 60 ** 2
min = n // 60
n = n - min * 60
seg = n

print('{}:{}:{}'.format(h, min, seg))
