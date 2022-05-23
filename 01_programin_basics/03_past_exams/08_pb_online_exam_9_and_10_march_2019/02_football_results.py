won_games = 0
lost_games = 0
drawn_games = 0
for number in range(3):
    results = str(input())
    home_team_result = results[0]
    guest_team_result = results[2]
    if home_team_result > guest_team_result:
        won_games += 1
    elif home_team_result < guest_team_result:
        lost_games += 1
    else:
        drawn_games += 1
print(f"Team won {won_games} games.")
print(f"Team lost {lost_games} games.")
print(f"Drawn games: {drawn_games}")