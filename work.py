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

"""
FUNCTION

"""

# def total(initial=5, *numbers, **keywords):
# 	count = initial
# 	for number in numbers:
# 		count += number
# 	for key in keywords:
# 		count += keywords[key]
# 	return count

# print(total(10, 1, 2, 3, vegetables=50, fruits=100))


# if not 10 - (5 * 2) == 10:
# 	print('True: yes!')
# else:
# 	print('False: yes!')

'''
This and That (or This, But Not That!)

there's an order of operations for boolean operators:

not is evaluated first;
and is evaluated next;
or is evaluated last.
For example, True or not False and False returns True. If this isn't clear, look at the Hint.


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


# pyg = 'ay'


# original = input('Enter a word: ')


# if len(original) > 0 and original.isalpha():
# 	word = original.lower()
# 	first = word[0]
# 	new_word = ' '.join([word, first, pyg])
# 	print(new_word)
# 	print(new_word[1:len(new_word)])
# else:
# 	print('empty')










# def hotel_cost(nights):
# 	return 140 * nights

# def plane_ride_cost(city):
# 	if city == "Charlotte":
# 		return 183
# 	elif city == "Tampa":
# 		return 220
# 	elif city == "Pittsburgh":
# 		return 222
# 	elif city == "Los Angeles":
# 		return 475

# def rental_car_cost(days):
# 	total = 40 * days
# 	if days >= 7:
# 		return total - 50
# 	elif days >= 3:
# 		return total - 20
# 	else:
# 		return total
  
  
# def trip_cost(city, days):
# 	sum = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)
# 	return sum



# print trip_cost('Los Angeles', 10)

"""
datatypes LIST
"""

# x = [1, 2, 3]
# x.append([4, 5])
# print (x)
# gives you: [1, 2, 3, [4, 5]]


"""
extend: Extends list by appending elements from the iterable.

"""

# x = [1, 2, 3]
# x.extend([4, 5])
# print (x)
# gives you: [1, 2, 3, 4, 5]


# suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
# first = suitcase[0:2]

# Third and fourth items (index two and three)
# print(suitcase[2:4])

# The last two items (index four and five)
# print(suitcase[4:6])

# animals = ["ant", "bat", "cat"]

# animals.insert(1, "dog")
# print animals




# start_list = [5, 3, 1, 2, 4]
# square_list = []

# # Your code here!
# for number in start_list:
# 	square_list.append(number ** 2) 
# square_list.sort()


# print square_list

# Your code here!
# del zoo_animals['Sloth'] 
# del zoo_animals['Bengal Tiger'] 
# zoo_animals['Rockhopper Penguin'] = 'My text'

# beatles = ["john","paul","george","ringo","stuart"]
# beatles.remove("stuart")




# inventory = {
#   'gold' : 500,
#   'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
#   'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
# }

# # Adding a key 'burlap bag' and assigning a list to it
# inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# # Sorting the list found under the key 'pouch'
# inventory['pouch'].sort() 

# # Your code here
# inventory['pocket'] = ['seashell', 'strange berry', 'lint']
# inventory['pocket'].sort()
# inventory['backpack'].remove('dagger')

# print(inventory)






# my_d = {
# 	'Word': 1,
# 	'Applay': [34, 12, 'MD'],
# 	'week': 45
# }

# def count_total(dic):
# 	total = 0

# 	for item in dic:
# 		if type(dic[item]) == int :
# 			total = total + 1
# 	return total

# print(count_total(my_d))


# Write your function below!
# def fizz_count(x):
#   count = 0
#   for item in x:
#     if item == "fizz":
#       count += 1
#   return count

# print(fizz_count(["fizz","cat","fizz"]))

# import functools 

# def my_func():
# 	"""This doc description"""
# 	age = 34
# 	print('My age: ' + str(age))

# # print(my_func.__doc__)

# help(my_func)

"""
STORE
"""
# prices = {
# 	"banana": 4,
# 	"apple": 2,
# 	"orange": 1.5,
# 	"pear": 3
# }

# stock = {
# 	"banana": 6,
# 	"apple": 0,
# 	"orange": 32,
# 	"pear": 15
# }

# total = 0

# for item in prices:
# 	print(item)
# 	print("price: %s" % prices[item])
# 	print("stock: %s" % stock[item])
# 	total += (prices[item] * stock[item])

# print(total)



# shopping_list = ["banana", "orange", "apple"]

# stock = {
# 	"banana": 6,
# 	"apple": 0,
# 	"orange": 32,
# 	"pear": 15
# }
    
# prices = {
# 	"banana": 4,
# 	"apple": 2,
# 	"orange": 1.5,
# 	"pear": 3
# }


# Write your code below!
# def compute_bill(food):
#   total = 0
#   for item in food:
#     if stock[item] > 0:
#       total += prices[item]
#       stock[item] -= 1
#   return total

# print(compute_bill(shopping_list))




# lloyd = {
#   "name": "Lloyd",
#   "homework": [90.0, 97.0, 75.0, 92.0],
#   "quizzes": [88.0, 40.0, 94.0],
#   "tests": [75.0, 90.0]
# }
# alice = {
# 	"name": "Alice",
# 	"homework": [100.0, 92.0, 98.0, 100.0],
# 	"quizzes": [82.0, 83.0, 91.0],
# 	"tests": [89.0, 97.0]
# }
# tyler = {
# 	"name": "Tyler",
# 	"homework": [0.0, 87.0, 75.0, 22.0],
# 	"quizzes": [0.0, 75.0, 78.0],
# 	"tests": [100.0, 100.0]
# }

# students = [lloyd, alice, tyler]

# for item in students:
# 	print(item['name'])
# 	print(item['homework'])
















# import functools


# def my_decorator(f):
# 	@functools.wraps(f)
# 	# function wrapper 
# 	def wrapper(*args, **kwds):
# 		print(f.__name__, args, kwds)
# 		return f(*args, **kwds)
# 	return wrapper

# @my_decorator
# def example(x):
# 	"""Docstring"""
# 	print('Called example function and param: ', x)

# example(42)






# lloyd = {
# 	"name": "Lloyd",
# 	"homework": [90.0, 97.0, 75.0, 92.0],
# 	"quizzes": [88.0, 40.0, 94.0],
# 	"tests": [75.0, 90.0]
# }
# alice = {
# 	"name": "Alice",
# 	"homework": [100.0, 92.0, 98.0, 100.0],
# 	"quizzes": [82.0, 83.0, 91.0],
# 	"tests": [89.0, 97.0]
# }
# tyler = {
# 	"name": "Tyler",
# 	"homework": [0.0, 87.0, 75.0, 22.0],
# 	"quizzes": [0.0, 75.0, 78.0],
# 	"tests": [100.0, 100.0]
# }

# # Add your function below!
# def average(numbers):
# 	total = sum(numbers)
# 	return float(total) / len(numbers)

# def get_average(student):
# 	homework = 0.1 * average(student['homework'])
# 	quizzes = 0.3 * average(student['quizzes'])
# 	tests = 0.6 * average(student['tests'])
# 	return homework + quizzes + tests

# def get_letter_grade(score):
# 	if score >= 90:
# 		return 'A'
# 	elif score >= 80:
# 		return 'B'
# 	elif score >= 70:
# 		return 'C'
# 	elif score >= 60:
# 		return 'D'
# 	else:
# 		return 'F'

# # print(get_letter_grade(lloyd))

# student = [lloyd, alice, tyler]
  	
# def get_class_average(class_list):
# 	results = []
# 	for item in class_list:
# 		results.append(get_average(item))
# 	return average(results)

# print(get_class_average(student))
# print(get_letter_grade(get_class_average(student)))

# print(get_letter_grade(get_average(lloyd)))
# print(get_letter_grade(get_average(alice)))
# print(get_letter_grade(get_average(tyler)))


# n = [3, 5, 7]

# def double_list(x):
# 	for i in range(0, len(x)):
# 		x[i] = x[i] * 2
# 	return x

# # Don't forget to return your new list!

# print(double_list(n))

# nx = list(map(lambda x : x * 2, n))

# print(nx)

# print(list(range(0, 3)))

# n = ["Michael", "Lieberman"]
# # Add your function here
# def join_strings(words):
# 	result = ""
# 	for item in words:
# 		result += item
# 	return result


# print(join_strings(n))





# n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# # Add your function here
# def flatten(lists):
# 	results = []
# 	for numbers in lists:
# 		for number in numbers:
# 			results.append(number)

# 	return results



# print(flatten(n))

# from random import randint 

# board = []

# for x in range(0, 5):
# 	board.append(["O"] * 5)

# def print_board(board):
# 	for row in board:
# 		print(" ".join(row))

# # Add your code below!
# def random_row(board_in):
# 	random_row = randint(0, len(board_in) - 1)
# 	return random_row
  
# def random_col(board_in):
# 	random_col = randint(0, len(board_in) - 1)
# 	return random_col

# print(random_row(board))

# print(random_col(board))



# ship_row = random_row(board)
# ship_col = random_col(board)
# print(ship_row)
# print(ship_col)

# guess_row = int(raw_input("Guess Row: "))
# guess_col = int(raw_input("Guess Col: "))

# # Write your code below!
# # Write your code below!
# if guess_row == ship_row and guess_col == ship_col:
# 	print("Congratulations! You sank my battleship!")
# elif guess_row not in range(5) or guess_col not in range(5):
# 	print("Oops, that's not even in the ocean.")
# elif board[guess_row][guess_col] == "X":
# 	print("You guessed that one already.")
# else:
# 	print("You missed my battleship!")
# 	board[guess_row][guess_col] = "X"
  

  
# print_board(board)


# class Counter:
# 	""" I COUNT"""
# 	def __init__(self, initial=0): #constract, initilization object
# 		self.value = initial #write atribute
# 	def increment(self):
# 		self.value += 1
# 	def get(self):
# 		return self.value


# c = Counter(42)
# print(c.increment())
# print(c.get())



# class MemorizingDict(dict):
# 	""" I doc text """
# 	pass

# d = MemorizingDict

# MemorizingDict.number = 56

# print(MemorizingDict.__doc__)

# print(sorted(vars(d)))

# del d.__dict__

# print(sorted(vars(d)))

# class myCounter:
# 	"""This doc Parent One"""
# 	def __init__(self, doc = __doc__):
# 		self.doc = myCounter.__doc__

# class Counter:
# 	"""This doc Parent"""
# 	all_caounter = []

# 	def __init__(self, initial = 0, doc = __doc__):
# 		self.__class__.all_caounter.append(self)
# 		self.value = initial
# 		self.doc = Counter.__doc__


# class OtherCounter(Counter, myCounter):
# 	"""This doc chaild"""
# 	def __init__(self, initial = 0,):
# 		self.initial = initial
# 		super().__init__(initial, doc = __doc__) # get constract parent all args
# 	def getDoc(self):
# 		return ' '.join([self.doc, __class__.__doc__])


# oc = OtherCounter()

# print(vars(oc))

# print(oc.__doc__)
# print(oc.doc)
# print(oc.getDoc())


# class A(object):
# 	"""asdfasdfasdf"""
# 	all_caounter = []

# 	def __init__(self, initial = 0):
# 		self.__class__.all_caounter.append(self)
# 		self.value = initial

# class B(object):
# 	"""asdfasdfasdfasdfasf"""
# 	all_caounter = []

# 	def __init__(self, initial = 0):
# 		self.__class__.all_caounter.append(self)
# 		self.value = initial

# class C(B, A):
# 	def __init__(self, initial = 0):
# 		self.initial = initial
# 		super().__init__(initial)
# 	def getDoc(self):
# 		for c in __class__.__bases__:
# 			print( ': '.join([c.__name__, c.__doc__]))


# c = C()

# print(C.__bases__)

# print(vars(c))

# c.getDoc()

"""
check instance of a class 
"""

# class At:
# 	def f(self):
# 		print("A.f")

# class Bt(At):
# 	def f(self):
# 		super(Bt, self).f()


# class Ct(Bt):
# 	def f(self):
# 		super(Ct, self)

# v = Ct()
# v.f()

# Ct.f()

# print(Ct.mro())

# print(isinstance(Bt(), At))

"""
Декораторы класса 
"""
# def thread_safe(cls):
# 	orig_increment = cls.increment
# 	orig_get = cls.get

# 	def increment(self):
# 		with self.get_lock():
# 			return orig_increment(self)
# 	def get(self):
# 		with self.get_lock():
# 			return orig_get(self)

# 	cls.get_lock = []
# 	cls.get = get 
# 	return cls

# import functools

# def singleton(cls):
# 	instance = None

# 	@functools.wraps(cls)
# 	def inner(*args, **kwards):
# 		nonlocal instance
# 		if instance is None:
# 			instance = cls(*args, **kwards)
# 		return instance
# 	return inner

# @singleton
# class Noop:
# 	"I do nothing"


# print(id(Noop()))

# import warnings 
# import functools

# def deprecated(cls):
# 	orig_init = cls.__init__

# 	@functools.wraps(cls.__init__)
# 	def new_init(self, *args, **kwargs):
# 		warnings.warn(cls.__name__ + " is deprecated.", category = DeprecationWarning)
# 		orig_init(self, *args, **kwargs)
# 	cls.__init__ = new_init
# 	return cls

# @deprecated
# class Counter:
# 	def __init__(self, initial = 0):
# 		self.value = initial

# cv = Counter()

# print(cv)

# class A(object):
# 	def foo(self,x):
# 		print("executing foo %s,%s " % (self,x))

# 	@staticmethod
# 	def static_foo(x):
# 		print("executing static_foo %s " % x)

# a=A()
# a.foo(1)

# a.static_foo(1)

"""
executing foo <__main__.A object at 0x7f520aa62ba8>,1 
executing static_foo 1
"""

# b = Bunch()
# b.hello = 'world'

# print(b.hello)

"""
super() for get method and property parent class  

получаем по приоритету OtherCounter(Counter, OneCounter) слева на право 

"""
# class OneCounter:
# 	"""One Doc counter"""
# 	def __init__(self, initial = 0):
# 		self.one = initial


# class Counter:
# 	"""Doc counter parent"""
# 	all_counter = []
# 	def __init__(self, initial = 0):
# 		self.__class__.all_counter.append(self)
# 		self.value = initial

# class OtherCounter(Counter, OneCounter):
# 	"""Doc chaild counter"""
# 	def __init__(self, initial = 0):
# 		self.initial = initial
# 		super().__init__(initial)
# 	def getDoc(self):
# 		for d in __class__.__bases__:
# 			print(': '.join([d.__name__, d.__doc__]))

# c = OtherCounter()

# print(vars(c))

# c.getDoc()


# class A:
# 	var_name = 'Ivan'

# class B:
# 	var_name = 'Vasa'

# class C(B, A):
# 	pass

# bf = C()

# print(bf.var_name)

# print(C.mro())
"""
{'value': 0, 'initial': 0}
Counter: Doc counter parent
OneCounter: One Doc counter
Vasa
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
"""

#!/usr/bin/env python3
# coding=utf-8

#!/usr/bin/env python3
# coding=utf-8

# class LengMixin:
# 	def even_length(self):
# 		return len(self) % 2 == 0


# class MyList(list, LengMixin):
# 	pass

# ml = MyList([1, 4, 8, 11])

# ml.sort()

# print(ml)


# import module1
# import module2

# print(3)


# from simplecrypt import decrypt

# with open("encrypted.bin", "rb") as inp:
#     encrypted = inp.read()
	
# with open("passwords.txt", "rb") as inp:
# 	pwds = [s.decode("utf-8") for s in inp.read().split()]
# 	for pwd in pwds:
# 		try:
# 			print('Succesfully: ' + decrypt(pwd, encrypted).decode('utf8'))
# 		except:
# 			print('Password ' + pwd + ' didnt match')

# import datetime
# print((datetime.date(*list(map(lambda x: int(x), input().split()))) + datetime.timedelta(int(input()))).strftime('%Y %-m %-d'))
# # Если возникает ошибка ValueError: Invalid format string, придется переписать с помощью ручного форматирования


# def main():
#     lines = []
#     with open("dataset_24465_4 (2).txt", "r") as inp:
#         lines = [line for line in inp]

#     with open("output2.txt", "w") as out:
#         out.writelines(reversed(lines))

# if __name__ == "__main__":
#     main()


# import shutil
# import os

# def main():
#     ARCH_FILE = "main.zip"
#     shutil.unpack_archive(ARCH_FILE)
#     DIRNAME = ARCH_FILE.split(".")[0]

#     dir_with_py = []
#     for (dirpath, dirname, filenames) in os.walk(DIRNAME):
#         for i in filenames:
#             # if we have even one *.py file add the name of a directory
#             # to the dir_with_py list and go into the next directory
#             if i.lower().endswith(".py"):
#                 dir_with_py.append(dirpath)
#                 break

#     with open("dir_output.txt", "w") as dout:
#         for item in sorted(dir_with_py):
#             print(item, file=dout)

# if __name__ == "__main__":
#     main()

# import re


# def main_imp():
# 	print(__name__)
# 	print('this it work!')

# if __name__ == '__main__':
# 	main_imp()
# else:
# 	print('Import module')

# import csv, re

# with open("Crimes.csv") as file:
# 	list = [crime[5] for crime in filter(lambda x: re.match(r'.*2015', x[2]), csv.reader(file))]
# 	print(max(set(list), key=list.count))

# import requests
# import json

# artsy_token_url = "https://api.artsy.net/api/tokens/xapp_token"
# artsy_api_url = "https://api.artsy.net/api/artists/{}"

# info = {
#     "client_id": "c72ead62d8fb82ddd3ca",
#     "client_secret": "eea6663ca58325d9d41fb8e48c3b3a59"
# }

# class NotFound(Exception):
#     pass

# class TokenFail(Exception):
#     pass

# def get_token():
#     token_data = requests.post(artsy_token_url, data=info)

#     if token_data.status_code == 400:
#         raise NotFound

#     json_token = token_data.json()

#     return json_token["token"]

# def main():
#     headers = {"X-XAPP-Token": get_token()}

#     with open("dataset_24476_4.txt", "r") as artists_inp, open("dataset_24476_4_out.txt", "w") as artist_info_out:
#         reader = (art_id.rstrip() for art_id in artists_inp)
#         artists_info = []

#         for art_id in reader:
#             resp = requests.get(artsy_api_url.format(art_id), headers=headers)
#             json_resp = resp.json()
#             artists_info.append((json_resp["birthday"], json_resp["sortable_name"]))

#         artists_info.sort()

#         for artist in artists_info:
#             print(artist[1], file=artist_info_out)


# if __name__ == "__main__":
#     main()

from turtle import *
import random



ob = Turtle()



class FracFl:
	def __init__(self, x= 0, y = 0):
		self.x = x
		self.y = y

	def __mul__(self, other):
		if isinstance( other, (int, float) ):
			return FracFl(self.x * other, self.y * other)
		elif isinstance(other, __class__):
			return FracFl(self.x * other.x, self.y * other.y)

v = FracFl(2, 5)
v1 = FracFl(3, 6)

v2 = v * v1

print(v2.x)


ob.speed(3)

cl = ['red', 'green', 'blue']

def draw_fractal(length, angle, x, y):
	ob.up()
	ob.goto(x, y)
	ob.down()


	c = 0
	ob.begin_fill()
	for i in range(5):

		x = random.randint(-100, -1)
		y = random.randint(1, 100)

		x = x // (x ** 2 + y ** 2)
		y = y // (x ** 2 + y ** 2)



		print(x)
		print(y)

		ob.fillcolor(cl[c])
		ob.goto(x, y)
		# x += 1
		# y += 1
		c += 1
		if c >2:
			c = 0
	ob.end_fill()




draw_fractal(200, 120, -30, 40)

exitonclick()