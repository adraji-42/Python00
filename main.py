#!/usr/bin/env python3

"""
Helper file for Growing Code.
Modified to support sub-directory structure (ex0, ex1, etc.)
"""

import sys
import os


def test_ft_exercise(exercise_name, folder=None):
    """
    Tries to run one of your exercises by adding its folder to sys.path.
    """
    print(f"\n=== Testing {exercise_name} ===")

    if folder:
        path = os.path.join(os.getcwd(), folder)
        if path not in sys.path:
            sys.path.append(path)

    try:
        # Import the module
        ft_module = __import__(exercise_name)

        # Reload the module in case of multiple tests in one session
        import importlib
        importlib.reload(ft_module)

        # Get the function from your file
        ft_function = getattr(ft_module, exercise_name)

        # Special handling for ft_seed_inventory (Exercise 7)
        if exercise_name == "ft_seed_inventory":
            print("Testing with different seed types and units:\n")
            ft_function("tomato", 15, "packets")
            ft_function("carrot", 8, "grams")
            ft_function("lettuce", 12, "area")
            print("\nTesting with unknown unit:")
            ft_function("basil", 5, "unknown")
        else:
            # Run your function normally (no parameters)
            ft_function()

    except ImportError:
        print(f"❌ Could not find {exercise_name}.py in {folder}/")
    except AttributeError:
        print(f"❌ Could not find function {exercise_name}() in your file")
    except TypeError as error:
        print(f"❌ Type error: {error}")
    except Exception as error:
        print(f"❌ Error running your function: {error}")


def main():
    """Main terminal interface for testing exercises."""
    print("🌱 Welcome to Growing Code! 🌱")
    print("\nWhich exercise would you like to test?")
    print("0 - ex0/ft_hello_garden")
    print("1 - ex1/ft_plot_area")
    print("2 - ex2/ft_harvest_total")
    print("3 - ex3/ft_plant_age")
    print("4 - ex4/ft_water_reminder")
    print("5 - ex5/ft_count_harvest (Iterative & Recursive)")
    print("6 - ex6/ft_garden_summary")
    print("7 - ex7/ft_seed_inventory")
    print("a - test all exercises")
    print()

    choice = input("Enter your choice: ")

    # Mapping choices to folder and file names
    exercises = {
        "0": [("ft_hello_garden", "ex0")],
        "1": [("ft_plot_area", "ex1")],
        "2": [("ft_harvest_total", "ex2")],
        "3": [("ft_plant_age", "ex3")],
        "4": [("ft_water_reminder", "ex4")],
        "5": [
            ("ft_count_harvest_iterative", "ex5"),
            ("ft_count_harvest_recursive", "ex5")
        ],
        "6": [("ft_garden_summary", "ex6")],
        "7": [("ft_seed_inventory", "ex7")]
    }

    if choice == "a":
        for key in sorted(exercises.keys()):
            for ex, folder in exercises[key]:
                test_ft_exercise(ex, folder)
    elif choice in exercises:
        for ex, folder in exercises[choice]:
            test_ft_exercise(ex, folder)
    else:
        print("❌ Invalid choice!")


if __name__ == "__main__":
    main()
