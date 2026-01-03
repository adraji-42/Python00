def ft_seed_inventory(seed_type: str, quantity: int, unit: str):

    output_string = seed_type[0].upper() + seed_type[1:].lower()

    elif (unit == "packets" or unit == "grams" or unit == "area"):
        if (unit == "packets"):
            last_word = "available"
        elif (unit == "grams"):
            last_word = "total"
        else:
            last_word = "square meters"
        print(f"{output_string} seeds: {quantity} {unit} {last_word}")

    else:
        print("Unknown unit type")
