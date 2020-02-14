# -*- coding: utf-8 -*-
time = int(input())
speed = int(input())

distance = speed * time
liters = distance / 12

print('{:.3f}'.format(liters))
