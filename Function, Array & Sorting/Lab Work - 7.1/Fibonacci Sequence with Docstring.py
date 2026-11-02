def get_fibonacci(limit):
    """
    Generates a list of Fibonacci numbers up to a specified limit.

    Parameters:
    limit (int): The upper numerical boundary for the sequence.

    Returns:
    list: Sequence of Fibonacci numbers less than or equal to limit.
    """
    sequence = []
    a, b = 0, 1
    while a <= limit:
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(get_fibonacci.__doc__)
print("Fibonacci Sequence:", get_fibonacci(20))