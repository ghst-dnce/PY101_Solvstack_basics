# this is the notation for defining a set
this_is_my_first_set = {"squirrel", "raccoon", True, 0, False, False}

print(f"value before: \n{this_is_my_first_set}")

# let's add a new string to our set
this_is_my_first_set.add("this is my brand new string that you should only see after this line of code runs")

print(f"value after: \n{this_is_my_first_set}")

# this is how to add multiple items to a set
# you can pass in any iterable type object (list, tuples, dictionaries, etc)
set_of_banks = {"Wells Fargo", "Chase", "Capital One"}
print(set_of_banks)

# let's add two more banks using a set
set_of_banks.update({"Ally", "Simple"})
print(set_of_banks)
# now using a list, let's try adding something we already added
set_of_banks.update(["Wells Fargo", "TD Bank"])
# hopefully only TD Bank gets added
print(set_of_banks)
