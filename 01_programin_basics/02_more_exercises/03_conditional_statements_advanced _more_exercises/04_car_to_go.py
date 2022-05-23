budget = float(input())
season = str(input())
car_class = ""
car_type = ""
if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        budget *= 0.35
        car_type = "Cabrio"
    elif season == "Winter":
        budget *= 0.65
        car_type = "Jeep"
elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        budget *= 0.45
        car_type = "Cabrio"
    elif season == "Winter":
        budget *= 0.8
        car_type = "Jeep"
elif budget > 500:
    car_class = "Luxury class"
    budget *= 0.9
    car_type = "Jeep"
print(car_class)
print(f"{car_type} - {budget:.2f}")
