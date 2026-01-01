In Python, a **function** is a block of reusable code that performs a specific task. Functions help you organize your code, make it readable, and avoid repetition.

Here is a complete guide on how to use them.

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
