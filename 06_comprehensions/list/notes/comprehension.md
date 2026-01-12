

**Python Comprehensions** are a concise way to create collections (lists, dictionaries, sets) using a single line of code. They are often faster and more readable than using traditional `for` loops.

There are four main types:
1.  **List Comprehension**
2.  **Dictionary Comprehension**
3.  **Set Comprehension**
4.  **Generator Expression**

---

### 1. List Comprehension
Creates a new list based on an existing iterable (like a list, tuple, or range).

**Syntax:**
```python
[expression for item in iterable if condition]
```

**Example A: Basic Loop**
*Create a list of squares:*

**Traditional Loop:**
```python
squares = []
for x in range(10):
    squares.append(x**2)
```

**List Comprehension:**
```python
squares = [x**2 for x in range(10)]
# Result: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**Example B: With Condition (Filtering)**
*Get only even squares:*

```python
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# Result: [0, 4, 16, 36, 64]
```

**Example C: With `if-else` (Value Modification)**
*Note: The `if` comes *after* the loop when filtering, but the `if-else` comes *before* the loop when modifying values.*

```python
# If x is even, square it; otherwise, keep x as is
result = [x**2 if x % 2 == 0 else x for x in range(5)]
# Result: [0, 1, 4, 3, 16]
```

When to Use List Comprehension
You should use list comprehension when you need to create a new list based on an existing iterable, and the logic is simple and readable.

## ✅ USE it when:

**Transforming data:** Applying the same operation to every item (e.g., converting strings to lowercase, squaring numbers).
Filtering data: Selecting specific items that meet a condition (e.g., all even numbers, names starting with 'A').

**Conciseness matters:** You want to replace a simple 3-line for loop with a readable one-liner.

**Performance is key:** List comprehensions are generally faster than standard for loops because the iteration is performed at C-level speed inside the Python interpreter.

---

## ❌ DO NOT use it when:

**The logic is complex:** If your comprehension requires nested loops, multiple if/else statements, or function calls that make the line wider than 80-100 characters. Standard loops are more readable here.

**You need side effects:** If the main goal is to print something, write to a file, or update a database, use a standard for loop. Comprehensions are for creating lists, not performing actions.

**Memory is a concern:** If you are generating millions of items and only need to iterate over them once (e.g., passing to a sum() function), use a Generator Expression (using parentheses ()) instead.


---

### 2. Dictionary Comprehension
Creates a new dictionary. Similar to list comprehensions but uses curly braces `{}` and requires a key:value pair.

**Syntax:**
```python
{key: value for item in iterable}
```

**Example: Create a number mapping**

```python
# Traditional way
numbers = {1: "one", 2: "two"}
# Let's swap keys and values
swapped = {}
for k, v in numbers.items():
    swapped[v] = k

# Dictionary Comprehension
swapped = {v: k for k, v in numbers.items()}
# Result: {'one': 1, 'two': 2}
```

**Example: Creating a lookup table**
```python
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
# Result: {'Alice': 5, 'Bob': 3, 'Charlie': 7}
```

---

### 3. Set Comprehension
Creates a new set. Remember, sets cannot contain duplicates. It also uses curly braces `{}` but without a key:value pair.

**Syntax:**
```python
{expression for item in iterable}
```

**Example: Find unique lengths of words**

```python
words = ["apple", "banana", "cherry", "date", "fig"]
unique_lengths = {len(word) for word in words}
# Result: {5, 6, 3, 4}
# Note: If two words had the same length, it would only appear once.
```

---

### 4. Generator Expressions
These look exactly like list comprehensions but use parentheses `()` instead of brackets `[]`.

**Key Difference:**
*   **List Comprehension:** Creates the entire list in memory at once.
*   **Generator Expression:** Creates an object that generates items one by one on demand (lazy evaluation). It is much more memory efficient for large datasets.

**Example:**

```python
# Summing squares of 1 million numbers
# List Comp (Creates a huge list in RAM first):
sum([x**2 for x in range(1000000)]) 

# Generator (Calculates one number at a time, passes to sum, then discards):
sum(x**2 for x in range(1000000))
```

---

### Nested Comprehensions
You can nest loops inside a comprehension.

**Flattening a Matrix (2D List):**
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened = [num for row in matrix for num in row]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

*Tip: If the nesting gets too complex, it is usually better to go back to standard `for` loops for readability.*

---

### Summary Table

| Type | Brackets | Syntax Structure | Returns |
| :--- | :--- | :--- | :--- |
| **List** | `[]` | `[x for x in i]` | List |
| **Dict** | `{}` | `{k:v for x in i}` | Dictionary |
| **Set** | `{}` | `{x for x in i}` | Set |
| **Gen** | `()` | `(x for x in i)` | Generator Object |

### Best Practice
The "Zen of Python" states: *"Readability counts."*
While comprehensions are cool, avoid writing "one-liners" that are too long or complicated. If your comprehension spans multiple lines or requires triple nesting, use a standard loop.