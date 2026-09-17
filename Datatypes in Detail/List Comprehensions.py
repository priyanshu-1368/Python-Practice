squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)

evens = [x for x in range(1, 21) if x % 2 == 0]
print("Evens:", evens)

string_list = ["hello", "WORLD", "PyThOn"]
lowercase_list = [s.lower() for s in string_list]
print("Lowercase strings:", lowercase_list)