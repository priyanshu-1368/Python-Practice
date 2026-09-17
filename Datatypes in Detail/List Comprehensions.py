# 1. Squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)

# 2. Even numbers from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Evens:", evens)

# 3. Convert strings to lowercase
string_list = ["hello", "WORLD", "PyThOn"]
lowercase_list = [s.lower() for s in string_list]
print("Lowercase strings:", lowercase_list)