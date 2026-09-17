# String to an integer
string_val = '123'
int_val = int(string_val)

# List to a tuple
list_val = [1, 2, 3]
tuple_val = tuple(list_val)

# Tuple to a list
tup_val = (4, 5, 6)
new_list_val = list(tup_val)

# List of pairs to a dictionary
pairs_list = [(1, 'A'), (2, 'B')]
dict_val = dict(pairs_list)

print("String to Int:", int_val, type(int_val))
print("List to Tuple:", tuple_val, type(tuple_val))
print("Tuple to List:", new_list_val, type(new_list_val))
print("Pairs to Dict:", dict_val, type(dict_val))