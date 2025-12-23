## What `if __name__ == "__main__":` Means

This is Python's way of checking if a file is being **run directly** (as a script) vs. **imported** as a module.

### How it Works
- **`__name__`** is a special built-in variable
- When Python runs a file **directly**, `__name__` is set to `"__main__"`
- When a file is **imported**, `__name__` is set to the module name (e.g., `"my_module"`)

### What it Does
```python
if __name__ == "__main__":
    main()  # Only runs when script is executed directly
```

### Why It's Useful

**Scenario:** You have `tea_shop.py`

```python
# tea_shop.py
def serve_tea():
    print("Serving tea...")

def main():
    serve_tea()

if __name__ == "__main__":
    main()
```

- **Run directly:** `python tea_shop.py` → Prints "Serving tea..."
- **Import as module:** `import tea_shop` → **Nothing prints** (main() doesn't run automatically)

**Without this check,** importing would accidentally execute code, which is bad for reusable modules.