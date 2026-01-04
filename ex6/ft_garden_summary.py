"""Module to display a summary of the garden status."""


def ft_garden_summary():
    """Prompt the user for garden details and display a summary report."""

    garde_name = input("Enter garden name: ")
    plant_number = input("Enter number of plants: ")

    # Displaying the collected garden information
    print(f"Garden: {garde_name}")
    print(f"Plants: {plant_number}")
    print("Status: Growing well!")
