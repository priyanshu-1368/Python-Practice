def rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

a, p = rectangle_properties(10, 5)
print("Area:", a)
print("Perimeter:", p)