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
