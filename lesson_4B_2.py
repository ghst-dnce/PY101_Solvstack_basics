colors = ("red", "green", "blue", "indigo", "violet")

# I want each of the strings to be assigned to their own
# individual variables instead of being in the color tuple

# the variable names red and green will match up
# to the first two values in the tuple.
# the asterisk before the variable rest_of_colors,
# will assign the remaining elements as a list

# longform
red = colors [0]
green = colors [1]
rest_of_colors = colors[2:-1]
rest_of_colors = list(rest_of_colors)

# shortform minimax way of doing the above
(red, green, *rest_of_colors) = colors
print(red)
print(green)
print(rest_of_colors)