
# this import the greet module from utils package not the
# function it self you have call it like greet.function_name
from utils import greet

# importing specific function from business package
from business.business import get_business_areas


if __name__ == "__main__":
    username = "Kc"
    message = greet.message(username)
    print(message)

    areas = get_business_areas()
    print("Business Areas:", areas)
