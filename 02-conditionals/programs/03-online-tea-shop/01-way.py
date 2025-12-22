# Tea Store Delivery Fee Challenge
# The ternary operator in Python perform conditional checks and assign
# values or execute expressions in a single line.
# It is also known as a conditional expression because it evaluates a condition
# and returns one value if the condition is True and another if it is False.

# syntax:
# value_if_true if condition else value_if_false


# Feedbacks

# Printing inside the ternary ties the logic to I/O and makes the value impossible to use later.
# Better practice: compute the fee, then decide what to do with it.
order_amount = 400
print("Delivery Is Free") if order_amount > 300 else print(
    "Delivery Costs is Rs. 30")


# better pratice for above program
order_price = int(input("Enter your order amount : "))
print(f"order price is {order_price}, type of input is {type(order_price)}")


# calculate delivery fee
delivery_fee = 0 if order_price > 300 else 30
print(delivery_fee)

print("Delivery is Free " if delivery_fee ==
      0 else f"Delivery price is: {delivery_fee}")
