def display_tokens(start: int = 1, end: int = 10) -> list[str]:
    """
    Generate token service messages for a range of tokens.

    Args:
        start: Starting token number (inclusive)
        end: Ending token number (inclusive)

    Returns:
        List of service messages for each token
    """
    messages = []
    for token in range(start, end + 1):
        messages.append(f"Serve chai to token no: {token}")
    return messages


def main() -> None:
    """Main execution function."""
    # Generate and print all tokens
    tokens = display_tokens(1, 10)
    for message in tokens:
        print(message)


if __name__ == "__main__":
    main()
