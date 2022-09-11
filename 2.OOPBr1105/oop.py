import os
os.system('cls' if os.name=='nt' else 'clear')
''' The OS module in Python provides functions for interacting with 
the operating system. OS comes under Python's standard utility modules.
This module provides a portable way of using operating system-dependent
 functionality. The *os* and *os. path* modules include many functions 
 to interact with the file system.Jun 16, 2022 
 'nt' means 'New Technology' which is come with the release of a 32-bit
  version initially. 
 '''
#!----------------Objects---------------
#def print_type(data): # a defination(function) of data
#    for i in data:
#        print(i, type(i))
#
#test = [ 122, 'John', (1,2,3,4), [1,2,3,4], { 1,2,3},True, lambda x:x]
#print_type(test)
#
#class Person:   #first char is Capt.
#    name='john'
#    age=45
#
#person1=Person()   # This means " an instant from Person()(Class) 
#                   # is created (person1) "
#person2=Person()
#
#print(person1.name)
#print(person2.name)
#Person.job='teacher'
#print(person1.job) # at first, it looks person1 (instant),
## if it cannot find, it search in class. finally it print the answer 'teacher'
#person1.location='Turkey'
#print(person2.location) # it is not an attribute for person2
#!------------------------------SELF keyword------------------
# class Person:
#     name = 'Barry'
#     age = 45
#     def test(self):
#         print('test')
#     def set_details(self, name, age):
#         self.name = name
#         self.age = age
#     def get_details(self):
#         print(self.name, self.age)
# person1 = Person()
# person1.test()
# Person.test(person1)----arka planda böyle yapıyor.
# Class- method-instance
# person1.get_details()-yazdırdığımda instance’de bulamayıp class’tan alacak. Barry ,45 verdi.
# person1.set_details('Aaron', 37)
# person1.get_details()-şimdi set edildiği için, Aaron, 37 verdi.
#!------------------------------ static method----------------
# class Person:
#     company = 'Clarusway'
#     def set_details(self, name, age):
#         self.name = name
#         self.age = age
#def get_details(self):
#         print(self.name, self.age)
#     @staticmethod
#     def salute():
#         print('Hi there!')
# # print(Person.name)

# person1 = Person()
# person1.salute()
#!------------------------------special methods-------------------
# class Person:
#     company = 'Clarusway'  #—class attri.

#     def __init__(self, name, age):--inst.attr.
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} {self.age}"

#     def get_details(self):
#         print(self.name, self.age)

# person1 = Person('Barry',45)
# person1.get_details()---person1 için Barry 45 yazdırdı.
# liste = [4,2,9,11,5]
# print(liste)
# print(person1)
# print(person1.__str__())

#!------------------------------encapsulation and abstraction---------
# class Person:
#     company = 'Clarusway'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self._id = 5000
#         self.__id2 = 4000

#     def __str__(self):
#         return f"{self.name} {self.age}"

#     def get_details(self):
#         print(self.name, self.age)

# person1= Person('Aaron',37)
# print(person1._id) #! don't touch "id", special. we cannot print "id"
# # print(person1.__id2) #!  "_" is attensions to us that it is a special data
# print(person1._Person__id2)#! we can print "id" with useing the Class name

# liste = [4,2,9,11,5]
# liste.sort() #! abstraction is used to protect data notto need being known
# print(liste)
##!--------------------- inheritance and polymorphism------------------
#class Person:
#    company = 'Clarusway'
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#
#    def __str__(self):
#        return f"{self.name} {self.age}"
#
#    def get_details(self):
#        print(self.name, self.age)
#
#class Lang:
#    def __init__(self, langs):
#        self.langs = langs
#
#    def display_langs(self):
#        print(self.langs)
#
#class Employee(Person, Lang):
#    def __init__(self, name, age, path, langs):
#        #! self.name = name
#        #! self.age = age
#        self.path = path
#        super().__init__(name,age)#! we want to use parent's data       
#        Lang.__init__(self, langs)
#        # self.langs = langs
#
##!--override----başka class ve tanımlama ifadeleri yerine tekrar çağırıp yeniden tanımlamalıyız. 
#    def get_details(self):
#        # print(self.name, self.age, self.path)
#        super().get_details()
#        print(self.path)
#
#emp1 = Employee('Barry', 45, 'FS', ['Python', 'JS'])
#emp1.get_details()
#emp1.display_langs()
#
## person1 = Person('Aaron',37)
## person1.get_details()
#!print(Employee.mro()) #  we use the ".mro" to see all parents Class
#From django.db import models
#Class Article(models.model):
#	 Name=models.charfield(max.length=30)
#	Class meta:
#		Ordering=[“name”]  default değeri değiştirdik.

