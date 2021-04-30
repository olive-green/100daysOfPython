#Multi-line statement
#In Python, the end of a statement is marked by a newline character.
# But we can make a statement extend over multiple lines with the line continuation character (\). For example

x= 1+2+3+ \
	4+5+6+ \
	7+8+9
print(x)


#we can also write multiline code in paranthesis
y=(1+2+3+
	5+6)
print(y)

#Indentation
#Indentation can be ignored in line continuation, but it's always a good idea to indent. It makes the code more readable. For example:

# if True:
# 	print("Hello")
# 	a=5
# 	print(a)

# The above can be written as
if True: print("HEllo");  a=5; print(a) 