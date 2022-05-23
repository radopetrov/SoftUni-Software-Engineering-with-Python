budget = float(input())
destination = input()
season = input()
days = int(input())
one_shooting_day_price = 0
if season == "Winter":
    if destination == "Dubai":
        one_shooting_day_price = 45000
    elif destination == "Sofia":
        one_shooting_day_price = 17000
    elif destination == "London":
        one_shooting_day_price = 24000
elif season == "Summer":
    if destination == "Dubai":
        one_shooting_day_price = 40000
    elif destination == "Sofia":
        one_shooting_day_price = 12500
    elif destination == "London":
        one_shooting_day_price = 20250
total_costs = one_shooting_day_price * days
if destination == "Dubai":
    total_costs *= 0.7
elif destination == "Sofia":
    total_costs *= 1.25
difference = abs(total_costs - budget)
if budget >= total_costs:
    print(f"The budget for the movie is enough! We have {difference:.02f} leva left!")
else:
    print(f"The director needs {difference:.02f} leva more!")