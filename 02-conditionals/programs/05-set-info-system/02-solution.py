# poslish code: give what type of value does function return


ticket_type = input(
    "Enter your seat type (sleeper, ac, general, luxury): ").lower().strip()


def get_seat_info(t_type: str) -> str:
    match t_type:
        case "sleeper":
            return f"{t_type}: bed provided"
        case "ac":
            return f"{t_type}: AC coach + bed"
        case "general":
            return f"{t_type}: non-AC sitting, no bed"
        case "luxury":
            return f"{t_type}: AC, luxury bed, TV"
        case _:
            return "Invalid seat type"


print(get_seat_info(ticket_type))
