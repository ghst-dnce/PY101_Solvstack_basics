# create two sets with strings for letters a through f & g through m respectively
set_1 = {"a", "b", "c", "d", "e", "f"}
set_2 = {"g", "h", "i", "j", "k", "l", "m"}

# set a new variable to a set containing the values of both set_1 and set_2
new_set = set_1.union(set_2)
print(new_set)
