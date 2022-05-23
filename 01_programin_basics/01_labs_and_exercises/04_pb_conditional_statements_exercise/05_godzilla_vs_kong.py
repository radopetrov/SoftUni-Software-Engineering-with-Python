budget = float(input())
number_of_statists = int(input())
one_dress_price = float(input())

decor = budget*0.1
deresses_price = number_of_statists * one_dress_price
if number_of_statists > 150:
    deresses_price *= 0.9

needed_money = decor + deresses_price
difference = abs(needed_money - budget)
if needed_money > budget: #парите не стигат
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")