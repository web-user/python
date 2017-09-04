#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Нужно пройтись по основным встроенным метода(map, range/xrange, filter, lambda, functools.wrap, functools.partial),
 ооп в питоне(super, порядок наследования), менеджер контекста, декораторы, генераторы. смотреть на версии питона 2.7 и 3.5/6 
 сейчас наиболее ходовые. по джанго разобратся с middleware, наследование моделей, generic views, формы.
Почитать ещё по основам, сесия/куки, что где хранится и как находит связь одно с другим

'''


# word_letter = "word"
# text_new = '*' * len(word_letter)
# print(text_new)

# while "*" in text_new:
# 	user = input("Enter letter:")
# 	dop = ""
# 	for number in range(len(word_letter)):
# 		if user == word_letter[number]:
# 			dop = dop + user
# 		else:
# 			dop = dop + text_new[number]
# 	text_new = dop
# 	print(text_new)

'''
String Method
str()
len()
upper()
lower()

Method that use dot notation 
only work with string upper(), lower()


'''

# number  = 'My text'

# print(len(number))

# from datetime import datetime
# now = datetime.now()

# print('%s:%s:%s' % (now.hour, now.minute, now.second))


# print(1**2 <= -1)



# if not 10 - (5 * 2) == 10:
# 	print('True: yes!')
# else:
# 	print('False: yes!')

'''
This and That (or This, But Not That!)


Set bool_one equal to the result of
	False or not True and True
Set bool_two equal to the result of
	False and not True or True
Set bool_three equal to the result of
	True and not (False or False)
Set bool_four equal to the result of
	not not True or False and not True
Set bool_five equal to the result of
	False or not (True and True)

'''
# bool_one = False

# bool_two = True

# bool_three = True

# bool_four = True

# bool_five = False


pyg = 'ay'


original = raw_input('Enter a word: ')


if len(original) > 0 and original.isalpha():
	word = original.lower()
	first = word[0]
	print(word + first + pyg)
else:
	print('empty')























# import functools 

# def my_func():
# 	"""This doc description"""
# 	age = 34
# 	print('My age: ' + str(age))

# # print(my_func.__doc__)

# help(my_func)





# def my_decorator(f):
# 	@functools.wraps(f)
# 	def wrapper(*args, **kwds):
# 		print(f.__name__, args, kwds)
# 		return f(*args, **kwds)
# 	return wrapper

# @my_decorator
# def example(x):
# 	"""Docstring"""
# 	print('Called example function and param: ', x)

# example(42)









