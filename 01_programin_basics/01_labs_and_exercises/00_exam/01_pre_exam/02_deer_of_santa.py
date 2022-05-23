import math

days = int(input())
food_left = int(input())
first_deer_food_per_day = float(input())
second_deer_food_per_day = float(input())
third_deer_food_per_day = float(input())
total_food_eaten = (first_deer_food_per_day + \
                    second_deer_food_per_day + \
                    third_deer_food_per_day) * days
difference = abs(total_food_eaten - food_left)
if food_left >= total_food_eaten:
    print(f"{math.floor(difference)} kilos of food left.")
else:
    print(f"{math.ceil(difference)} more kilos of food are needed.")
