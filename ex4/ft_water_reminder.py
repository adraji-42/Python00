"""Module to provide watering reminders for the garden."""


def ft_water_reminder():
    """
    Check if plants need watering based on the last watering date.

    Prompts the user for the number of days since the last watering.
    If it has been more than 2 days, it prints a reminder to water.
    Otherwise, it confirms the plants are fine.
    """
    last_watered = int(input("Days since last watering: "))

    # Decision logic based on the 2-day threshold
    if last_watered > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
