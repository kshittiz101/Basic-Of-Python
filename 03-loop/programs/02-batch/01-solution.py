def get_batch_messages(start: int = 1, end: int = 4) -> list[str]:
    """
    Generate a list of batch preparation messages.

    Args:
        start: Starting batch number (inclusive)
        end: Ending batch number (inclusive)

    Returns:
        List of formatted batch messages
    """
    messages = []
    for batch_num in range(start, end + 1):
        messages.append(f"Preparing chai for batch #{batch_num}")
    return messages


def main() -> None:
    """Generate and display batch messages."""
    batch_messages = get_batch_messages(end=4)  # Use default start=1
    for msg in batch_messages:
        print(msg)


if __name__ == "__main__":
    main()
