initial_temp_of_water = 40


def temperature_tracker(initial_temp: int) -> None:
    """Tracks and prints temperature until boiling point."""
    # Creating a current_temp copy preserves the original parameter value(good practice)
    current_temp = initial_temp

    while current_temp < 100:
        print(current_temp)
        current_temp += 15

    # Print the final boiling temperature (>= 100)
    print(current_temp)


# Main execution
def main() -> None:
    temperature_tracker(initial_temp=initial_temp_of_water)


if __name__ == "__main__":
    main()
