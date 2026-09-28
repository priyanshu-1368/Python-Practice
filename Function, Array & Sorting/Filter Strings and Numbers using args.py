def separate_types(*args):
    strings = []
    numbers = []
    for item in args:
        if isinstance(item, str):
            strings.append(item)
        elif isinstance(item, (int, float)):
            numbers.append(item)
    return tuple(strings), tuple(numbers)

str_tuple, num_tuple = separate_types("apple", 10, "banana", 25.5, 30)
print("Strings:", str_tuple)
print("Numbers:", num_tuple)