def ft_seed_inventory(seed_type: str, quantity: int, unit: str):

    if (unit == "packets" or unit == "grams" or unit == "area"):
        if (unit == "packets"):
            last_word = unit + " available"
        elif (unit == "grams"):
            last_word = unit + " total"
        else:
            last_word = "square meters"
        print(seed_type.capitalize(), "seeds:", quantity, last_word)

    else:
        print("Unknown unit type")
