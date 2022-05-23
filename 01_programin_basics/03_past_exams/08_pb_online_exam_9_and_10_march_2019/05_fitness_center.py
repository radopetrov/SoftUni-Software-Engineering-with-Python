customers_number = int(input())
workout_counter = 0
items_counter = 0
back_counter = 0
chest_counter = 0
legs_counter = 0
abs_counter = 0
protein_shake_counter = 0
protein_bar_counter = 0
for current_customer in range(customers_number):
    command = input()
    if command == "Back":
        back_counter += 1
        workout_counter += 1
    elif command == "Chest":
        chest_counter += 1
        workout_counter += 1
    elif command == "Legs":
        legs_counter += 1
        workout_counter += 1
    elif command == "Abs":
        abs_counter += 1
        workout_counter += 1
    elif command == "Protein shake":
        protein_shake_counter += 1
        items_counter += 1
    elif command == "Protein bar":
        protein_bar_counter += 1
        items_counter += 1
workout_share_rate = workout_counter / customers_number * 100
items_bought_share_rate = items_counter / customers_number *100
print(f"{back_counter} - back")
print(f"{chest_counter} - chest")
print(f"{legs_counter} - legs")
print(f"{abs_counter} - abs")
print(f"{protein_shake_counter} - protein shake")
print(f"{protein_bar_counter} - protein bar")
print(f"{workout_share_rate:.2f}% - work out")
print(f"{items_bought_share_rate:.2f}% - protein")