set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: Combines elements from both sets (no duplicates)
union_set = set_a | set_b  # Alternative: set_a.union(set_b)
print("Union:", union_set)

# Intersection: Elements common to both sets
intersection_set = set_a & set_b  # Alternative: set_a.intersection(set_b)
print("Intersection:", intersection_set)

# Difference: Elements in set_a but NOT in set_b
difference_set = set_a - set_b  # Alternative: set_a.difference(set_b)
print("Difference (A - B):", difference_set)