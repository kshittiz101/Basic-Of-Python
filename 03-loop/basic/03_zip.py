# zip
# zip() aggregates multiple iterables (list, tuples, etc). in parallel,
# returning an iterator of tuples where each tuple contains corresponding elements
#  from each iterable


# symtax
# zip(*iterables)


names = ["Harry", "John", "Hari", "Peter"]
scores = [90, 29, 55, 99]

for name, score in zip(names, scores):
    print(f"{name}: {score}")


# 2. Handling different lengths: Stops at the shortest
# [(1, 'a'), (2, 'b'), (3,'c)]
different_length = list(zip(['a', 'b', 'c', 'd'], [1, 2, 3]))
print(different_length)


# 3. Building a dictionary
keys = ['name', 'age', 'city']
values = ['Tom', 25, 'Beijing']
person = dict(zip(keys, values))

print(person)
# {'name': 'Tom', 'age': 25, 'city': 'Beijing'}
