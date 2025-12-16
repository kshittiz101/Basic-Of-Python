# Dictionary is one of the built in data types in python 
# It store data in key-value pairs 
# key in dict is must be immutable (like strings, numbers, and tuples)


# creating dictionary 
coffee_recipe = dict("types": "black", "size":"medium", "is_suger": false)
print(f"coffee recipe : {coffee_recipe}")

# a={
#     "name":"sujan",
#     "age":30,

# }
# a=dict(name="sujan",age=24)

# print(type(a))
# print(a)

# print(a["email"])
# print(a.get("email","email is not found!!")) #it access direct from key

# print(a.values())
# print(a.keys()) 
# print(a.items())

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