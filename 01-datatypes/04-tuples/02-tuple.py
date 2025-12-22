# important method in tuple
# tuples are very few method, because of it immutablity


# count() -this method return the number of time the value appears in the tuple
tuple_of_nums = (20, 23, 25, 65, 2, 1, 2, 4, 2)
print(tuple_of_nums.count(2))

# index() - this method return the index of the first occureance of item
# note: Gives an error if the value is not found.
print(tuple_of_nums.index(2))

# len() - this method return the lengt of the tuple
print(len(tuple_of_nums))


# max() - return the largest among the tuple
print(max(tuple_of_nums))

# min() - return the minimun among the tuple
print(min(tuple_of_nums))


# sum() - provide the total of the tuple
print(sum(tuple_of_nums))

# concatenation
t1 = (10, 20)
t2 = ("alex", "ram", 45, 55)
t3 = t1 + t2
print(t3)

# repetition
t4 = t1*3
print(t4)

# membership check
if 20 in t1:
    print("Avaiable")
else:
    print("not Avaiable ")


# Tuple unpacking means assigning the values of a tuple to multiple variables in a single statement.
t = (10, 20, 30)
a, b, c = t

print(a)  # 10
print(b)  # 20
print(c)  # 30
