import math

guests_number = int(input())
budget = int(input())
kozunatsi_number = math.ceil(guests_number / 3)
kozunatsi_price = kozunatsi_number * 4
eggs_number = guests_number * 2
eggs_costs = eggs_number * 0.45
total_cost = kozunatsi_price + eggs_costs
difference = abs(total_cost - budget)
if budget >= total_cost:
    print(f"Lyubo bought {kozunatsi_number} Easter bread and {eggs_number} eggs.")
    print(f"He has {difference:.2f} lv. left.")

else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")
