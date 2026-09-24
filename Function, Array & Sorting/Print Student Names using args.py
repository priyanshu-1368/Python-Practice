def print_students(*args):
    if not args:
        print("The list is empty.")
        return
    for name in args:
        print(name)

print_students("Alice", "Bob", "Charlie")
print_students()