"""Module to calculate the area of a garden plot."""


def ft_plot_area():
    """
    Calculate and print the area of a rectangle based on user input.

    The function prompts the user for length and width, converts them
    to integers, and calculates the area (length * width).
    """
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))

    # Calculating area using f-string for formatted output
    print(f"Plot area: {length * width}")
