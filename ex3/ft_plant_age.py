"""Module to check if a plant is ready for harvesting based on its age."""


def ft_plant_age():
    """Check the harvest readiness of a plant."""

    age = int(input("Enter plant age in days: "))

    # Check if the age meets the minimum requirement for harvest
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
