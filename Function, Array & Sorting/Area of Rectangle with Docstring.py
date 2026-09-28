def calculate_area(length, width):
    """
    Calculates the area of a rectangle.

    Parameters:
    length (float/int): The length of the rectangle.
    width (float/int): The width of the rectangle.

    Returns:
    float/int: The area of the rectangle.
    """
    return length * width

print(calculate_area.__doc__)
print("Area:", calculate_area(5, 4))