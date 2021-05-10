# Class is a blueprint of objects
# Objects are the istances of class

# create a class

class computer:
    def config(self):
        print("config is i5,16gb") 

# creating a object
comp1=computer()


# calling confing method of class computer 
computer.config(comp1) #we have to pass object as a parameter as "self" argument is object

# we can call methods of a class  directly also
comp1.config()