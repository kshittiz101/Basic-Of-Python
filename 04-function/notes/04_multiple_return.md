In Python, there are several ways to handle multiple return values, ranging from the simplest syntax to more structured approaches for complex data.

Here are the most common methods.

---

### 1. The Standard Way: Tuple Unpacking

Python does not actually return multiple values; it returns a single **tuple** containing the values. Python automatically "unpacks" this tuple when you assign it to variables.

**How to do it:**

```python
def calculate(x, y):
    sum_val = x + y
    product = x * y
    return sum_val, product  # Python wraps this as a tuple: (sum_val, product)

# Calling the function
result = calculate(5, 10)
print(result)  # Output: (15, 50)

# Unpacking into separate variables
s, p = calculate(5, 10)
print(s)  # Output: 15
print(p)  # Output: 50
```

**Best for:** Simple functions returning 2 or 3 related values (like coordinates, width/height, or a success flag/message).

---

### 2. The Readable Way: Returning a Dictionary

If you return many values, or if the order isn't obvious, using a dictionary makes your code much more readable. You don't have to remember which index corresponds to which value.

**How to do it:**

```python
def get_user(user_id):
    # logic to find user...
    return {
        "id": user_id,
        "name": "Alice",
        "email": "alice@example.com",
        "is_active": True
    }

user_data = get_user(101)
print(user_data['name'])  # Output: Alice
```

**Best for:** When you have 4+ return values or when the context of the data matters more than the order.

---

### 3. The Structured Way: Data Classes or NamedTuples

If you want the dot-access syntax of objects (like `result.name`) but don't want to create a full class manually, use `dataclasses` (Python 3.7+) or `namedtuple`.

**Using `dataclass`:**

```python
from dataclasses import dataclass

@dataclass
class CalculationResult:
    sum: int
    product: int
    average: float

def calculate(x, y):
    s = x + y
    p = x * y
    a = (x + y) / 2
    return CalculationResult(s, p, a)

res = calculate(10, 20)
print(res.sum)      # Output: 30
print(res.average)  # Output: 15.0
```

**Best for:** Larger applications where type hinting and code completion in IDEs (like VS Code or PyCharm) are important.

---

### 4. Handling "Ignore" Variables

Sometimes a function returns multiple values, but you only need one. You can use `_` to ignore the values you don't care about.

```python
def get_position():
    # logic...
    return 10, 20, 50  # x, y, z

# I only want x, ignore y and z
x, _, _ = get_position()
print(x)
```

---

### 5. Summary: Which one should I use?

| Method              | Syntax Example            | Use Case                                                               |
| :------------------ | :------------------------ | :--------------------------------------------------------------------- |
| **Tuple Unpacking** | `return a, b`             | Quick, simple returns (2-3 items).                                     |
| **Dictionary**      | `return {'a': a, 'b': b}` | Many items, or when names are important.                               |
| **Data Class**      | `return MyObj(a, b)`      | Large codebases, libraries, or when you need type hints.               |
| **List**            | `return [a, b]`           | When the data is a sequence of homogenous items (e.g., a list of IDs). |

### A Note on "Too Many" Returns

If you find yourself returning more than 4 or 5 values regularly, it is often a sign that your function is doing too much (violating the Single Responsibility Principle) or that those values belong together in their own custom **Class**.
