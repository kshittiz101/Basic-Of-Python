# In this approch we will create a function a reusable code, to get price according to the cup sized

price_base_on_cup_sized = {
    'small': 10,
    'medium': 20,
    'large': 30
}


def get_price(cup_size):
    ''' 
    this function will return cup price according to its sizes
    '''
    return price_base_on_cup_sized.get(cup_size)


customer_order = input("Enter your order: ").lower()
price = get_price(customer_order)

if price is not None:
    print(f"You have to pay: {price}")
else:
    print("Invalid input or order")
