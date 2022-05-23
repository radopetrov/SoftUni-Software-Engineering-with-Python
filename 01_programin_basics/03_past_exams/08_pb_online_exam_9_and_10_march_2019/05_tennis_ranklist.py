import math

tours_number = int(input())
starter_points = int(input())
tours_points = 0
wins_counter = 0
for number in range(tours_number):
    tour_state = input()
    if tour_state == "W":
        tours_points += 2000
        wins_counter += 1
    elif tour_state == "F":
        tours_points += 1200
    elif tour_state == "SF":
        tours_points += 720
total_points = starter_points + tours_points
average = tours_points / tours_number
wins_rate = wins_counter / tours_number * 100
print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average)}")
print(f"{wins_rate:.2f}%")