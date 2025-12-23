
"""
Railway-seat feature lookup.
Adding a new type = 1 line in SEAT_MAP, zero code changes.
"""

from typing import Dict

# --------------------------------------------------------------------------- #
# 1.  Data layer – easy to extend or translate
# --------------------------------------------------------------------------- #
SEAT_MAP: Dict[str, str] = {
    "sleeper": "bed provided",
    "ac": "AC coach + bed",
    "general": "non-AC sitting, no bed",
    "luxury": "AC, luxury bed, TV",
}

# --------------------------------------------------------------------------- #
# 2.  Pure business logic – no I/O, no print, easy to unit-test
# --------------------------------------------------------------------------- #


def seat_features(seat_type: str) -> str:
    """Return human-readable features for a normalised seat type."""
    return SEAT_MAP.get(seat_type.lower().strip(), "Invalid seat type")

# --------------------------------------------------------------------------- #
# 3.  thin CLI – only this part touches input / print
# --------------------------------------------------------------------------- #


def main() -> None:
    user_choice = input("Enter seat type (sleeper, ac, general, luxury): ")
    print(seat_features(user_choice))


if __name__ == "__main__":
    main()
