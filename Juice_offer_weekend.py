percentages = {(1, 2): 1.0, (3, 3): 3 / 4, (4, 5): 2 / 3, (6, 10): 1 / 2}
minimum = 1
maximum = 10
bonus = 4 / 5


def calculate_discount(amount: int, member: bool):
    if not isinstance(amount, int):
        raise ValueError("amount must be an int")
    if amount < minimum or amount > maximum:
        raise ValueError("amount has to be greater than 0 and less or equal to 10")
    for interval, percentage in percentages.items():
        if interval[0] <= amount <= interval[1]:
            if member:
                percentage *= bonus
            return 1 - percentage

    raise RuntimeError("Logical error. Check implementation.")


print(calculate_discount(1, False))
