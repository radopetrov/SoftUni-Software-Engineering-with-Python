budget = float(input())
nights = int(input())
one_night_price = float(input())
extra_costs_interest = int(input())
if nights > 7:
    one_night_price *= 0.95
total_nights_cost = nights * one_night_price
extra_costs = budget * extra_costs_interest / 100
total_costs = total_nights_cost + extra_costs
difference = abs(total_costs - budget)
if budget >= total_costs:
    print(f"Ivanovi will be left with {difference:.02f} leva after vacation.")
else:
    print(f"{difference:.02f} leva needed.")