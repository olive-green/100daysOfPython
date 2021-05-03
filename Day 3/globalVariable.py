
a=10

def random():
    global a # we have to use global keyword explicity to define a local varaible into global variable
    a=4
    print("inside function",a)

random()
print("outside function",a)


# What if you want to change the value of x inside a function?
x = "global"

def foo():
    x = x * 2
    print(x)

foo()
# The output shows an error because Python treats x as a local variable and x is also not defined inside foo().

# To make this work, we use the global keyword. 