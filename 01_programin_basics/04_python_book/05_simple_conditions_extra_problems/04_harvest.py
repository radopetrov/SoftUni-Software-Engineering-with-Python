import math

vineyard_size = int(input())
grapes_from_one_square_meter = float(input())
needed_wine = int(input())
workers = int(input())
harvest_grapes = (vineyard_size * 0.4) * grapes_from_one_square_meter
total_wine = harvest_grapes / 2.5
diff = abs(total_wine - needed_wine)
if total_wine < needed_wine:
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")
else:
    wine_per_worker = diff / workers
    print(f"Good harvest this year! Total wine: {math.floor(total_wine)} liters.")
    print(f"{math.ceil(diff)} liters left -> {math.ceil(wine_per_worker)} liters per person.")