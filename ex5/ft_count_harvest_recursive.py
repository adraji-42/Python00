"""Module to count harvest days using a recursive approach."""


def ft_count_harvest_recursive():
    """
    Initiate a recursive count of days until harvest.

    Prompts the user for the total remaining days and calls a nested
    recursive function to print each day sequentially.
    """
    remaining_days = int(input("Days until harvest: "))

    def ft_count_up(n, target):
        """
        Recursive helper function to print the current day.

        Args:
            n (int): The current day to print.
            target (int): The final day of the countdown.
        """
        # Base case: if the current day exceeds the target, stop recursion
        if n > target:
            return
        print(f"Day {n}")
        # Recursive call: move to the next day
        ft_count_up(n + 1, target)

    ft_count_up(1, remaining_days)
    print("Harvest time!")
