```markdown
# Tea Store Delivery Fee Challenge

## Scenario  
You operate an online tea store.  
- If the order amount is **greater than R300**, delivery is **free**.  
- Otherwise, delivery costs **R30**.

## Task  
Write a **single-line expression** that calculates the correct delivery fee using the **ternary operator**.

### Input  
```python
order_amount  # float or int, always ≥ 0
```

### Output  
Return the delivery fee as an `int`.

### Examples  
| Input | Output |
|-------|--------|
| 250   | 30     |
| 300   | 30     |
| 301   | 0      |

### Python Stub  
```python
delivery_fee = <write your ternary expression here>
```

### Constraints  
- Must use the ternary (`value_if_true if condition else value_if_false`) syntax.  
- No extra whitespace or semicolons.
```