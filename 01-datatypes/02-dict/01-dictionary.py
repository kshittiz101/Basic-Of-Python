# Dictionary is one of the built in data types in python
# It store data in key-value pairs
# key in dict is must be immutable (like strings, numbers, and tuples)


# creating dictionary
# method:1
coffee_recipe = dict(types="black", size="medium", is_suger=False)
print(f"coffee recipe : {coffee_recipe}")

# method: 2
laptop_spec = {'brand_name': 'Acer', "model": "Aspire 7", "price": 750000}
print(f"laptop spec : {laptop_spec}")


# see the type of dict
print(type(coffee_recipe))  # <class 'dict'>

# 1. accsss to value
# method 1: using dict_name[key] it will through error if the key is not avaiable, it crached the programs
# print(f"laptop brand name: {laptop_spec['customer_review']}")

# method 2: using dict_name.get(key)
print(
    f"laptop review: {laptop_spec.get('customer_review', 'Not Avaiable')}"
)


# 2. updating value of dictionary
student = {'name': 'Harry', 'age': 22}
student['age'] = 28
print(f"{student.get('name')} age after update:{student.get('age', 'not found')}")


#  1.accessing key and values
# it will provide the list of keys
print(f"laptop spec keys: {laptop_spec.keys()}")
# it will provide the list of value present in dict
print(f"laptop spec values: {laptop_spec.values()}")

#

# a.clear()
# a.copy

# a["email"]="sujan@gmail.com"
# b={
#     "age":31,
#     'email':"sujan@gmail.com"
# }

# a.update(b)
# print(a)

# a={
#     "name":"sujan",
#     "age":30,

# }

# a.pop("name")
# del a["name"]

# a.popitem()
# print(a)

# a.setdefault("email","sujan@gmail.com")
# print(a)


# sentence=input("enter your sentence here: ")
# a=sentence.split()
# count=len(a)
# print(count)
