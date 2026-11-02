def calculate_cube(num):
    return num ** 3

def process_list(func, numbers):
    return [func(x) for x in numbers]

nums = [1, 2, 3, 4]
print(process_list(calculate_cube, nums))