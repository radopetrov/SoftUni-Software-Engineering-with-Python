destination = input()
date = input()
days = int(input())
price_per_day = 0
if date == "21-23":
    if destination == "France":
        price_per_day = 30
    elif destination == "Italy":
        price_per_day = 28
    elif destination == "Germany":
        price_per_day = 32
elif date == "24-27":
    if destination == "France":
        price_per_day = 35
    elif destination == "Italy":
        price_per_day = 32
    elif destination == "Germany":
        price_per_day = 37
elif date == "28-31":
    if destination == "France":
        price_per_day = 40
    elif destination == "Italy":
        price_per_day = 39
    elif destination == "Germany":
        price_per_day = 43
total_costs = price_per_day * days
print(f"Easter trip to {destination} : {total_costs:.2f} leva.")