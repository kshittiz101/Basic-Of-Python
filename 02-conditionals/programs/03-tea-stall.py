# A tea stall offer different prices for the different sizes of the cups
# write a programs that calculate price base on sizes
# task:
# input: "small", "medium", "large"
# small - 10, medium - 20, large: 30
# other inputs show invalid inputs

price_base_on_cup_sized = {
    'small': 10,
    'medium': 20,
    'large': 30
}

user_order = input("Enter the cup size you want: ").lower()

if user_order in price_base_on_cup_sized:
    print(f"You have to pay: {price_base_on_cup_sized[user_order]}")

else:
    print("Invalid inputs or order")


#  others ways create function and avoid in operations
def get_price(cup_size):
    return price_base_on_cup_sized.get(cup_size)


customer_order = input("Enter your order: ").lower()
price = get_price(customer_order)

if price is not None:
    print(f"You have to pay: {price}")
else:
    print("Invalid input or order")


# with get it is more professional way of writing code
price_base_on_cup_size = {
    'small': 10,
    'medium': 20,
    'large': 30
}

user_order = input("Enter the cup size you want: ").lower()

price = price_base_on_cup_size.get(user_order)

if price:
    print(f"You have to pay: {price}")
else:
    print("Invalid input or order")
