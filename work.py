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




lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
	"name": "Alice",
	"homework": [100.0, 92.0, 98.0, 100.0],
	"quizzes": [82.0, 83.0, 91.0],
	"tests": [89.0, 97.0]
}
tyler = {
	"name": "Tyler",
	"homework": [0.0, 87.0, 75.0, 22.0],
	"quizzes": [0.0, 75.0, 78.0],
	"tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

for item in students:
	print(item['name'])
	print(item['homework'])






















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









