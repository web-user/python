#!/usr/bin/env python3

"""self 
Python присваивает значение self

есть класс с именем MyClass и экземпляр этого класса с именем myobject . При вызо-
ве метода этого объекта, например, “ myobject.method(arg1, arg2) ”, Python автоматиче-
ски превращает это в “ MyClass.method(myobject, arg1, arg2) ” – в этом и состоит смысл
self .
"""

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

"""абстрактные  классы. 
если в абстрактном классе объявляются методы или свойства с использованием декораторов 
@abstractmethod и @abstractproperty, то экземпляры производных классов не могут быть созданы

все методы обьявленые в абстрактном классе должны быть обьявлены в дочернем класе 

"""

# from abc import ABCMeta, abstractmethod, abstractproperty

# class Stackable:

#     __metaclass__ = ABCMeta # class Stackable(metaclass=ABCMeta)

#     @abstractmethod
#     def push(self,item):
#         pass

#     @abstractmethod
#     def pop(self):
#         pass

#     @abstractproperty
#     def size(self):
#         pass

# # класс, производный от класса Stackable
# class Stack(Stackable):

#     def __init__(self):
#         self.items = []

#     def push(self,item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop()

    # def size(self):
    #     pass



"""
Полиморфизм

один и тотже обьект введет себя по разному 

"""

# def mean(numbers):
#     return float(sum(numbers)) / max(len(numbers), 1)

# print(mean([1,2,3]))


"""В Python есть метод super(), который обычно применяется к объектам.
Его главная задача это возможность использования в классе потомке, методов класса-родителя."""


# Родительский класс
 
class A(object):

	def __init__(self):
		print(u'constructor class A')
 
# Потомок класса А
class B(A):

	def __init__(self):
		print(u'constructor class B')
		super(B,self).__init__()
"""Смысл примера заключается в том, что Python автоматически (сам по себе) не запустит родительский конструктор, поскольку мы
 его переопределили в классе B… Поэтому методом super() мы явно вызываем родительский конструктор."""


 """
Метаклассы
. Метаклассы существуют для изменения или добавления
нового поведения в классы.
 """

# Example

"""Допустим, мы хотим быть уверены, что мы всегда создаём
исключительно экземпляры подклассов класса SchoolMember , и не создаём экземпляры
самого класса SchoolMember .

Мы можем объявить наш класс как абстрактный базовый класс при помощи встроенного
метакласса по имени ABCMeta .
"""

from abc import *

class SchoolMember(metaclass=ABCMeta):
	'''Представляет любого человека в школе.'''
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('(Create SchoolMember: {0})'.format(self.name))

	@abstractmethod
	def tell(self):
		"""display information"""
		print('Name:"{0}" Age:"{1}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
	"""Represents a teacher"""
	def __init__(self, name, age, salary):
		super().__init__(name, age)
		self.salary = salary
		print('(Create Teacher: {0})'.format(self.name))

	def tell(self):
		super().tell()
		print('Salary: "{0:d}"'.format(self.salary))


class Student(SchoolMember):
	"""Represents a studenr"""
	def __init__(self, name, age, marks):
		super().__init__(name, age)
		self.marks = marks
		print('(Create student: {0})'.format(self.name))

	def tell(self):
		super().tell()
		print('Marks: {0:d}'.format(self.marks))

t = Teacher('Mrs, Shriv', 40, 30000)
s = Student('Swaroop', 25, 75)





class vectorClass:
	def __init__(self, x = 0, y = 0, z = 0):
		self.x = x
		self.y = y
		self.z = z

	def __mul__(self, other):
		if isinstance(other, (int, float)):
			return vectorClass(self.x * other,
				self.y * other,
				self.z * other)
		elif isinstance(other, __class__):
			return vectorClass(self.x * other.x,
				self.y * other.y,
				self.z * other.z)

v1 = vectorClass(1,2,3)
v2 = vectorClass(2,3,4)
v3 = v1 * v2

print(v3.x)
print(v3.y)