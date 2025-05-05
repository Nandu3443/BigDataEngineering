#Parent Class
class Vehilce:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
        return "Engine started.."
    def stop_engine(self):
        return "Engine stopped!..."
    
#child Class
class Car(Vehilce):
    def __init__(self, make, model, year,fuel_type):
        #call parent class constructor 
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
    
    #method overriding
    def start_engine(self):
        print(f"{self.make} {self.model}'s engine started with {self.fuel_type}")


#creating an instance of child
my_car = Car("BMW","X5",2023,"Diesel")
print(my_car.make)
my_car.start_engine()
my_car.stop_engine()

my_vehicle = Vehilce("BMW","X5",2023)
print(my_vehicle.start_engine())

# Multile Inheritance

#parent
class Engine:
    def start(self):
        return "Engine starting..."
    def stop(self):
        return "Engine stopping.."

#parent
class Electric:
    def start(self):
        return "Electric engine powering up.."
    def charge(self):
        return "Charging battery.."
    def stop(self):
        return "Electric systems powering down"
    
#multiple Inheritance 
class HybridCar(Engine,Electric):
    def stop(self):
       engine_stop = Engine.stop(self)
       electric_stop = Electric.stop(self)
       return f"{engine_stop} {electric_stop}"
    

hybrid = HybridCar()
print(hybrid.start())
print(hybrid.charge())
print(hybrid.stop())

# Method Resolution Order(MRO)
print(HybridCar.__mro__)