#!/usr/bin/env python3

"""
Статические переменные и методы
не пренадлежат экземпляру класса а храняться в самом классе 
из экземпляра мы имеем к ним доступ 
к ним можно обращаться someClass.method_name()

"""

# class someClass:
# 	# static var
# 	# y = 20
# 	count = 0
# 	def __init__(self):
# 		self.__class__.count += 1

# c = someClass()
# print(c.count)

# f = someClass()
# print(f.count)

"""
c.y = 45 не меняем статическую переменную а создаем новую
она будет видна только для конкретного экземпляра класса 

"""
# c.y = 45

"""
изменения данных переменной класса 
через класс MyObj.int_field = 45 данные поменяються вовсех обьекттах и в классе
через обьект object1.int_field данные поменяються только в этом обьекте 
мы не изменили мы создалли атрибут данных 
"""

# class MyObj:
# 	int_field = 10
# 	str_field = 'test str'

# object1 = MyObj()
# object2 = MyObj()

# object2.str_field = 'Wow text'
# print(object2.str_field)
# print(object1.str_field)
# print(MyObj.str_field)

# MyObj.int_field = 18
# print(MyObj.int_field)
# print(object1.int_field)
# print(object2.int_field)

"""
обращения к методам обькта 

"""
# class Person:

# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def print_info(self):
# 		print(self.name, "is", self.age)



# join = Person('join', 22)

# Luci = Person('Luci', 20)

# join.print_info()
# Luci.print_info()

"""
доступы переменных , инкапсуляция __private_attr 

Инкапсуляция - это свойства системы позволяющее обьединить данные и методы 
работающие с ними , в классе и скрыть детали реализации 

"""

# class MyObject:
# 	def __init__(self):
# 		self.__private_attr  = 0 
# 	def get_data(self):
# 		return self.__private_attr

# obj  = MyObject()
# print(obj.get_data())

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

print(mean([1,2,3]))