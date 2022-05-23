team_name = input()
games_played = int(input())
team_has_played = True
won_games = 0
draw_games = 0
lost_games = 0
total_points = 0
if games_played == 0:
    team_has_played = False
else:
    for games in range(games_played):
        result = input()
        if result == "W":
            won_games += 1
            total_points += 3
        elif result == "D":
            draw_games += 1
            total_points += 1
        elif result == "L":
            lost_games += 1
if team_has_played:
    win_rate = won_games / games_played * 100
    print(f"{team_name} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {won_games}")
    print(f"## D: {draw_games}")
    print(f"## L: {lost_games}")
    print(f"Win rate: {win_rate:.2f}%")
else:
    print(f"{team_name} hasn't played any games during this season.")