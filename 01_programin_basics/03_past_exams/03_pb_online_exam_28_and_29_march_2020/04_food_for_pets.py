days = int(input())
total_food = float(input())
dog_food_eaten = 0
cat_food_eaten = 0
biscuits = 0
for currеnt_day in range(1, days + 1):
    food_eaten_from_dog = int(input())
    food_eaten_from_cat = int(input())
    dog_food_eaten += food_eaten_from_dog
    cat_food_eaten += food_eaten_from_cat
    if currеnt_day % 3 == 0:
        biscuits += (food_eaten_from_cat + food_eaten_from_dog) * 0.1
eaten_food_share = (dog_food_eaten + cat_food_eaten) / total_food * 100
eaten_dog_food_share = dog_food_eaten / (dog_food_eaten + cat_food_eaten) * 100
eaten_cat_food_share = cat_food_eaten / (dog_food_eaten + cat_food_eaten) * 100
print(f"Total eaten biscuits: {int(round(biscuits, 0))}gr.")
print(f"{eaten_food_share:.2f}% of the food has been eaten.")
print(f"{eaten_dog_food_share:.2f}% eaten from the dog.")
print(f"{eaten_cat_food_share:.2f}% eaten from the cat.")