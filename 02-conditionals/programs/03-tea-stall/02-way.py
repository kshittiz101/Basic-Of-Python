#  others ways create function and avoid in operations

price_base_on_cup_sized = {
    'small': 10,
    'medium': 20,
    'large': 30
}


def get_price(cup_size):
    return price_base_on_cup_sized.get(cup_size)


customer_order = input("Enter your order: ").lower()
price = get_price(customer_order)

if price is not None:
    print(f"You have to pay: {price}")
else:
    print("Invalid input or order")
