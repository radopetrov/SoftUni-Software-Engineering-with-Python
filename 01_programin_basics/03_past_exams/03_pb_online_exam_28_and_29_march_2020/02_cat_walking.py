minutes_per_walk_day = int(input())
walks_number = int(input())
calories_per_day = int(input())
walk_calories = (walks_number * minutes_per_walk_day) * 5
calories_per_day *= 0.5
if walk_calories >= calories_per_day:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {walk_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {walk_calories}.")