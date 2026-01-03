In Python, **scope** refers to the region of a program where a particular variable, function, or object is accessible and recognized.

Python determines the visibility of a variable using the **LEGB Rule**. This rule defines the order in which Python looks for variable names.

---

### The LEGB Rule

When you reference a variable in your code, Python searches for it in the following order:

1.  **L: Local**
2.  **E: Enclosing**
3.  **G: Global**
4.  **B: Built-in**

If the variable is not found in any of these scopes, Python raises a `NameError`.

---

### 1. Local Scope

Variables defined **inside a function** belong to the local scope.

- They are created when the function is called and destroyed when the function exits.
- They are **only accessible within that function**.

```python
def my_function():
    x = 10  # Local variable
    print(x)

my_function()
# print(x)  <-- This would raise an error because x is local to my_function
```

### 2. Enclosing (Non-local) Scope

This scope only exists for **nested functions** (functions defined inside other functions).

- If a variable is not found in the local scope of the inner function, Python looks in the enclosing function's scope.

```python
def outer_func():
    y = 20  # Enclosing variable

    def inner_func():
        print(y)  # Python finds 'y' in the enclosing scope

    inner_func()

outer_func()
```

### 3. Global Scope

Variables defined **outside of all functions** belong to the global scope.

- They can be accessed from anywhere in the code, including inside functions (to read them).

```python
z = 30  # Global variable

def my_func():
    print(z)  # Accessing global variable

my_func()
print(z) # Also accessible here
```

### 4. Built-in Scope

This is the widest scope in Python. It contains names of built-in functions and objects like `print()`, `len()`, `sum()`, `list`, etc. These are available everywhere without you needing to define them.

---

### Important Interaction: `global` and `nonlocal`

There is a critical distinction between **reading** a variable and **modifying** it.

#### Reading vs. Assignment

If you try to assign a value to a variable inside a function, Python automatically treats it as a **Local** variable, even if a global variable with the same name exists.

```python
x = 5  # Global

def change_x():
    x = 10 # Creates a NEW local variable 'x', doesn't change global 'x'
    print("Inside function:", x)

change_x()
print("Outside function:", x) # Still 5
```

#### The `global` keyword

If you want to **modify** a global variable inside a function, you must use the `global` keyword.

```python
x = 5

def change_x():
    global x
    x = 10 # Modifies the global variable
    print("Inside function:", x)

change_x()
print("Outside function:", x) # Now 10
```

#### The `nonlocal` keyword

If you have nested functions and want to modify a variable in the **Enclosing** scope (not the global scope), use `nonlocal`.

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1 # Modifies 'count' from the outer function
        return count

    return inner

counter = outer()
print(counter()) # Output: 1
print(counter()) # Output: 2
```

---

### Summary Visual

```python
# B: Built-in (e.g., print)
z = 5  # G: Global

def outer():
    y = 10 # E: Enclosing

    def inner():
        x = 15 # L: Local
        print(x, y, z)

    inner()

outer()
```
