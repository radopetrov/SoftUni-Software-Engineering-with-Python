fruit = input()
set_size = input()
ordered_sets = int(input())
price_per_number = 0
set_number = 0
if set_size == "small":
    set_number = 2
    if fruit == "Watermelon":
        price_per_number = 56
    elif fruit == "Mango":
        price_per_number = 36.66
    elif fruit == "Pineapple":
        price_per_number = 42.10
    elif fruit == "Raspberry":
        price_per_number = 20
elif set_size == "big":
    set_number = 5
    if fruit == "Watermelon":
        price_per_number = 28.70
    elif fruit == "Mango":
        price_per_number = 19.60
    elif fruit == "Pineapple":
        price_per_number = 24.80
    elif fruit == "Raspberry":
        price_per_number = 15.20
total_price = price_per_number * set_number * ordered_sets
if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.5
print(f"{total_price:.2f} lv.")