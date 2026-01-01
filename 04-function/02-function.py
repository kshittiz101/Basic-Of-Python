#
# parameters and arguments in functions
# parameters are the variables defined in the function definition
# arguments are the values passed to the function when calling it
# argurements are actual values while parameters are placeholders

def add_numbers(a, b):
    ''' This function takes two parameters a and b,
    adds them and returns the result '''
    return a + b


# calling the function
result = add_numbers(5, 10)
print(f"The sum is: {result}")

# Default Parameters


def multiple_numbers(num1, num2=20):
    ''' This function takes two parameters num1 and num2,
    multiplies them and returns the result.
    num2 has a default value of 2 '''
    return num1 * num2


# num2 will take the default value of 20
default_example = multiple_numbers(10)
print(f"Multiplication with default parameter: {default_example}")


# Positional and keyword Arguments
def personal_info(name, age, city):
    '''
    This function takes three parameters name, age, and city, 
    and returns a formatted string with the personal information.

    '''
    return f"{name} is {age} years old and lives in {city}."


# calling the function with positional argument
# in positional arguments, the order matters
positional_example = personal_info("Alice", 30, "New York")
print(f"Positional Argument: {positional_example}")

# calling the function with keyword argument
# in keyword arguments, the order does not matter
keyword_example = personal_info(age=25, city="Los Angeles", name="Bob")
print(f"Keyword Argument: {keyword_example}")
