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
