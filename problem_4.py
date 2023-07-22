authors = {
    "Science Fiction": "Andy Weir",
    "Fantasy": "Brandon Sanderson",
    "Drama": "Diana Gabaldon"
}

# loop through the above dictionary and print "The best author of (insert genre here)
# is (insert author here)!"
for key, value in authors.items():
    print(f"The best author of {key} is {value}")