#lists can have any number of items and they may be of different types (integer, float, string etc.).

l1=["pankaj",21,"94%"]
print(l1)

# A list can also have another list as an item. This is called a nested list.
l2=[12,["ehyy"],"Ruby"]
print(l2[1])

# Negative indexing
# Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.
print(l2[-1])

### slicing
l3 = ['p','r','o','g','r','a','m','i','z']
# print(l3[:])
# print(l3[:2])
print(l3[1:4])
print(l3[-1:-2])


### Add/Change List Elements
# Lists are mutable, meaning their elements can be changed unlike string or tuple.

# We can use the assignment operator = to change an item or a range of items.
l3[2]="hey"

#### We can add one item to a list using the append() method or add several items using extend() method.
l3.append("Pankaj")
l3.extend(['ankit','aman'])
print(l3)

#### Lists methods
# append() - Add an element to the end of the list
# extend() - Add all elements of a list to the another list
# insert() - Insert an item at the defined index
# remove() - Removes an item from the list
# pop() - Removes and returns an element at the given index
# clear() - Removes all items from the list
# index() - Returns the index of the first matched item
# count() - Returns the count of the number of items passed as an argument
# sort() - Sort items in a list in ascending order
# reverse() - Reverse the order of items in the list
# copy() - Returns a shallow copy of the list

print(l3.pop(2))
print(len(l3))
print(l3.index('g'))


####List Comprehension: Elegant way to create Lists
# List comprehension is an elegant and concise way to create a new list from an existing list in Python.

# A list comprehension consists of an expression followed by for statement inside square brackets.

# Here is an example to make a list with each item being increasing power of 2.

pow2 = [2 ** x for x in range(10) if x<4]
print(pow2)