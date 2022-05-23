days_number = int(input())
hours_per_day = int(input())
price_per_hour = 0
total_costs= 0
for current_day in range(1, days_number + 1):
    current_day_costs = 0
    for current_hour in range(1, hours_per_day + 1):
        if current_day % 2 == 0 and current_hour % 2 != 0:
            price_per_hour = 2.5
        elif current_day % 2 != 0 and current_hour % 2 == 0:
            price_per_hour = 1.25
        else:
            price_per_hour = 1
        current_day_costs += price_per_hour
        total_costs += price_per_hour
    print(f"Day: {current_day} - {current_day_costs:.2f} leva")
print(f"Total: {total_costs:.2f} leva")