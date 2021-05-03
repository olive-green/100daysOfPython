
a=10

def random():
    global a # we have to use global keyword explicity to define a local varaible into global variable
    a=4
    print("inside function",a)

random()
print("outside function",a)
