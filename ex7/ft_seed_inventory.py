"""Module to manage and display seed inventory with specific units."""


def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    """Display the current inventory of seeds based on their unit type."""

    # Define valid units for checking
    valid_units = ("packets", "grams", "area")

    if unit in valid_units:
        # Determine the appropriate label based on the unit
        if unit == "packets":
            inventory_info = f"{quantity} {unit} available"
        elif unit == "grams":
            inventory_info = f"{quantity} {unit} total"
        else:
            inventory_info = f"covers {quantity} square meters"

        print(f"{seed_type.capitalize()} seeds: {inventory_info}")

    else:
        print("Unknown unit type")
