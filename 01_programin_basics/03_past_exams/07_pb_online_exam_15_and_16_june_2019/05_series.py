budget = float(input())
series_number = int(input())
total_costs = 0
for series in range(series_number):
    series_title = input()
    series_price = float(input())
    if series_title == "Thrones":
        series_price *= 0.5
    elif series_title == "Lucifer":
        series_price *= 0.6
    elif series_title == "Protector":
        series_price *= 0.7
    elif series_title == "TotalDrama":
        series_price *= 0.8
    elif series_title == "Area":
        series_price *= 0.9
    total_costs += series_price
differance = abs(budget - total_costs)
if budget >= total_costs:
    print(f"You bought all the series and left with {differance:.2f} lv.")
else:
    print(f"You need {differance:.2f} lv. more to buy the series!")