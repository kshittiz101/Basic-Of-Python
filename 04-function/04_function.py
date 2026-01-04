# how to handle to many return in python


# def discount_cal(original_price, discount_rate):
#     discount_amt = original_price * discount_rate / 100
#     final_price = original_price - discount_amt
#     return original_price, final_price


# original_price, discount_amt = discount_cal(100, 10)
# print(f"Original Price {original_price}")
# print(f"Discount Price {discount_amt}")


def discount_cal(original_price, discount_rate):
    discount_amt = original_price - (original_price * discount_rate / 100)
    return original_price, discount_amt


original_price, discount_amt = discount_cal(100, 10)

print(f"Original Price {original_price}")
print(f"Discount Price {discount_amt}")
