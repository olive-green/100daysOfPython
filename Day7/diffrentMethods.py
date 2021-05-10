# methods are of three types
# instance methods
# class methods
# static methods

# instance methods are those methods which have self as a parameter or we can those methods which are according to instances

#class methods are methods which have access of class variables and are defined by @classmethods

#static methods are those methods which don't have any parameters
#and are defined by @staticmethods

class Student:
    school="APS"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    #class methods
    @classmethod
    def schoolName(cls):
        return cls.school
    
    # static methods
    @staticmethod
    def info():
        print("This is studnet class")

s1=Student(12,34,5)
s2=Student(234,53,6)
print(s1.avg())
print(s2.avg())

print(Student.schoolName())
print(Student.info())