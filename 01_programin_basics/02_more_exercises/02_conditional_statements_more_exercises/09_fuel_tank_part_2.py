fuel_type = input() #"Gas", "Gasoline" или "Diesel"
fuel_quantity = float(input())
club_card = input() # Yes or No
fuel_price = 0
club_discount_per_liter = 0
if fuel_type == "Gas":
    fuel_price = 0.93
    if club_card == "Yes":
        club_discount_per_liter = 0.08
elif fuel_type == "Gasoline":
    fuel_price = 2.22
    if club_card == "Yes":
        club_discount_per_liter = 0.18
else:
    fuel_price = 2.33
    if club_card == "Yes":
        club_discount_per_liter = 0.12
total_cost = (fuel_price - club_discount_per_liter) * fuel_quantity
if fuel_quantity > 20 and fuel_quantity <= 25:
    total_cost *= 0.92
elif fuel_quantity > 25:
    total_cost *= 0.9
print(f"{total_cost:.2f} lv.")
