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
