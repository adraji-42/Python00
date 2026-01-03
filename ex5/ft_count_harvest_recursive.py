def ft_count_harvest_recursive():

    remaining_days = int(input("Days until harvest: "))

    def ft_count_up(n, target):
        if n > target:
            return
        print(f"Day {n}")
        ft_count_up(n + 1, target)

    ft_count_up(1, remaining_days)
    print("Harvest time!")
