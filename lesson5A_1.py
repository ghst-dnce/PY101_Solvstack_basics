class Car:
    def __init__(self):
        self.make = ""
        self.model = ""
        self.year = 0

my_car = Car()
print(my_car.__dict__) # returns instance variable, class attributes and functions
print(my_car)

#print(__name__)

my_car.make = "Jeep"
my_car.model = "Wrangler"
my_car.year = 2015
print(f"My car is a {my_car.year} {my_car.make} {my_car.model}.")