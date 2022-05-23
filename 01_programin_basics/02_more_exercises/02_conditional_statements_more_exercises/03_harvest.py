import math
x = int(input()) #площ на лозето в кв.м.
y = float(input()) #розде за 1 квм.м
z = int(input()) #нужни литри вино
workers = int(input()) #брой работници

harvest_area = x * 0.4
harvest_grapes = harvest_area * y
wine = harvest_grapes / 2.5

left_wine = abs(wine - z)
wine_for_one_worker = left_wine/ workers

if wine < z:
    print(f"It will be a tough winter! More {math.floor(left_wine)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(left_wine)} liters left -> {math.ceil(wine_for_one_worker)} liters per person.")