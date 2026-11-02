def process_numbers(numbers):
    total_sum = sum(numbers)
    max_val = max(numbers)
    min_val = min(numbers)
    return total_sum, max_val, min_val

s, maximum, minimum = process_numbers([12, 45, 2, 89, 34])
print("Sum:", s)
print("Maximum:", maximum)
print("Minimum:", minimum)