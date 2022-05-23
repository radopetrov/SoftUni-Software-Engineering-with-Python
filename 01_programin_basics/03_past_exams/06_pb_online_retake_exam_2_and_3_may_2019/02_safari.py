budget = float(input())
fuel_liters = float(input())
day = input()
total_costs = fuel_liters * 2.1 + 100
if day == "Saturday":
    total_costs *= 0.9
elif day == "Sunday":
    total_costs *= 0.8
diference = abs(budget - total_costs)
if budget >= total_costs:
    print(f"Safari time! Money left: {diference:.02f} lv. ")
else:
    print(f"Not enough money! Money needed: {diference:.02f} lv.")