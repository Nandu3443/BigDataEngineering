def function():
    pass

class Car:
    #class attributes
    wheels = 4

    #constructor/Intializer
    def __init__(self,make,model,year):
        #Instance attributes
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    #instance methods
    def start(self):
        print("car is starting..")

    def stop(self):
        print("car is stopped")

    def drive(self,distance):
        # self.odometer = self.odometer + distance
        self.odometer +=distance
        print(f"Drove {distance} km. Total: {self.odometer}  km")

# creating objects (instances)
my_car = Car("Toyota","Fortuner",2025)
your_car = Car("Honda","Civic",2022)

# access attribute and calling methods

print(my_car.make)
print(my_car.drive(100))
print(my_car.wheels)
print(your_car.wheels)
print(Car.wheels)
print(my_car.drive(50))

Car.wheels = 5 # will update value in all the objects created from it
my_car.wheels=5 # will update only in that respective object

print(my_car.wheels)
print(your_car.wheels)

print(your_car.make)
print(your_car.odometer)
print(your_car.drive(100))
print(your_car.odometer)