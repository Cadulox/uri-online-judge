# -*- coding: utf-8 -*-
numbers = input().split()
list1 = list()
for item in numbers:
    list1.append(int(item))
list2 = sorted(list1)
list3 = sorted(list1, reverse=True)

if list1 == list2:
    print('C')
elif list1 == list3:
    print('D')
else:
    print('N')
