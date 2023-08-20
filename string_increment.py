def digital_root(number: int):
    if not number % 9:
        return 9
    return number % 9


print(digital_root(123))
