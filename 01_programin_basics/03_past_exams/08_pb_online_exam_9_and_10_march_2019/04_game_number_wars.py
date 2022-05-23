firs_player_name = input()
second_player_name = input()
command = input()
winner = ""
winner_points = 0
is_number_wars = False
first_player_points = 0
second_player_points = 0
while command != "End of game":
    first_player_hand = int(command)
    second_player_hand = int(input())
    if first_player_hand > second_player_hand:
        first_player_points += first_player_hand - second_player_hand
    elif first_player_hand < second_player_hand:
        second_player_points += second_player_hand - first_player_hand
    else: # при еднакви карти на двамата == Number Wars
        first_player_hand = int(input())
        second_player_hand = int(input())
        is_number_wars = True
        if first_player_hand > second_player_hand:
            winner = firs_player_name
            winner_points = first_player_points
            break
        elif first_player_hand < second_player_hand:
            winner = second_player_name
            winner_points = second_player_points
            break
    command = input()
if is_number_wars:
    print("Number wars!")
    print(f"{winner} is winner with {winner_points} points")
else:
    print(f"{firs_player_name} has {first_player_points} points")
    print(f"{second_player_name} has {second_player_points} points")

