a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

if a == b == c == d:
    print("All four numbers are equal.")
elif a == b == c:
    print("Number 1, Number 2, and Number 3 are equal.")
elif a == b == d:
    print("Number 1, Number 2, and Number 4 are equal.")
elif a == c == d:
    print("Number 1, Number 3, and Number 4 are equal.")
elif b == c == d:
    print("Number 2, Number 3, and Number 4 are equal.")
else:
    if a == b:
        print("Number 1 and Number 2 are equal.")
    if a == c:
        print("Number 1 and Number 3 are equal.")
    if a == d:
        print("Number 1 and Number 4 are equal.")
    if b == c:
        print("Number 2 and Number 3 are equal.")
    if b == d:
        print("Number 2 and Number 4 are equal.")
    if c == d:
        print("Number 3 and Number 4 are equal.")

    if a != b and a != c and a != d and b != c and b != d and c != d:
        print("All numbers are distinct and no two numbers are equal.")

    if a < b:
        print("Number 1 is less than Number 2.")
    if a > b:
        print("Number 1 is greater than Number 2.")
    if a < c:
        print("Number 1 is less than Number 3.")
    if a > c:
        print("Number 1 is greater than Number 3.")
    if a < d:
        print("Number 1 is less than Number 4.")
    if a > d:
        print("Number 1 is greater than Number 4.")
    if b < c:
        print("Number 2 is less than Number 3.")
    if b > c:
        print("Number 2 is greater than Number 3.")
    if b < d:
        print("Number 2 is less than Number 4.")
    if b > d:
        print("Number 2 is greater than Number 4.")
    if c < d:
        print("Number 3 is less than Number 4.")
    if c > d:
        print("Number 3 is greater than Number 4.")