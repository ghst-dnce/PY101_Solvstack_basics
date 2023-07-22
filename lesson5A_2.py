class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

my_mentors_old_car = Car("Hyundai", "Elantra", 2013)
print(f"My mentor's old car is a {my_mentors_old_car.year} {my_mentors_old_car.make} {my_mentors_old_car.model}.")

my_car = Car("Ram 1500", "Laramie", 2013)
print(f"My car is a {my_car.year} {my_car.make} {my_car.model}.")