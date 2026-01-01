#decorator---it is a function which take another function as a argument and add some functionality and return function

#step 1
# def show():
#     print("hello sipalaya")
#     return "sujan"

# print(show())

#step 2
#everything in python is object

# def show():
#     print("hello sipalya")

# a=show
# a()

#step 3 ---=nested function

# def outer():
#     def inner():
#         print("this is inner function")

#     print("this is outer function")
#     inner()


# outer()


#step 4:function can take another function as argument
# def outer(func):
#     def inner():
#         print("this is inner function")
#         func()

#     print("this is outer function")
#     return inner


# def show():
#     print("hello sipalya")

# var=outer(show)
# var()


#alternative method
def outer(func):
    def inner():
        print("this is inner function")
        func()

    print("this is outer function")
    return inner

@outer
def show():
    print("hello sipalya")
show()


