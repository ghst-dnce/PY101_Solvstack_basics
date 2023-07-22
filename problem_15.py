first_set = {5, 10, 15, 20, 25}
second_set = {10, 15, 40, 75}

# add code that updates first_set to contain the values {20, 5, 40, 25, 75}
# (order unimportant)
first_set.update({20, 5, 40, 25, 75})

# Values 20, 25, and 5 will not appear in the updated set, since duplicates are automatically removed.

print(first_set)
