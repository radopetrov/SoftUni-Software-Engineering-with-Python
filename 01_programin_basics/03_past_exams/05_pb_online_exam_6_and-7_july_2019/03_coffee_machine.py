drink = input()
sugar = input()
drinks_number = int(input())
price_per_drink = 0
if drink == "Espresso":
    if sugar == "Without":
        price_per_drink = 0.9
    elif sugar == "Normal":
        price_per_drink = 1
    elif sugar == "Extra":
        price_per_drink = 1.2
elif drink == "Cappuccino":
    if sugar == "Without":
        price_per_drink = 1
    elif sugar == "Normal":
        price_per_drink = 1.2
    elif sugar == "Extra":
        price_per_drink = 1.6
elif drink == "Tea":
    if sugar == "Without":
        price_per_drink = 0.5
    elif sugar == "Normal":
        price_per_drink = 0.6
    elif sugar == "Extra":
        price_per_drink = 0.7
total_cost = drinks_number * price_per_drink
if sugar == "Without":
    total_cost *= 0.65
if drink == "Espresso" and drinks_number >= 5:
    total_cost *= 0.75
if total_cost > 15:
    total_cost *= 0.8
print(f"You bought {drinks_number} cups of {drink} for {total_cost:.2f} lv.")