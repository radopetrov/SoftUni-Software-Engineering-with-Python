import math

staff_number = int(input())
entrance_fee = float(input())
deck_chair_price = float(input())
umbrella_price = float(input())
entrance_fee_total = staff_number * entrance_fee
umbrella_total_cost = math.ceil(staff_number / 2) * umbrella_price
deck_chair_total_price = math.ceil(staff_number * 0.75) * deck_chair_price
total_cost = entrance_fee_total + umbrella_total_cost + deck_chair_total_price
print(f"{total_cost:.2f} lv.")