n= int(input("enter the no of length of series"))


def fib(n):
    a=0
    b=1
    if(n==1):
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c        
            print(b)

fib(n)


# print a fibonacci series less than n
# def febb(n):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     while True:
#         c=a+b
#         a=b
#         b=c
#         if b>n:
#             break
#         print(b)

# febb(n)