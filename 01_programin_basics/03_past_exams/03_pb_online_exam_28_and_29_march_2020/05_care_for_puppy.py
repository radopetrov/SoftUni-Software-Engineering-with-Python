bought_food = int(input())
bought_food *= 1000
food_eaten = input()

food_is_enough = True
while food_eaten != "Adopted":
    food_eaten = int(food_eaten)
    bought_food -= food_eaten
    food_eaten = input()
if bought_food < 0:
    food_is_enough = False
if food_is_enough:
    print(f"Food is enough! Leftovers: {bought_food} grams.")
else:
    print(f"Food is not enough. You need {abs(bought_food)} grams more.")