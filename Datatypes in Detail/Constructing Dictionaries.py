keys = ['id', 'name', 'email']
values = [101, 'Bob', 'bob@example.com']

# The zip() function pairs the elements from both lists, 
# and dict() converts those pairs into a dictionary.
student_dict = dict(zip(keys, values))

print("Created Dictionary:", student_dict)