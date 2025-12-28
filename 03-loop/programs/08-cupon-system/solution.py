# ---------- 1.  tiny "database" ----------
import re
from datetime import datetime, date
users = [
    {"username": "kc",   "password": "123"},
    {"username": "amit", "password": "888"},
    {"username": "ram",  "password": "555"},
]

products = [
    {"product_name": "laptop",  "price": 300},
    {"product_name": "mouse",   "price": 50},
    {"product_name": "keyboard", "price": 100},
]

coupon_db = {
    "SUMMER20": {
        "discount_percent": 20,
        "min_purchase": 50.0,
        "expiration_date": "2025-12-31",
        "usage_limit": 1,
        "used_customers": []        # just a list of usernames
    },
    "WELCOME10": {
        "discount_percent": 10,
        "min_purchase": 25.0,
        "expiration_date": "2025-12-31",
        "usage_limit": 1,
        "used_customers": []
    }
}

# ---------- 2.  helpers ----------


def login() -> str | None:
    """3-tries login.  Returns username on success, else None."""
    for tries in range(3, 0, -1):
        user = input("Username: ").strip()
        pwd = input("Password: ").strip()
        if any(u["username"] == user and u["password"] == pwd for u in users):
            return user
        print(
            f"Wrong password.  {tries-1} tries left." if tries > 1 else "Account locked.")
    return None


def shop() -> float:
    """Ask qty for each product, return cart total."""
    total = 0.0
    for p in products:
        qty = int(input(f"How many {p['product_name']} @ ${p['price']}? "))
        total += qty * p["price"]
    return total


def validate_coupon(code: str, cart: float, user: str):
    """
    Returns  (ok:bool, message:str, discount:float)
    Does NOT mutate coupon_db yet – we do that only after success.
    """
    code = code.strip().upper()
    cp = coupon_db.get(code)
    if not cp:
        return False, "Code not found", 0.0

    # ---- format ----
    if not re.fullmatch(r"[A-Z0-9]{6,12}", code):
        return False, "Bad format – 6-12 alphanumeric only", 0.0

    # ---- expiry ----
    expiry = datetime.strptime(cp["expiration_date"], "%Y-%m-%d").date()
    if date.today() > expiry:
        return False, "Coupon expired", 0.0

    # ---- minimum ----
    if cart < cp["min_purchase"]:
        return False, f"Need ${cp['min_purchase']:.2f}+ in cart", 0.0

    # ---- usage limit ----
    if user in cp["used_customers"]:
        return False, "You already used this coupon", 0.0
    if len(cp["used_customers"]) >= cp["usage_limit"]:
        return False, "Coupon fully redeemed", 0.0

    discount = cart * cp["discount_percent"] / 100
    return True, "Coupon applied successfully", round(discount, 2)

# ---------- 3.  main flow ----------


def main():
    user = login()
    if not user:
        return          # locked out

    print("\n--- shopping ---")
    cart = shop()
    print(f"Cart total: ${cart:.2f}")

    print("\n--- coupon ---")
    code = input("Enter coupon (or press Enter to skip): ").strip()
    if code:
        ok, msg, disc = validate_coupon(code, cart, user)
        print(msg)
        if ok:
            # ----- mutate only after success -----
            coupon_db[code.upper()]["used_customers"].append(user)
            print(f"Discount:  ${disc:.2f}")
            print(f"Final pay: ${cart - disc:.2f}")
        else:
            print(f"No discount – pay ${cart:.2f}")
    else:
        print(f"No coupon – pay ${cart:.2f}")


# ---------- 4.  run ----------
if __name__ == "__main__":
    main()
