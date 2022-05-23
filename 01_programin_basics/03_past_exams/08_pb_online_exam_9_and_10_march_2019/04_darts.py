player_name = input()
command = input()
starter_points = 301
is_player_won = False
successful_shots_count = 0
false_shots_count = 0
while command != "Retire":
    points = int(input())
    if command == "Single":
        pass
    elif command == "Double":
        points *= 2
    elif command =="Triple":
        points *= 3
    if points <= starter_points:
        starter_points -= points
        successful_shots_count += 1
        if starter_points == 0:
            is_player_won = True
            break
    else:
        false_shots_count += 1
        command = input()
        continue
    command = input()
if is_player_won:
    print(f"{player_name} won the leg with {successful_shots_count} shots.")
else:
    print(f"{player_name} retired after {false_shots_count} unsuccessful shots.")