# when to use  a function
# 1. when you want to reuse a code block multiple times
# 2. when you want to divide your code into multiple small parts to make it more
#    readable and manageable


# defining a function
def greeting():
    print("Good morning")


# calling a function
# we have to call the function to execute the code inside it
# function should be called by its name followed by parentheses
greeting()


# type of function
# 1. function without parameters and without return type
# example:
def welcome_message():
    ''' This function is an example of a function 
    without parameters and without return type '''
    print("Welcome to our store!")


# calling the function
welcome_message()
# 2. function with parameters and without return type


def greet_user(name):
    ''' This function is an example of a function 
    with parameters and without return type '''
    print(f"Hello, {name}! Welcome to our store.")


# calling the function
greet_user("Ram")


# 3. function without parameters and with return type


def get_store_name():
    ''' This function is an example of a function 
    without parameters and with return type '''
    return "SuperMart"


store_name = get_store_name()
print(f"Store Name: {store_name}")

# 4. function with parameters and with return type


def get_greeting_message(name):
    ''' This function is an example of a function 
    with parameters and with return type '''
    return f"Hello, {name}! Welcome to our store."


greeting_msg = get_greeting_message("Harry")
print(greeting_msg)
