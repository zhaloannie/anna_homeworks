from typing import Callable
from functools import wraps

def round_result(ndigits: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if isinstance(result, (int, float)):
                return round(result, ndigits)

            return result
        return wrapper
    return decorator


@round_result(1)
def divide(a, b):
    return a / b

@round_result(3)
def get_value():
    return "not a number, nothing changed..."

print(get_value())
print(divide(2,9))