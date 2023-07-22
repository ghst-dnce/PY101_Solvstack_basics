mixed_tuple = ("Sunshine", "Daisies", True, False, 0, 1, None)
# if you really must make changes

# first change the tuple to a list using the previously mentioned
# list constructor
mixed_tuples_as_list = list(mixed_tuple)

# now that we have a list, we can do the normal shennanigans to
# make whatever changes we want
# in this case, let's delete the last 4 values
del mixed_tuples_as_list[-5:]

# now let's change this back to a tuple
# using the tuple constructor
mixed_tuple = tuple(mixed_tuples_as_list)
print(mixed_tuple)