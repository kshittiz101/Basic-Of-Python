# ---------- configurable data ----------
CHAI_MENU = ["Masala Chai", "Ginger Chai", "Elaichi Chai", "Green Tea"]
PROMPT = "Enter your choice"
ERROR_NUM = "Invalid choice"
ERROR_TYPE = "Please enter a valid number"

# ---------- reusable helpers ----------


def display_chai_menu(chai_list):
    """Print numbered menu (1-based)."""
    for idx, chai in enumerate(chai_list, start=1):
        print(f"{idx}. {chai}")


def get_user_choice(max_valid: int) -> int:
    """Keep asking until user supplies an int between 1 and max_valid."""
    while True:
        try:
            choice = int(input(f"{PROMPT}: "))
            if 1 <= choice <= max_valid:
                return choice
            print(ERROR_NUM)
        except ValueError:
            print(ERROR_TYPE)

# ---------- main flow ----------


def main():
    display_chai_menu(CHAI_MENU)
    choice = get_user_choice(len(CHAI_MENU))
    print(f"You selected: {CHAI_MENU[choice - 1]}")


if __name__ == "__main__":
    main()
