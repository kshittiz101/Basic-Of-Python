# Problem: Chai Flavor Inventory Checker

## Description
You manage a chai tea inventory system. Each day, you process a list of requested flavors. Some flavors may be temporarily **"Out of Stock"**—these should be skipped. However, if you encounter a **"Discontinued"** flavor, you must **immediately stop** processing any further requests for safety and compliance reasons.

Your task is to process the list sequentially, printing only the available flavors that can be served.

## Input
- The first line contains an integer `n` (1 ≤ n ≤ 100), the number of flavors.
- The next `n` lines each contain a string representing a flavor status or name.

## Output
Print each **available** flavor on its own line. Stop processing immediately after encountering a "Discontinued" flavor (do not print "Discontinued" itself or any flavors after it).

## Sample Input
```
6
Vanilla
Out of Stock
Spice
Discontinued
Ginger
Cardamom
```

## Sample Output
```
Vanilla
Spice
```

## Explanation
1. "Vanilla" → printed (available)
2. "Out of Stock" → skipped with `continue`
3. "Spice" → printed (available)
4. "Discontinued" → triggers `break`, ending the loop immediately
5. "Ginger" and "Cardamom" are never processed

## Constraints
- `n` is a positive integer ≤ 100
- Each flavor string contains only letters and spaces
- Exactly two special status strings exist: `"Out of Stock"` and `"Discontinued"`

## Notes
You **must** use a `continue` statement to skip out-of-stock items and a `break` statement to exit when encountering a discontinued flavor.