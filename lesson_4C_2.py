# some examples of sets that can be created by passing in different object types

# a string is a sequence
set1 = set("abcdefghijklmn")
# you can pass in a list
set2 = set([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
# or even a tuple!
set3 = set((True, False, 1, 2, "arm", "nose", False))

print(f"set1: \n{set1}")
print(f"set2: \n{set2}")
print(f"set3: \n{set3}")