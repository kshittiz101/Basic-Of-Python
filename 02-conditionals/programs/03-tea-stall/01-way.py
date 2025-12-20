price_base_on_cup_sized = {
    'small': 10,
    'medium': 20,
    'large': 30
}

user_order = input(
    "Enter the cup size (Small, Medium, Large)  you want: "
).lower()

if user_order in price_base_on_cup_sized:
    print(f"You have to pay: {price_base_on_cup_sized[user_order]}")

else:
    print("Invalid inputs or order")
