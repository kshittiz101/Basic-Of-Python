# railway ticket info system
ticket_type = input(
    "Enter your seat type (sleeper, ac, general, luxury ): ").lower().strip()


def get_seat_info(ticket_type):
    match ticket_type:
        case "sleeper":
            return f"You  ticket type is {ticket_type}, you have got bed only"
        case "ac":
            return f"You  ticket type is {ticket_type}, you have got ac and bed"

        case "general":
            return f"You  ticket type is {ticket_type}, you have no ac and no bed"
        case "luxury":
            return f"You  ticket type is {ticket_type}, you have got ac, luxury bed and tv"
        case _:
            return "There no such seat avaiable"


# calling a function
seat_info = get_seat_info(ticket_type=ticket_type)
print(seat_info)
