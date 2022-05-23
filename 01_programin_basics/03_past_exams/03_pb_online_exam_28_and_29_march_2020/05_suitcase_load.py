free_space = float(input())
bag_size = input()
bag_counter = 0
is_space_enough = True
while bag_size != "End":
    bag_size = float(bag_size)
    bag_counter += 1
    if bag_counter % 3 == 0:
        bag_size *= 1.1
    if bag_size < free_space:
        free_space -= bag_size
    else:
        bag_counter -= 1
        is_space_enough = False
        break
    bag_size = input()
if is_space_enough:
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")
print(f"Statistic: {bag_counter} suitcases loaded.")