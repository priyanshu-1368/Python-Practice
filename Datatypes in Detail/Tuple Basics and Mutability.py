numbers = (10, 20, 30, 40, 50)

print("Third item:", numbers[2])

# numbers[1] = 25
# Explanation of Mutability:
# If we run numbers[1] = 25,
# Python will show a TypeError: 'tuple' object does not support item assignment.
# Tuples are immutable.
# While lists are mutable (can be changed after creation),
# meaning once a tuple is created,
# its elements cannot be modified, added, or removed.