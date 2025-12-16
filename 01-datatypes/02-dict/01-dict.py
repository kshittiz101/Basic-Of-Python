# Dictionary is one of the built in data types in python
# It store data in key-value pairs
# key in dict is must be immutable (like strings, numbers, and tuples)
#  Notes:
# 1. dict is unordered, changeable, and indexed
# 2. duplicate keys are not allowed, if we try to create dict with duplicate keys the last one will overwrite previous one.
# 3. dict is mutable, we can change, add, or remove items after the dict has been created.
# 4. dict is optimized to retrieve values when the key is known.
# 5. dict is defined with curly braces {} with key-value pairs separated by colon (:), and each key-value pair is separated by comma (,)


# when to use dictionary?
# 1. when we need a logical association between a key:value pair
# 2. when we need fast lookups for our data, based on a custom key
# 3. when we need a data structure that can be modified
# 4. when we need to represent real-world entities with their properties


# 1.creating dictionary
# method:1 using dict() function
coffee_recipe = dict(types="black", size="medium", is_suger=False)
print(f"coffee recipe : {coffee_recipe}")

# method: 2 using curly braces {}
laptop_spec = {'brand_name': 'Acer', "model": "Aspire 7", "price": 750000}
print(f"laptop spec : {laptop_spec}")


# see the type of dict
print(type(coffee_recipe))  # <class 'dict'>

# 2. accessing value
# method 1: using dict_name[key] it will through error if the key is not avaiable, it crached the programs
# print(f"laptop brand name: {laptop_spec['customer_review']}")

# method 2: using dict_name.get(key)
print(
    f"laptop review: {laptop_spec.get('customer_review', 'Not Avaiable')}"
)


# 3. updating value of dictionary
student = {'name': 'Harry', 'age': 22}
student['age'] = 28
print(f"{student.get('name')} age after update:{student.get('age', 'not found')}")


print(f"Before deleteling age value from student dict: {student}")

# delete the value in dictionary
del student['age']
print(f"After deleting age value from student dict: {student}")

#  deleting the entire dictionary
employee = {'name': 'John', 'age': 30}
del employee
# print(employee) # it will through error because employee dict is deleted
