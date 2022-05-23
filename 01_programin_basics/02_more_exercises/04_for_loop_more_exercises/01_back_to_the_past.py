heritage = float(input())
year_of_death = int(input())
total_costs = 0
for age in range(18, (year_of_death-(1800-18)) + 1):
    if age % 2 == 0:
        total_costs += 12000
    else:
        total_costs += (12000 + 50 * age)
diference = abs(heritage - total_costs)
if heritage >= total_costs:
    print(f"Yes! He will live a carefree life and will have {diference:.02f} dollars left.")
else:
    print(f"He will need {diference:.02f} dollars to survive.")