ticket_type = input(
    "Enter your seat type (sleeper, ac, general, luxury): ").lower().strip()

SEAT_FEATURES = {
    "sleeper": "bed provided",
    "ac": "AC coach + bed",
    "general": "non-AC sitting, no bed",
    "luxury": "AC, luxury bed, TV"
}

print(SEAT_FEATURES.get(ticket_type, "Invalid seat type"))
