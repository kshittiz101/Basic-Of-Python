CHAI_MENU = ["Masala Chai", "Ginger Chai", "Elaichi Chai", "Green Tea"]


def display_chai_menu(chai_list):
    for idx, chai in enumerate(chai_list, start=1):
        print(f"{idx}. {chai}")


display_chai_menu(CHAI_MENU)

try:
    user_order = int(input("Enter your order: "))

    if 1 <= user_order <= len(CHAI_MENU):
        print(f"You selected: {CHAI_MENU[user_order - 1]}")
    else:
        print("Invalid number")

except ValueError:
    print("Please enter a valid number")
