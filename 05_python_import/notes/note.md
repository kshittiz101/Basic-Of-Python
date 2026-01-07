### 1. The Two Ways to Import Inside a Function

There are two main ways to import inside a function in Python. They behave slightly differently regarding how you access the code.

#### Method A: Importing the whole module

This imports the module file. You must use the module name as a prefix to use the functions inside it.

```python
def process_data():
    # Import the whole 'math' module
    import math

    # You must type 'math.' before the function name
    result = math.sqrt(100)
    print(result)

process_data()
```

#### Method B: Importing specific objects (functions/classes) directly

This pulls specific functions or classes out of the module into your local scope. You do **not** need the prefix.

```python
def process_data():
    # Import ONLY the sqrt function directly
    from math import sqrt

    # You can use sqrt directly without 'math.'
    result = sqrt(100)
    print(result)

process_data()
```

---

### 2. Scope: The "Invisible Bubble"

This is the most important concept in Python to understand here.

When you import inside a function, the imported function or object is **Local**. It only exists inside that specific function while the function is running.

**Example of the limitation:**

```python
def my_function():
    from math import pi # 'pi' is created here

    print(pi) # This works (3.1415...)

my_function()

# print(pi)  <-- This would CRASH
# Error: NameError: name 'pi' is not defined
```

Once `my_function()` finishes running, Python deletes `pi` from memory to save space. You cannot access it from anywhere else.

---

### 3. Performance: Is it slow?

Many beginners worry that importing inside a function makes the code slow because "it has to load the file every time."

**It is NOT slow.**

Python has a built-in system called **Module Caching**.

1.  The **first time** you call the function, Python finds the file, reads it, and loads it into memory (`sys.modules`).
2.  The **second time** you call the function, Python sees the module is already loaded in memory and skips the loading process. It effectively just creates a pointer to the existing code.

**The only actual overhead** is the time it takes Python to look up the name in the cache, which is measured in nanoseconds.

---

### 4. The Best Use Case: Solving "Circular Imports"

This is the #1 reason professional Python developers import inside functions.

**The Problem:**
Imagine you have two files:

- `file_a.py` imports `file_b`
- `file_b.py` imports `file_a`

If you put imports at the top of both files, Python enters an infinite loop (A needs B, but B needs A to finish starting first). The program crashes.

**The Solution:**
Move one of the imports inside a function.

```python
# file_b.py
def do_something():
    # This import only runs when do_something() is called
    # By this time, file_a is fully loaded, so no crash happens.
    import file_a

    file_a.helper_function()
```

### 5. Summary Checklist

| Feature           | Import at Top (Global)                                         | Import Inside Function (Local)                                                                                            |
| :---------------- | :------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| **Availability**  | Available everywhere in the file.                              | Available **only** inside that function.                                                                                  |
| **Usage Style**   | `import math` then `math.sqrt()`                               | `from math import sqrt` then `sqrt()`                                                                                     |
| **Performance**   | Loaded once at startup.                                        | Loaded on first call, then cached.                                                                                        |
| **Best Practice** | **Do this 95% of the time.** It is cleaner and easier to read. | **Do this only** to fix Circular Imports or to delay loading a massive library (like Pandas/PyTorch) that is rarely used. |

**Recommendation:**
Unless you have a specific reason (like a Circular Import), keep your imports at the **top of your Python file**. It makes your code easier to read and debug because you can see all dependencies at a glance.
