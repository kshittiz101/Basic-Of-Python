
# 1. List in python
Ordered, **mutable** collection of arbitrary objects, written with brackets.

```python
nums = [7, 11, 42]
mixed = [1, "chai", 3.14, True]
nested = [[1, 2], [3, 4]]
```

## 2. Core ops (big-O in comments)
```python
len(lst)          # O(1)  size
lst.append(x)     # O(1)  add to tail
lst.insert(i, x)  # O(n)  add at index
lst.pop()         # O(1)  remove & return tail
lst.pop(i)        # O(n)  remove at index
lst[i]            # O(1)  read / write by index
lst[i:j]          # O(k)  slice (k = size of slice)
x in lst          # O(n)  membership
lst.sort()        # O(n log n)  in place
sorted(lst)       # O(n log n)  returns new list
lst.reverse()     # O(n)  in place
```

## 3. Creating
```python
empty = []
zeros = [0] * 10              # [0,0,…,0]
range_list = list(range(5))   # [0,1,2,3,4]
comp = [x**2 for x in range(6) if x % 2 == 0]  # [0, 4, 16]
```

## 4. Reading items
```python
first  = lst[0]      # leftmost
last   = lst[-1]     # rightmost
sub    = lst[1:4]    # slice: positions 1,2,3
step   = lst[::2]    # every 2nd item
rev    = lst[::-1]   # reversed copy
```

## 5. Updating
```python
lst[2] = 99                # mutate in place
lst[1:3] = ['a', 'b', 'c'] # replace stretch
```

## 6. Insert / Delete
```python
lst.insert(0, "head")   # prepend
lst.append("tail")      # append
lst.extend(other)       # concat in place
del lst[3]              # delete by index
lst.remove("val")       # delete 1st occurrence
lst.pop()               # pop last
```

## 7. Utilities
```python
lst.count(x)            # occurrences
lst.index(x)            # position (ValueError if missing)
lst.copy()              # shallow copy
lst.clear()             # remove all
```

## 8. Sort & order
```python
lst.sort(key=str.lower, reverse=False)  # stable in place
new = sorted(lst, key=lambda x: x.price)  # out-of-place
```

## 9. Stack / Queue idioms
```python
stack = []; stack.append(x); x = stack.pop()           # LIFO
queue = collections.deque(); queue.append(x); x=queue.popleft()  # FIFO
```

## 10. Gotchas
- **Mutable**: aliasing changes visible through every reference.  
  ```python
  a = [1, 2]; b = a; a.append(3)  # b sees [1,2,3]
  ```
  Clone first: `b = a.copy()` or `b = a[:]`.

- **Never use `list` as a variable name** – shadows built-in.

- Membership (`in`) is linear; convert to `set`/`dict` for heavy look-ups.

## 11. Quick cheat
| Task | One-liner |
|---|---|
| flatten 2-D | `[item for row in matrix for item in row]` |
| dedupe keep order | `list(dict.fromkeys(lst))` |
| random item | `import random; random.choice(lst)` |
| enumerate (index, value) | `for i, v in enumerate(lst, start=1):` |

Keep this sheet handy; lists are the workhorse of everyday Python.