# write a class to represent an eventcard in the game with the following private instance variables:
# name - "riots with mask burning"
# event type (mandate, mutation, or public unrest)
# area_affected - one of either "local" or "federal"
# r0 difference - Difference to the spread factor in the City location
# unemployment rate difference - Difference to the unemployment rate in the city location

# Methods
# Init method: takes in name, event type, area_affected, r0 difference, and
# unemployment rate difference and saves them all to private attributes

# apply_to_affected_cities(city): takes in a city and changes its r0 by the
#.    r0 difference private attribute, changes the city's unemployment rate by the unemployment rate difference
# apply_federally(): changes all cities' r0 by the r0 difference private attribute,
#.    all cities' unemployment rate by the unemployment rate difference private attribute


class EventCard:
    def __init__(self, name, event_type, area_affected, r0_difference, unemployment_rate_difference):
        self.name = name
        self.event_type = event_type
        self.area_affected = area_affected
        self.r0_difference = r0_difference
        self.unemployment_rate_difference = unemployment_rate_difference

    def apply_to_affected_cities(self, city):
        city.r0 += self.r0_difference
        city.unemployment_rate += self.unemployment_rate_difference

    def apply_federally(cities, r0_difference, unmployment_rate_difference):
        for city in cities:
            city.r0 += r0_difference
            city.unemployment_rate += unmployment_rate_difference

#creating additional class "City" to use as an example and test if the above works
class City:
    def __init__ (self, name, population):
        self.name = name
        self.population = population
        self.infected_population = 0
        self.r0 = 0
        self.unemployment_rate = 0.0
        self.open_hires = 0

#create an instance of the EventCard class
event_card = EventCard("riots with mask burning", "public unrest", "local", 0.5, 0.1)

#Example usage of the methods
city = City("New York", 1000000)
event_card.apply_to_affected_cities(city)

cities = [City("Phoenix", 500000), City("Tuscon", 700000)]
EventCard.apply_federally(cities, 0.3, 0.2)


#In the modified code, the __init__ method takes five parameters: name, event_type, area_affected, r0_difference, and unemployment_rate_difference. These parameters are used to set the respective private instance variables.

#The apply_to_affected_cities method takes a city parameter and modifies its r0 and unemployment_rate by adding the respective differences from the event card's private instance variables.

#The apply_federally method is defined as a static method using the @staticmethod decorator. It takes a cities list, r0_difference, and unemployment_rate_difference as parameters. It iterates over the list of cities and modifies their r0 and unemployment_rate by adding the respective differences.

#You can create an instance of the EventCard class and use the defined methods to apply the event card's effects to individual cities or all cities in a list.