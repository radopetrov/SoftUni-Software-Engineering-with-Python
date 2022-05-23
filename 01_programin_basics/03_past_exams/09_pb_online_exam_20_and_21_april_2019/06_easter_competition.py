easter_breads_number = int(input())
winner_points = 0
winner_name = ""
for current_bread in range(easter_breads_number):
    baker_name = input()
    points = input()
    current_baker_points = 0
    while points != "Stop":
        current_baker_points += int(points)
        points = input()
    if current_baker_points > winner_points:
        winner_name = baker_name
        winner_points = current_baker_points
    print(f"{baker_name} has {current_baker_points} points.")
    if baker_name == winner_name:
        print(f"{baker_name} is the new number 1!")
print(f"{winner_name} won competition with {winner_points} points!")