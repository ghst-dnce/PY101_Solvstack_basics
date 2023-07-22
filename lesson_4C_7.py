# Example 1:
#first_set = {"a", "b", "c", "d"}
#second_set = {"e", "f", "g", "h"}

#first_set.update(second_set)
#print(first_set)

# Example 2:
#first_set = {1, 2, 3, 4, 5}
#second_set = {4, 5, 6, 7, 8}

#first_set.intersection_update(second_set)
#print(first_set)

# OR
#first_set = {1, 2, 3, 4, 5}
#third_set = first_set.intersection(second_set)
#print(third_set)

# Example 3:

first_set = {1, 2, 3, 4, 5}
second_set = {4, 5, 6, 7, 8}

first_set.symmetric_difference_update(second_set)
print(first_set)

# OR
first_set = {1, 2, 3, 4, 5}
third_set = first_set.symmetric_difference(second_set)
print(third_set)
