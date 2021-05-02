#in python you can return two output from a function

def add_sub(x,y):
    a=x+y
    b=x-y
    return a,b

addition,subtraction=add_sub(5,4)
print(addition,subtraction)

# in python there is no concept of pass by value or pass by reference

# ex
def update(x):
    print(id(x))
    x=6
    print(id(x))

a=10
update(a)    
print(id(a))

# here the address of a and x will be same but a's value doesn't change if x changes


# in python we can add variable arguments as a parameter, and also if we don't know the order of parameters we can simply write it on the calling function 
# and we can also give default value to a parameter of function

def person(name,age):
    print(name)
    print(age)

person(age=20,name="Pankaj")

def Person(age,name="Ankit"):
    print(name)
    print(age)

Person(15)

def sum(a,*b):  #just add * before a variable for unknow arguments
    print(a)
    print(b)

sum(2,3,4,5)

# so all the other extra arguments are stored as a tuple in * one variable




