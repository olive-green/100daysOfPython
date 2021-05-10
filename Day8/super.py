#you can call all the methods of parent class inside a child class by using super() method
# we can inherit one class into other class

class A:
    def __init__(self):
        print("this is A init")
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")

class B(A): #that's how we inherit the parent class
    def __init__(self):
        super().__init__()
        print("init of b")
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
# similarly class C can inherit the features of b and a by calling only b
# class C(B):
#     def feature5(self):
#         print("feature 5 is working")
#     def feature6(self):
#         print("feature 6 is working")

obj1=B()
obj1.feature1() # so here if we call obj1 then it will also print init of A beacause it is constructor but it doesnot print init of a if we define init of B
# to print init of a also we have to use super() method

# but in c init of a is print if we call super method inside it because it prefer methods of Grandparent class over parents class 
# obj2=C()
# print(obj2.feature1())
