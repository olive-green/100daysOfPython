# we can inherit one class into other class

class A:
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")

class B(A): #that's how we inherit the parent class
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
# similarly class C can inherit the features of b and a by calling only b
class C(B):
    def feature5(self):
        print("feature 5 is working")
    def feature6(self):
        print("feature 6 is working")

obj1=B()
obj2=C()

obj1.feature1()
obj2.feature1()
