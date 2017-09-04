
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

import functools 

# def my_func():
# 	"""This doc description"""
# 	age = 34
# 	print('My age: ' + str(age))

# # print(my_func.__doc__)

# help(my_func)





def my_decorator(f):
	@functools.wraps(f)
	def wrapper(*args, **kwds):
		print(f.__name__, args, kwds)
		return f(*args, **kwds)
	return wrapper

@my_decorator
def example(x):
	"""Docstring"""
	print('Called example function and param: ', x)

example(42)









