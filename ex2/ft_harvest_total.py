"""Module to calculate the total harvest over three days."""


def ft_harvest_total():
    """Collect harvest amounts for three days and calculate the total."""

    harvests = [
        int(input("Day 1 harvest: ")),
        int(input("Day 2 harvest: ")),
        int(input("Day 3 harvest: "))
    ]

    total = 0
    # Iterating through the list to accumulate the total amount
    for amount in harvests:
        total += amount

    print(f"Total harvest: {total}")
