import math

days = int(input())
food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

dog_eats = days * dog_food_per_day
cat_eats = days * cat_food_per_day
turtle_eats = (days * turtle_food_per_day) / 1000

total_food_eaten = dog_eats + cat_eats + turtle_eats
food_dif = abs(food - total_food_eaten)

if food >= total_food_eaten:
    print(f"{math.floor(food_dif)} kilos of food left.")
else:
    print(f"{math.ceil(food_dif)} more kilos of food are needed.")