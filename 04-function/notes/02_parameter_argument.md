# Python Functions: Advanced Parameters & Arguments

## 1. Parameters vs. Arguments

It is important to distinguish between these two terms, though they are often used interchangeably in casual conversation.

- **Parameters:** These are the variables listed inside the parentheses in the **function definition**. They act as placeholders for the data the function expects to receive.
- **Arguments:** These are the actual values passed to the function when it is **called**.

**Example:**

```python
# 'name' is a PARAMETER (placeholder)
def greet_user(name):
    print(f"Hello, {name}!")

# "Alice" is an ARGUMENT (actual value)
greet_user("Alice")
```

---

## 2. Types of Arguments

When calling a function in Python, there are two main ways to pass arguments: **Positional** and **Keyword**.

### Positional Arguments

In positional arguments, the order in which you pass the arguments matters. The first argument is assigned to the first parameter, the second to the second, and so on.

```python
def personal_info(name, age, city):
    return f"Name: {name}, Age: {age}, City: {city}"

# Calling the function with positional arguments
# Order matters: "Alice" -> name, 30 -> age, "New York" -> city
positional_example = personal_info("Alice", 30, "New York")
print(f"Positional Argument: {positional_example}")
```

### Keyword Arguments

In keyword arguments, you explicitly specify the parameter name along with the value using the `parameter_name=value` syntax. **The order does not matter** here because Python knows exactly which value goes to which parameter.

```python
# Calling the function with keyword arguments
# Order does not matter
keyword_example = personal_info(age=25, city="Los Angeles", name="Bob")
print(f"Keyword Argument: {keyword_example}")
```

---

## 3. Default Parameters

We should use **default parameters** in Python when you want a function to work even if the caller doesn't provide a value for that specific argument. It allows you to make a function more flexible while keeping the code simple.

Here are the most common scenarios where default parameters are useful:

### 1. Providing Common "Default" Settings

This is the most frequent use case. If a function usually uses a specific value (like a standard size, color, or setting) but occasionally needs to change it, use a default parameter. This saves the user from typing the same value every time.

**Scenario:** Calculating the total price of items. Most of the time, the tax rate is fixed (e.g., 10%), so you shouldn't have to type `0.10` every single time.

```python
def calculate_price(price, tax_rate=0.10):
    return price + (price * tax_rate)

# Most of the time, you just pass the price (uses default 10% tax)
print(calculate_price(100))  # Output: 110.0

# Occasionally, you need a different tax rate
print(calculate_price(100, 0.18))  # Output: 118.0
```

### 2. Making Arguments Optional (Flagging)

Sometimes a function has a main feature and a secondary "extra" feature (like a verbose output or a specific debug mode). You can use a default boolean parameter to turn these features on or off.

**Scenario:** A function that sends an email. Usually, you just want to send it. But sometimes you want to save a copy to the drafts folder as well.

```python
def send_email(message, save_copy=False):
    print(f"Sending message: {message}")
    if save_copy:
        print("Saving a copy to drafts.")

# Normal usage (doesn't save copy)
send_email("Meeting at 5 PM")

# Special usage (saves copy)
send_email("Meeting at 5 PM", save_copy=True)
```

### 3. Handling User Input (Database/API Fields)

When saving data to a database or sending data to an API, some fields might be mandatory (like `username`) while others are optional (like `profile_picture` or `bio`).

**Scenario:** Creating a user profile. A user _must_ have a name, but the bio is optional.

```python
def create_user(username, bio="No bio provided"):
    print(f"Creating user: {username}")
    print(f"Bio: {bio}")

# User provides a bio
create_user("Alice", "I love Python!")

# User skips the bio (uses default)
create_user("Bob")
```

### 4. Simplifying Complex Functions

If a function has many parameters, it can be annoying to call it if you only care about the first one. Default parameters let you skip the ones you don't need.

**Scenario:** Connecting to a server. You usually connect to the local IP (`127.0.0.1`) on the standard port (`8080`).

```python
def connect_to_server(ip="127.0.0.1", port=8080):
    print(f"Connecting to {ip} on port {port}...")

# Quick connection (uses defaults)
connect_to_server()

# Specific connection (overrides defaults)
connect_to_server(ip="192.168.1.5", port=9000)
```

### Summary: When to use them?

Use a default parameter when:

1.  The function works correctly without the user providing that specific value.
2.  There is a logical "standard" value that is used 80-90% of the time.
3.  You want to keep your function calls short and readable.
