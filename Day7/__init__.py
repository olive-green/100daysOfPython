# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# init() function is acted as constructor of a class in python

class Person:
    def __init__(self,name,age): #The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
        # It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
        self.name=name
        self.age=age
    def profile(self):
        print("Your profile is ",self.name,self.age)

Pankaj=Person("Pankaj",20)
Pankaj.profile()