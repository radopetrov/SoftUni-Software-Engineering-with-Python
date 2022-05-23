month = input()
days = int(input())

room = "" #studio or apratment
studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    if days > 7 and days <= 14:
        studio_price = 50 * 0.95
        apartment_price = 65
    elif days > 14:
        studio_price = 50 * 0.7
        apartment_price = 65 * 0.9
    elif days <= 7:
        studio_price = 50
        apartment_price = 65
elif month == "June" or month == "September":
    if days <= 14:
        studio_price = 75.2
        apartment_price = 68.7
    elif days > 14:
        studio_price = 75.2 * 0.8
        apartment_price = 68.7 * 0.9
elif month == "July" or month == "August":
    if days <= 14:
        studio_price = 76
        apartment_price = 77
    elif days > 14:
        studio_price = 76
        apartment_price = 77 * 0.9
studio_total = studio_price * days
apartment_total = apartment_price * days

print(f"Apartment: {apartment_total:.2f} lv.")
print(f"Studio: {studio_total:.2f} lv.")