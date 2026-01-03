"""Module to manage and display seed inventory with specific units."""


def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    """
    Display the current inventory of seeds based on their unit type.

    Args:
        seed_type (str): The name of the seed.
        quantity (int): The amount of seeds.
        unit (str): The unit of measurement (packets, grams, or area).
    """
    # Define valid units for checking
    valid_units = ("packets", "grams", "area")

    if unit in valid_units:
        # Determine the appropriate label based on the unit
        if unit == "packets":
            last_word = unit + " available"
        elif unit == "grams":
            last_word = unit + " total"
        else:
            last_word = "square meters"

        print(seed_type.capitalize(), "seeds:", quantity, last_word)

    else:
        print("Unknown unit type")
