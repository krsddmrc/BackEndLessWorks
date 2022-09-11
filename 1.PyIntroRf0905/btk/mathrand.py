#import math #!metod1
#import math as islem #!method2
#from math import factorial,ceil,floor #!method 3, only in usage
from math import * #!method3
import random
#value=dir(math)
#value=help(math)
#value=help(math.factorial)
#value=math.sqrt(49) #7
#value=math.factorial(5)#120
#value=math.floor(5.9)#5
#value=math.ceil(5.9)#6
#value=islem.ceil(5.9)#6 method2
#value=factorial(5) #120 #!method3
#value=floor(5.9) #5 #!method3
#value=ceil(5.9) #6 #!method3
#print (value)  
"""random modules"""
#result =dir(random) #to see modules
#result=help(random) #to see usage of modules
#result=random.random() # to generate a number between 0.0 and 1.0
#result=random.uniform(1,10) # to generate a number between 1.0 and 10.0 with 15 elements after comma
#result=int(random.uniform(10,100)) # to generate a number between 10.0 and 100.0 with 15 elements after comma
#result=random.randint(10,100)) # to generate a number between 10 and 100 with integeer
#names=["john","jane", "jack", "james", "jenyy", "jonny" ]
#result=names[random.randint(0,len(names)-1)]  # with a random number take name
#print(result)
#result=random.choice(names) # to take sema result
#liste=list(range(10)) # to create a list with 10 elements
#random.shuffle(liste) # to shuffle the list
#result=liste # shuffled list
liste=range (100)
result=random.sample(liste,3) # to take the 3 element of sample from the list
print(result)


