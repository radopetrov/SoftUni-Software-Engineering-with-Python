veg_price = float(input())
fruit_price = float(input())
veg_kg = int(input())
fruit_kg = int(input())
total_price = veg_price * veg_kg \
    + fruit_kg * fruit_price
total_price /= 1.94
print(total_price)
