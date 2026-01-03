def ft_count_harvest_iterative():

    remaining_days = int(input("Days until harvest: "))

    for day in range(1, remaining_days + 1, 1):
        print(f"Day {day}")

    print("Harvest time!")
