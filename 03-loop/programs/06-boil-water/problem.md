# Problem: Tea Heating Simulation

## Description
You are simulating the process of heating a cup of tea. The tea starts at an initial temperature of **40°C** and will boil when it reaches or exceeds **100°C**. The temperature increases in fixed increments of **15°C** during each heating step. Your task is to track and display the temperature at each step until the tea boils.

## Input
There is no input for this problem. All parameters are fixed as described.

## Output
Print each temperature value on a separate line, starting from the initial temperature (40) and including every intermediate temperature after each increase. The final line should be the first temperature that is **greater than or equal to 100**.

## Constraints
- Initial temperature: 40
- Temperature increase per step: 15
- Boiling threshold: 100

## Sample Output
```
40
55
70
85
100
```

## Note
You **must** use a `while` loop to implement the heating simulation. The loop should continue as long as the current temperature is **strictly less than** 100. Ensure you print the temperature **before** each increment, including the initial temperature.