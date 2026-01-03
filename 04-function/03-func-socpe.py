# function scope in python
# The python determines the scope visibility of variables based on
# LEGB rule
# L - Local
# E - Enclosing
# G - Global
# B - Built-in

# 1. local variable scope
def local_scope():
    local_var = 10
    print("local variable inside function:", local_var)


local_scope()


# 2. Enclosing variable scope
def outer_function():
    # outer function scope is now enclosing scope for the
    # inner function
    outer_var = "I am from outer function scope variable"

    def inner_func():
        print(outer_var)  # Python finds outer_var in the enclosing scope

    inner_func()


outer_function()


# GLobal scope
# the variable that define outside of all function is called global scope
# variable


global_var = 50


def access_global():
    print("Accessing global variable : ", global_var)


access_global()


# 4. Built-in Scope
# This is the widest scope in Python. It contains names of built-in functions and objects like print(), len(), sum(), list, etc. These are available everywhere without you needing to define them.

# local Vs global reading and assignment
company_name = "Abc Store"


def display():
    '''
    This function will not modify the global varibal, instead it create
    own local variable of company_name

    '''
    company_name = "kc group"
    company_tag = "Pvt Ltd"
    full_company_name = " ".join([company_name, company_tag])
    print(f"Full company name: {full_company_name}")


display()


def change_global():
    '''
    This function will modify global variable value for the we have to
    use global keyboard
    '''
    global company_name
    company_tag = "Pvt Ltd"
    full_company_name = " ".join([company_name, company_tag])
    print(full_company_name)


change_global()
