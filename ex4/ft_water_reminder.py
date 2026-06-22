"""Module to provide watering reminders for the garden."""


def ft_water_reminder():
    """Check if plants need watering based on the last watering date."""

    last_watered = int(input("Days since last watering: "))

    # Decision logic based on the 2-day threshold
    if last_watered > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
