# set
# 1. it is built in data type in pytho use to store a collection of data
# 2. it is unordered, store only unique value, Mutable (can add and remove value)


# create set in python
# 1. by using {}
set_of_fruits = {'apple', 'orange', 'banana'}
print(set_of_fruits)

# 2. create using set() constructor
#  when create with set constructor set should pass one iterable
set_of_clothes = set(['pant', 'gloves', 't-shirts'])
print(set_of_clothes)
# Creating an empty set
empty_set = set()


# some important methods
# 1. Add
colors = {"red", "green"}
colors.add("blue")
print(f"colors = {colors}")
# 2. Update
# Adds multiple items from a list, tuple, or another set.
list_of_rem = ['black', 'orange']
colors.update(list_of_rem)
print(f"After Updating colors = {colors}")

# 3. Remove
# Removes an item. Raises an error if the item doesn't exist.
# colors.remove('gray')  # it will raise keyerror

# 4. Discard
# # Removes an item. Does not Raises an error if the item doesn't exist.
colors.discard('gray')

# 5. Pop
# Removes and returns a random item (since sets are unordered).
remove_item = colors.pop()
print(remove_item)
# 6. Clear
colors.clear()
print(f"colors after clear: {colors}")


# a={1,2,3,4,5}
# b={2,4,6,8}

# a.update(b)
# c=a.union(b)
# c=a.intersection(b)
# c=b.difference(a)
# c=a.isdisjoint(b)
# c=a.issuperset(b)
# c=b.issubset(a)
# c=a.symmetric_difference(b)
# print(c)

# print(a.difference_update(b))
# a.difference_update(b)
# print(a)
