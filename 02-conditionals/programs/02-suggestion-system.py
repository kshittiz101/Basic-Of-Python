# a local cafe wants a suggestion system based on the products they have
# if user ask for coffer, tea, juice it should confirm the order
#  if user as for anything else it should say "sorry we don't have that item"

available_items_in_cafe = ['coffee', 'tea', 'juice']
user_request = input("Place your order: ").lower()


# here we are using membership check in list
if user_request in available_items_in_cafe:
    print("your order is placed")
else:
    print("sorry we don't have that item")
