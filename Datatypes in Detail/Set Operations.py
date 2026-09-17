# Create a set of integers
my_set = {1, 2, 3, 4, 5}

# Add 6
my_set.add(6)

# Remove 3
my_set.remove(3) 
# Note: You can also use my_set.discard(3) which won't throw an error if 3 is missing.

# Check if 2 is in the set
is_present = 2 in my_set

print("Updated set:", my_set)
print("Is 2 in the set?:", is_present)