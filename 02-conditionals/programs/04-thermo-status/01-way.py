# Step 1: Take input
device_status_input = input(
    "Enter Device status (T for true and F for false): "
).lower()
room_temperature = float(input("Enter room temperature (Celsius): "))


def check_device_status(status):
    """
    Returns True/False based on device status input.
    Returns None if input is invalid.
    """
    device_status_rules = {
        't': True,
        'f': False
    }
    return device_status_rules.get(status)  # returns None if key not found


# Call the function once
device_active = check_device_status(device_status_input)

if device_active is None:
    print("Invalid device input")
elif not device_active:
    print("Device is not active")
else:
    # Device is active, check temperature
    if room_temperature > 35:
        print("Critical Alert: Temperature too high")
    elif 26 <= room_temperature <= 35:
        print("Warning: Temperature is high")
    elif 10 <= room_temperature < 26:
        print("Temperature is normal")
    else:
        print("Warning: Temperature too low")
