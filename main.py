# args
def add(*args):
    print(args[3])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3,5,8,9))
# kawargs

def calculate(n,**kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]

calculate(2,add=3,multiply=5)

class Car:

    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")


my_car=Car(make="Toyota",model="Supra",colour="Candy Red",)
print(my_car.make)
print(my_car.model)
print(my_car.colour)
