

def is_leap(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)


def days_in_month(m, y):
    if m < 1 or m > 12:
        raise ValueError("Invalid month")

    if m == 2:
        return 29 if is_leap(y) else 28
    elif m in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def day_of_year(d, m, y):
    if m < 1 or m > 12:
        raise ValueError("Invalid month")

    if d < 1 or d > days_in_month(m, y):
        raise ValueError("Invalid day")

    total = 0
    for month in range(1, m):
        total += days_in_month(month, y)

    return total + d


def days_remaining_in_year(d, m, y):
    return (366 if is_leap(y) else 365) - day_of_year(d, m, y)


if __name__ == "__main__":
    print("Leap year:", is_leap(2024))
    print("Days in February 2025:", days_in_month(2, 2025))
    print("Day of year:", day_of_year(31, 12, 2024))
    print("Days remaining:", days_remaining_in_year(31, 12, 2024))
