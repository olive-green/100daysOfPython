# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# init() function is acted as constructor of a class in python

class Person:
    def __init__(self,name,age): #self is here object which is created when Person class is called
        self.name=name
        self.age=age
    def profile(self):
        print("Your profile is ",self.name,self.age)

Pankaj=Person("Pankaj",20)
Pankaj.profile()