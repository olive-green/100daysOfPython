# Creating a Tuple
# A tuple is created by placing all the items (elements) inside parentheses (), separated by commas. The parentheses are optional, however, it is a good practice to use them.

x=(23,4,"HEyy")
y = 12,32,4

print(x)
print(y)

# we can also unpack this tuple
a,b,c=y
print(a,b,c)

# Creating a tuple with one element is a bit tricky.

# Having one element within parentheses is not enough. We will need a trailing comma to indicate that it is, in fact, a tuple.

my_tuple = ("hello")
print(type(my_tuple))  # <class 'str'>

# Creating a tuple having one element
my_tuple = ("hello",)
print(type(my_tuple))  # <class 'tuple'>

# Parentheses is optional
my_tuple = "hello",
print(type(my_tuple))  # <class 'tuple'>


#### note- in tuples rest slicing,negative indexing and accesing are same as list
#### we cannot delete a element of tuple , we can just delete the whole tuple

# Changing a Tuple
# Unlike lists, tuples are immutable.

# This means that elements of a tuple cannot be changed once they have been assigned. But, if the element is itself a mutable data type like a list, its nested items can be changed.

# We can also assign a tuple to different values (reassignment).