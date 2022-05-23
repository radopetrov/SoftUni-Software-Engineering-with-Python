bag_price = float(input())
bags_kg = float(input())
day_till_trip = int(input())
bags_number = int(input())
if bags_kg < 10:
    bag_price *= 0.2
elif bags_kg <= 20:
    bag_price *= 0.5
if day_till_trip < 7:
    bag_price *= 1.4
elif day_till_trip <= 30:
    bag_price *= 1.15
else:
    bag_price *= 1.1
total_price = bag_price * bags_number
print(f"The total price of bags is: {total_price:.2f} lv.")