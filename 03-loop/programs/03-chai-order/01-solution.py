from typing import Iterable


def display_chai_name(list_of_chai: Iterable[str]) -> list[str]:
    """
    Take the list of chai and generate message according to the 
    name of chai

    Arg:
    list_of_chai: list of string with chai name

    Returns:
    list of string with message
    """

    message = []

    for chai in list_of_chai:
        message.append(f"Order ready for [{chai}]")
    return message


CHAI_LIST = ["black tea", "milk tea", "Masala Chai"]


def main():
    """Main function to display chai orders"""
    ready_chai_orders = display_chai_name(CHAI_LIST)
    for order in ready_chai_orders:
        print(order)


if __name__ == "__main__":
    main()
