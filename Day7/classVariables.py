# the variables which are created inside the methods are called instance variables
#while the variables which are created outside the methods are called class variables which are common to all objects

class Car:

    wheels=4
    def __init__(self,price,model):
        self.price=price
        self.model=model

# instance
car1=Car(10,"Bmw")
car2=Car(20,"benz")

print(car1.model)
print(car2.model)

print(car1.wheels)