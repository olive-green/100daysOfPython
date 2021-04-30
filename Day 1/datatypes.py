# Data types in Python
# Every value in Python has a datatype. Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.

# Python Numbers
# Integers, floating point numbers and complex numbers fall under Python numbers category. They are defined as int, float and complex classes in Python.

# We can use the type() function to know which class a variable or a value belongs to. Similarly, the isinstance() function is used to check if an object belongs to a particular class.

a=4
print(type(a))

b=4.345
print(type(b))

c=4j
print(type(c))
print(isinstance(c,complex))
