import math

tournaments_number = int(input())
start_points = int(input())
won_tournaments = 0
won_points = 0
for i in range(tournaments_number):
    tournament_place = input()
    if tournament_place == "W":
        won_tournaments += 1
        won_points += 2000
    elif tournament_place == "F":
        won_points += 1200
    elif tournament_place == "SF":
        won_points += 720
total_points = won_points + start_points
average_poits_per_tournament = won_points / tournaments_number
won_tournaments_percent = won_tournaments / tournaments_number * 100
print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_poits_per_tournament)}")
print(f"{won_tournaments_percent:.2f}%")