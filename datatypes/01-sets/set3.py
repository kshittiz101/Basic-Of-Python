# Mathematical Set Operations

# 1. Union ( | )
# Combines all items from both sets (removes duplicates).
a = {1, 2, 3, 4, 5}
b = {2, 3, 4, 5, 6, 7}
union_of_sets = a | b
print(union_of_sets)

# 2. Intersection (`&`)
# Keeps only items present in both sets.
common_value = a & b
print(f"common value for sets : {common_value}")

# 3.Difference ( - )
# Keeps items in the first set that are not in the second set.
only_a = a - b
print(f"the only a element: {only_a}")


# 4. Symmetric Difference (`^`)
# Keeps items that are in either set, but not in both.
symmentric_diff = a ^ b
print(symmentric_diff)
