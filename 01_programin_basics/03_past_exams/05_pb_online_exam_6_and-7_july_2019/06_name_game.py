name = input()
winner_name = ""
winner_points = 0
while name != "Stop":
    current_player_points = 0
    for current_letter in name:
        player_numbers = int(input())
        if ord(current_letter) == player_numbers:
            current_player_points += 10
        else:
            current_player_points += 2
    if current_player_points > winner_points:
        winner_name = name
        winner_points = current_player_points
    elif current_player_points == winner_points:
        winner_name = name
        winner_points = current_player_points
    name = input()
print(f"The winner is {winner_name} with {winner_points} points!")