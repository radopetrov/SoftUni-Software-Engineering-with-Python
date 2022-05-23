distance = int(input())
time_of_day = str(input())
price_per_km = 0
if distance < 20:  # taxi fee
    if time_of_day == "day":
        price_per_km = 0.79
    elif time_of_day == "night":
        price_per_km = 0.9
elif distance < 100:  # buss fee
    price_per_km = 0.09
else:  # train fee
    price_per_km = 0.06
total_price = price_per_km * distance
if distance < 20:
    total_price += 0.7  # taxi starter fee
    print(f"{total_price:.2f}")
else:
    print(f"{total_price:.2f}")
