tournament = input()
matches_played = 0
matches_won = 0
matches_lost = 0
while tournament != "End of tournaments":
    match_number = int(input())
    for current_match in range(1, match_number + 1):
        matches_played += 1
        desi_team_points = int(input())
        other_team_points = int(input())
        difference_team_points = abs(desi_team_points - other_team_points)
        if desi_team_points > other_team_points:
            matches_won += 1
            print(f"Game {current_match} of tournament {tournament}: win with {difference_team_points} points.")
        else:
            matches_lost += 1
            print(f"Game {current_match} of tournament {tournament}: lost with {difference_team_points} points.")
    tournament = input()
won_matches_shares = matches_won / matches_played * 100
lost_matches_shares = matches_lost / matches_played * 100
print(f"{won_matches_shares:.2f}% matches win")
print(f"{lost_matches_shares:.2f}% matches lost")
