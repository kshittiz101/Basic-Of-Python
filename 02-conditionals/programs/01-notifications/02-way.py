
# def weather_notification(temperature):
#     rules = [
#         (temperature > 30, "Hot weather"),
#         (15 <= temperature <= 30, "Normal weather"),
#         (temperature < 15, "Cold weather"),
#     ]

#     for condition, message in rules:
#         if condition:
#             return message


# print(weather_notification(45))


user_temp = 55


def weather_notification(temp):
    rules = [
        (temp >= 30, "Hot Weather"),
        (15 <= temp < 30, "Normal weather"),
        (temp < 15, "cold weather")
    ]

    for condition,  msg in rules:
        if condition:
            return msg


print(weather_notification(temp=user_temp))
