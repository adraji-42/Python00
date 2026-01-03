"""Module to count down the days until the harvest begins."""


def ft_count_harvest_iterative():
    """
    Print each day leading up to the harvest.

    Prompts the user for the number of remaining days and uses
    a for loop to iterate from day 1 to the final day, printing
    the progress before declaring it is harvest time.
    """
    remaining_days = int(input("Days until harvest: "))

    # Iterate from 1 up to and including remaining_days
    for day in range(1, remaining_days + 1, 1):
        print(f"Day {day}")

    print("Harvest time!")
