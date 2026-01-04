"""Module to calculate the area of a garden plot."""


def ft_plot_area():
    """Calculate and print the area of a rectangle based on user input."""

    length = int(input("Enter length: "))
    width = int(input("Enter width: "))

    # Calculating area using f-string for formatted output
    print(f"Plot area: {length * width}")
