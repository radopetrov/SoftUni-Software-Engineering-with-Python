days = int(input())
hours = int(input())
total_costs = 0
for current_day in range(1, days + 1):
    cost_current_day = 0
    for current_hour in range(1, hours + 1):
        if current_day % 2 == 0 and current_hour % 2 != 0:
            parking_cost = 2.5
        elif current_day % 2 != 0 and current_hour % 2 == 0:
            parking_cost = 1.25
        else:
            parking_cost = 1
        total_costs += parking_cost
        cost_current_day += parking_cost
    print(f"Day: {current_day} - {cost_current_day:.2f} leva")
print(f"Total: {total_costs:.2f} leva")