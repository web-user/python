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
Инкапсуляция - это свойства системы позволяющее обьединить данные и методы 
работающие с ними , в классе и скрыть детали реализации 

"""
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		