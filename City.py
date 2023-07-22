# Make a city class with the following private instance variables:
# name
# population
# infected_population
# r0 - Spread factor in the City location
# unemployment rate
# open hires

# Make the following instance methods:
# Init method - takes in name and population,
# saves the name and population as instance variables
# then randomizes the starting unemployment rate between 7 and 12%,
# saves taht unemployment rate to the instance variable, and
# applies that unemployment rate to the population, and sets it as the open hires private instance variable

import random

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.infected_population = 0
        self.r0 = 0 # Spread factor in the City location
        self.unemployment_rate = random.uniform(0.07, 0.12) # Randomize unemployment rate
        self.open_hires = int(self.population * self.unemployment_rate) # Calculate open hires

my_city = City("Phoenix", 1000000)
print(my_city.__dict__)
print(my_city)

