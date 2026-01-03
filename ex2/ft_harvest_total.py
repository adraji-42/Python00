def ft_harvest_total():

    harvests = [
        int(input("Day 1 harvest: ")),
        int(input("Day 2 harvest: ")),
        int(input("Day 3 harvest: "))
    ]

    total = 0
    for amount in harvests:
        total += amount

    print(f"Total harvest: {total}")
