# enumerate is python built in function, that help to fetch both index(postion)
# and value at the same time

# when to use it
# if we have to track both index and value in the loop

# syntax: enumerate(iterable, start=0 (by default is zero))
# example
list_of_coffee = ['black coffee', 'Americano', 'milk coffee']
for idx, coffee in enumerate(list_of_coffee, start=1):
    print(f"{idx}: {coffee}")
