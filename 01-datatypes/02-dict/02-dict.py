# others important method in dictionary
employee = {
    'name': 'John',
    'age': 30,
    'department': 'Sales',
    'salary': 50000,
    'city': 'New York'
}

# 1. get all keys in dictionary
# returns a view object that displays a list of all the keys in the dictionary
keys = employee.keys()
print(keys)


# 2. get all values in dictionary
# returns a view object that displays a list of all the values in the dictionary
values = employee.values()
print(f"employee values: {values}")


# 3. get all key-value pairs in dictionary
# returns a view object that displays a list of a dictionary's key-value tuple pairs
items = employee.items()
print(f"employee items: {items}")


# 4. remove all items from dictionary make dictionary empty
mobile_spec = {
    'brand': 'Samsung',
    'model': 'Galaxy S21',
    'price': 799,
    'storage': '128GB'
}
print(f"mobile spec before clear: {mobile_spec}")
mobile_spec.clear()
print(f"mobile spec after clear: {mobile_spec}")

# 5.create a empty dictionary and update it with another dictionary using update() method
others_emp = {}
others_emp.update(employee)
print(f"others emp: {others_emp}")
