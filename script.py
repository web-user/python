#!/usr/bin/env python3

# def many(dolor, dolor1):
# 	return dolor + dolor1

# inc = [10, 20, 30]
# inc1 = [100, 200, 300]

# new_inc = list(map(many, inc, inc1))

# print(new_inc)

# def test(post=[]):
# 	return sum(post)

# text = [2, 1, 3]

# print(test(text))



# def world_text(debit):
# 	"""  it'is function  """
# 	return debit + 2

# items = [5, 2, 4]
# print(list(map(world_text, items)))

# a = []

# for i in range(7):
# 	if i % 2 != 0:
# 		a.append(i)
# 		print(a)

# print(a.clear())
# b = a
# print(b)

# age = 26
# name = 'Jems'

# print('Age {} -- {} years.'.format(name, age))

# def function_filter(number_r):
# 	"""
# 	Exeple description function
# 	"""
# 	return list(filter(lambda x: x < 0, number_r ))


# number = range(-5, 5)

# print(function_filter.__doc__)


# def tottal(initial=5, *numbers, **keywords):
# 	"""
# 	This function use many parameter
# 	"""
# 	count = initial
# 	for number in numbers:
# 		count += number
# 	for key in keywords:
# 		count += keywords[key]
# 	return count

# print(tottal(10, 1, 2, vegetabl=50, fruits=10))

# sortList = ['a', 'cc', 'bbb']

# print(sortList)

# print(sorted(sortList, reverse=True))

# Class and Object

# class monitor:
# 	price = 0
# 	weight = 0
# 	produced_by = ''
# 	resolution = ''
# 	model = ''

# LG = monitor()

# print(LG)

# BACKUP
# import os
# import time

# source = ['./doc', './code']

# target_dir = '/home/user/lesson/python/backup'

# target = target_dir + os.sep + time.strftime('%Y-%m-%d-%H-%M-%S') + '.zip'

# zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# if os.system(zip_command) == 0:
# 	print('Backup create in', target)
# else:
# 	print('Backup ERROR!')

# class Shop:
# 	int_feild = 8
# 	str_feild = 'string test'

# print(Shop.int_feild)

# obj_shop = Shop()
# obj_shop2 = Shop()

# print(obj_shop.str_feild)
# Shop.int_feild = 12

# # obj_shop.int_feild = 17

# print(obj_shop.int_feild)
# print(obj_shop2.int_feild)

"""   
является универсальной функцией для создания списков (list) содержащих арифметическую прогрессию
range() может принимать от одного до трех агрументов, при этом аргументами должны быть целые числа (int)
range(старт, стоп, шаг)

Функция xrange() в Python очень похожа на функцию range() за тем лишь исключением, что вместо списка создает объект xrange

алгоритм сложения чисел от 1 до 7
a = sum(range(8)) сложить все 

"""
# my_list = list(range(5))
# print(my_list)


"""
Map applies a function to all the items in an list 
"""
# items_list  = [2, 3, 6]

# squeret = list( map( lambda x: x **2, items_list ) )

