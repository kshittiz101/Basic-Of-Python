# Python Functions: Complete Guide

In Python, a **function** is a block of reusable code that performs a specific task. Functions help you organize your code, make it readable, and avoid repetition.

## 1. When to Use a Function

Functions are a fundamental building block in programming. You should use a function:

1.  **To reuse code:** When you have a block of code that needs to be executed multiple times in different parts of your program.
2.  **To improve readability:** When you want to divide a large, complex problem into smaller, manageable, and logical parts. This makes the code easier to debug and maintain.

---

## 2. Defining and Calling a Function

### Defining a Function

A function is defined using the `def` keyword followed by the function name and parentheses.

```python
def greeting():
    """Optional docstring describing the function."""
    print("Good morning")
```

### Calling a Function

Defining a function does not execute it. You must **call** the function by its name followed by parentheses to run the code inside it.

```python
greeting()  # This executes the print statement
```

---

## 3. Types of Functions

Functions can be categorized based on whether they accept **Parameters** (input) and whether they return a **Value** (output).

### Type 1: Function without Parameters and without Return Type

These functions perform a specific task (like printing) but do not accept any input data and do not give any value back to the caller.

```python
def welcome_message():
    '''
    This function is an example of a function
    without parameters and without return type
    '''
    print("Welcome to our store!")

# Calling the function
welcome_message()
```

---

### Type 2: Function with Parameters and without Return Type

These functions accept input (parameters) to perform a task, but they still perform an action (like printing) rather than returning a value.

```python
def greet_user(name):
    '''
    This function is an example of a function
    with parameters and without return type
    '''
    print(f"Hello, {name}! Welcome to our store.")

# Calling the function with an argument
greet_user("Ram")
```

---

### Type 3: Function without Parameters and with Return Type

These functions do not need any input to do their work, but they process something and **return** a result back to the caller. The result can be stored in a variable.

```python
def get_store_name():
    '''
    This function is an example of a function
    without parameters and with return type
    '''
    return "SuperMart"

# Storing the returned value in a variable
store_name = get_store_name()
print(f"Store Name: {store_name}")
```

---

### Type 4: Function with Parameters and with Return Type

This is the most versatile type. It accepts input data, processes it, and returns a result. This allows the function to be used in calculations or further logic.

```python
def get_greeting_message(name):
    '''
    This function is an example of a function
    with parameters and with return type
    '''
    return f"Hello, {name}! Welcome to our store."

# Calling the function and storing the returned string
greeting_msg = get_greeting_message("Harry")
print(greeting_msg)
```

### 1. Defining a Function

You use the `def` keyword to define a function, followed by the function name and parentheses `()`.

```python
def my_function():
    print("Hello from a function!")
```

### 2. Calling a Function

To execute the code inside a function, you need to **call** it by its name followed by parentheses.

```python
def my_function():
    print("Hello from a function!")

# Call the function
my_function()
# Output: Hello from a function!
```

---

### 3. Parameters (Arguments)

You can pass data into a function using parameters. These act as variables inside the function.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output: Hello, Alice!

greet("Bob")
# Output: Hello, Bob!
```

### 4. Return Values

Functions can send data back to the caller using the `return` keyword. If you don't use `return`, the function returns `None` by default.

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)
# Output: 8
```

---

### 5. Default Parameters

You can set a default value for a parameter. If the caller doesn't provide an argument, the default value is used.

```python
def power(base, exponent=2):
    return base ** exponent

print(power(4))      # Output: 16 (uses default exponent 2)
print(power(4, 3))   # Output: 64 (uses provided exponent 3)
```

---

### 6. Lambda Functions (Anonymous Functions)

Python allows you to create small, one-line functions without a name using `lambda`. They are useful for short, throwaway functions.

```python
multiply = lambda x, y: x * y

print(multiply(10, 5))
# Output: 50
```

---

### Summary Structure

Here is the anatomy of a Python function:

```python
def function_name(param1, param2=default_value):  # 1. Definition
    """Optional docstring describing the function.""" # 2. Description
    # Code block
    result = param1 + param2
    return result  # 3. Output
```
