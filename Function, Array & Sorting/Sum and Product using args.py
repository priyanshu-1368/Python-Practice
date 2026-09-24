def calculate_sum_and_product(*args):
    total_sum = 0
    total_product = 1
    for num in args:
        total_sum += num
        total_product *= num
    return total_sum, total_product

s, p = calculate_sum_and_product(2, 3, 4)
print("Sum:", s)
print("Product:", p)