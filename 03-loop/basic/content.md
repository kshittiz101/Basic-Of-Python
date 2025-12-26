# Python Loops
## 1. What Are Loops?
A loop is a control flow structure that repeats a block of code until a certain condition is met. Instead of writing the same line 10 times, you write it once and let the loop handle the repetition.

## when to use loop ? 
- Repeat code multiple times automatically
- Iterate over a sequence (list, string, range)
- Process items one-by-one without manual repetition
- Run until a condition is met

## Types of Loops
### **for Loop**
Use when you know how many times to iterate
Iterates over a sequence (range, list, string)
Example: for i in range(10):

### **While Loop**
Use when you don't know the count upfront
Runs while a condition is true
Example: while user_input != "quit":


## Python `range()` Function

Generates a sequence of numbers, commonly used with `for` loops.

### Syntax
- `range(stop)` → 0 to stop-1
- `range(start, stop)` → start to stop -1
- `range(start, stop, step)` → start to stop-1, skipping by step

### Key Points
- **Stops before the end value** (exclusive)
- **Default start is 0**
- **Default step is 1**
- **Memory efficient**: generates numbers on-the-fly

### Examples
```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8
range(5, 0, -1) # 5, 4, 3, 2, 1 (countdown)
```


# what is enumerate ? 
enumerate() is a buit-in function in python that lets you loop over something and get bot index (postion) and the value at the same time. 

## when to use it
You should use enumerate() in Python whenever you need BOTH:
- the index (position)
- and the value (item) while looping through something.

Example:
```
names = ["Ali", "Sara", "John"]

for i, name in enumerate(names):
    print(f"{i}: {name}")
```

---

# Python `zip()` Function Learning Notes

## Definition
`zip()` aggregates multiple iterables (lists, tuples, etc.) **in parallel**, returning an iterator of tuples where each tuple contains **corresponding elements** from each iterable.

## Core Use Cases
- Simultaneously iterating over **multiple sequences** (most common)
- **Pairing** related data (e.g., names and scores)
- Quickly **building dictionaries** (with `dict()`)
- **Matrix transposition** (with `*` unpacking)

## Basic Syntax
```python
zip(*iterables)  # Returns an iterator
```

## Example Code
```python
# 1. Basic usage: Parallel iteration over two lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Output:
# Alice: 85
# Bob: 92
# Charlie: 78

# 2. Handling different lengths: Stops at the shortest
list(zip([1, 2], ['a', 'b', 'c']))  # [(1, 'a'), (2, 'b')]

# 3. Building a dictionary
keys = ['name', 'age', 'city']
values = ['Tom', 25, 'Beijing']
person = dict(zip(keys, values))
# {'name': 'Tom', 'age': 25, 'city': 'Beijing'}

# 4. Matrix transposition
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = list(zip(*matrix))  # [(1, 4), (2, 5), (3, 6)]
```

## Key Points
- **Lazy evaluation**: Returns an iterator; use `list()` to view contents
- **Length mismatch**: Automatically truncates to the **shortest** iterable (Python 3.10+ can use `itertools.zip_longest()` for padding)
- **Empty inputs**: Result is empty if any input is empty
- Often used with `enumerate`: `for i, (a, b) in enumerate(zip(list1, list2)):`