def is_valid_email(value: str) -> bool:
    if not value:
        return False

    if value.count("@") != 1:
        return False

    if value [0] in "@." or value [-1] in "@.":
        return False

    local, domain = value.split("@")

    if "." not in domain:
        return False

    return True

def avg(values: list[float]) -> float:

    if not values:
        raise ValueError("Empty list")

    return sum(values)/len(values)

def uah_to_usd(amount: float, rate: float) -> float:

    if amount <= 0:
        raise ValueError("Invalid amount")

    if rate <= 0:
        raise ValueError("Invalid rate")

    return amount/rate