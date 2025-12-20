available_items_in_cafe = ['coffee', 'tea', 'juice']
user_request = input("Place your order  (coffee, tea, juice): ").lower()

# here we are using membership check in list
if user_request in available_items_in_cafe:
    print("your order is placed")
else:
    print("sorry we don't have that item")
