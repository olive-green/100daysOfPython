from functools import reduce 

# What are lambda functions in Python?
# In Python, an anonymous function is a function that is defined without a name.

# While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.

# Hence, anonymous functions are also called lambda functions.
f= lambda x,y:x*y
print(f(3,4))
# Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned. Lambda functions can be used wherever function objects are required.


####In Python, we generally use it as an argument to a higher-order function (a function that takes in other functions as arguments). Lambda functions are used along with built-in functions like filter(), map() etc.

## with filter()
# The filter() function in Python takes in a function and a list as arguments.

# The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True.

nums=[2,1,3,5,4,6,7,8]

evens= list(filter(lambda n:  n%2==0, nums))
print(evens)


## with map()
# The map() function in Python takes in a function and a list.

# The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item.

doubles= list(map(lambda n:n*2,evens))
print(doubles)

# with reduce()
#it will reduce your list into some particular result
sum= reduce(lambda a,b:a+b,doubles)
print(sum)