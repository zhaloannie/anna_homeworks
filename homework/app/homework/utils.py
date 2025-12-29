def is_strong_password(password:str) -> bool:
    if len(password) < 8:
        return False

    has_digit = False
    has_upper = False
    has_lower = False

    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True

    return has_digit and has_upper and has_lower

print(is_strong_password("hallihallo"))
print(is_strong_password("Hall1hallo"))



def has_duplicates(my_list: list[int | float | str | bool]) -> bool:
    return len(my_list) != len(set(my_list))

print(has_duplicates([1, 2, 3, 4]))
print(has_duplicates([1, "a", True, 1]))



def is_warm(temperature: int | float) -> bool:
    return temperature > 20

print(is_warm(10))
print(is_warm(21))