season = str(input())
km_per_month = float(input())
price_per_km = 0
if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.75
    elif season == "Summer":
        price_per_km = 0.9
    elif season == "Winter":
        price_per_km = 1.05
elif km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.95
    elif season == "Summer":
        price_per_km = 1.10
    elif season == "Winter":
        price_per_km = 1.25
elif km_per_month <= 20000:
    price_per_km = 1.45
total_profit = (km_per_month * price_per_km * 4) * 0.9
print(f"{total_profit:.2f}")