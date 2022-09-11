"""Class -->Person (name, surname, birthday, calculate())
    attributes, methods"""
#lst1=[1,2,3]
#lst2=[1,2,3]
#result1=type(lst1)
#result2=type(lst2)
#print (result1)
#print (result2)
#!  printed: <class 'list'>
#!  printed: <class 'list'>
"""#lst1. it is written "lst1" and put the comma "." end of the line,
   it is seen a list of methods. we can use these on the Instance."""

#!Instance (object)
#class Person: # after this statement  we must to add a statement at least
#   pass           #   " pass"  not to take an error.
#p1=Person()
#p2=Person()
#print(p1) #in  different adrress same object
#print(p2)
#print(type(p1)) # types are same 
#print(type(p2))
#print(p1==p2) # false, they are not equal
#! Class attributes
    #address="no information"
    #! constructor (is a creator method, different from class attribute, to ınstnace    )
        #def __init__ (self): # self is take an attributes form class to object
    #! object attributes
            #self.name=name
            #self.year=year
    #! object (instance)
            # p1=Person('john', 1990)
            # p2=Person("Jane", 1991)     # the parameters numbers must be equal
#class Person:
#    address="no informations" #class attributes for all member of the class 
#    def __init__(self, name, year): # a conrtructor, it gets an attributes for ınstances/objects
#        self.name=name          # attributes must to be equal (numbers)
#        self.year=year
#p1=Person(name="John", year=1990)
#p2=Person(name="Jane", year=1991) #There is no space at the beginnig of the statement.
#print(f'p1:name:{p1.name} year: {p1.year} address:{p1.address}')
#print(f'p2:name:{p2.name} year: {p2.year} address:{p2.address}')

"""----------adding methods  to Class---------------"""
#class Person:
#    address="no informations" #class attributes for all member of the class 
#    def __init__(self, name, year): # a conrtructor, it gets an attributes for ınstances/objects
#        self.name=name          # attributes must to be equal (numbers)
#        self.year=year  
#    def intro(self):#  methods runs in class, in instance needs to add self
#        print("Hello, There!"+ "I am " + self.name)
#    
#    def calculateAge(self):
#        return 2019- self.year
#
#p1=Person(name="John", year=1990)
#p2=Person(name="Jane", year=1991)
#p1.intro()
#print (f'Adım:{p1.name} Yaşım:{p1.calculateAge()}')

#! Exaple 2 : 
#class Circle:   
#    #class object attrib.  
#    pi=3.14  
#
#    def __init__(self, yaricap=1):
#        self.yaricap=yaricap  
"""Methods"""   
#    def cevre_hesap(self):
#        return 2 * self.pi + self.yaricap
#
#    def alan_hesap(self):
#        return self.pi * (self.yaricap**2)
#c1=Circle()
#c2=Circle(5)
#
#print (f' c1:alan={c1.alan_hesap()} çevre={c1.cevre_hesap()}')
#print (f' c2:alan={c2.alan_hesap()} çevre={c2.cevre_hesap()}')
## ! in this example, we must to use "pi" with self, because we use "pi"
## ! in functions (in local )
"""ınheritance: Kalıtım , miras alma"""
# class Person-->name, lastname, age, eat(), drink()
# class Student(Person), class Teacher(Person)
#an example:
#class Person():
#    def __init__(self):
#        print(" Person Created")
#
#class Student():
#    def __init__(self):
#        Person.__init__(self) # ! in locals, if we want to print " Person Created"
#                                # ! we must to call Person in local
#        print(" Student Created")
#
#p1=Person()
#s1=Student()
#
"""an other example"""  
#class Person():
#    def __init__(self, fname,lname):
#        self.firstName=fname 
#        """Yapısal attr. lara (self.***) dışardan gelecek özellikleri (attr.)
# atamak gerekiyor. Instance(obje) özelliklerine dışardan geleni atadık"""
#        self.lastName=lname
#        print(" Person Created")
#    def who_am_i(self):
#        print("I am a person")
#
#class Student(Person):
#    def __init__(self, fname,lname, number):#!if we add a special attribute of student Class 
#        self.studentNumber=number  #!we must assign with self.attrrb, and use it with attrb. of self
#        Person.__init__(self, fname,lname)  # aynı gerekçelerle burada yazdık                              
#        print(" Student Created")
#    def who_am_i(self):
#        print("I am a student") #! override 
#p1=Person('John', "Doe")
#s1=Student("Jane", "doe", 256)
#print(p1.firstName, p1.lastName)
#print(s1.firstName, s1.lastName,s1.studentNumber) ##!we must assign with self.attrrb, and use it with attrb. of self
#
#p1.who_am_i()
#s1.who_am_i()
"""Methods--------__str__---------------"""
class Movie():
    def __init__(self, title, director, duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("movie object is occured")

    def __str__(self):
	    return f"{self.title} by {self.director}" 

m=Movie("film adı", "yönetmen adı", "filmin süresi")

print(str(m))  




