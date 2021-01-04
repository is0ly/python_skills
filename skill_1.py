#!/usr/bin/env python3

x, y, z = 100, 150, 10.5

print(type(x))
print(isinstance(y, float))
print(id(z))

print(True and True)
print(True and False)
print(True or False)
print(False or True)

print(True == True)
print(True != True)
print(5 > 3 == 5 < 10)


my_list = []

my_list.append([9,44,7,16])
my_list.extend([2,56,105,88,1])
my_list[0].sort()
my_list = my_list[0] + my_list[1:]
my_list.sort()
print(my_list)
my_list[0] = my_list[:4]
my_list[1] = my_list[4:]
new_list = my_list[:2]
print(my_list)
print(new_list)