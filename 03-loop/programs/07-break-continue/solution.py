# 1. Use UPPER_CASE for constants
CHAI_FLAVORS = [
    'Vanilla',
    'Out of Stock',
    'Spice',
    'Discontinued',
    'Ginger',
    'Cardamom'
]


def tea_flavor_tracker(tea_flavors: list[str]) -> None:
    """
    Process chai flavor inventory, skipping out-of-stock items and 
    stopping entirely if a discontinued flavor is encountered.

    Args:
        tea_flavors: List of flavor names/statuses.
    """
    for flavor in tea_flavors:
        if flavor == "Out of Stock":
            continue

        if flavor == "Discontinued":
            break

        print(flavor)


def main() -> None:
    tea_flavor_tracker(CHAI_FLAVORS)


if __name__ == "__main__":
    main()
