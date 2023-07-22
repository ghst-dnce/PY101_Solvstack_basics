class Car:
    def __init__(self, make, model, year, tow_required=False):
        self.make = make
        self.model = model
        self.year = year
        self.tow_required = tow_required
        self.location = 'shop' # always starts at the shop
        self.symptoms = [ ]
        self.assignee = None

    def add_symptom(self, symptom):
        self.symptoms.append(symptom)

customer_1_car = Car("Dodge", "Neon", 2005, tow_required=True)
print(customer_1_car.__dict__)

customer_1_car.add_symptom("won't start")
customer_1_car.add_symptom("smoke")
customer_1_car.add_symptom("overheating")
customer_1_car.add_symptom("engine knocking")

print(customer_1_car.symptoms)

customer_1_car.assignee = "Timmy"
print(customer_1_car.assignee)

customer_2_car = Car("Ford", "Focus", 2009, tow_required=False)
print(customer_2_car.__dict__)
customer_2_car.add_symptom("ignition sputters on cold start")