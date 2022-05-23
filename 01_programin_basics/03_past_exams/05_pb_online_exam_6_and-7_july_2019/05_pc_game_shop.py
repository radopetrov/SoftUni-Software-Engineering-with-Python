sold_games_number = int(input())
hearthstone_count = 0
fornite_count = 0
overwatch_count = 0
others_count = 0
for number in range(sold_games_number):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone_count += 1
    elif game_name == "Fornite":
        fornite_count += 1
    elif game_name == "Overwatch":
        overwatch_count += 1
    else:
        others_count += 1
hearthstone_rate = hearthstone_count / sold_games_number * 100
fornite_rate = fornite_count / sold_games_number * 100
overwatch_rate = overwatch_count / sold_games_number * 100
others_rate = others_count / sold_games_number * 100
print(f"Hearthstone - {hearthstone_rate:.2f}%")
print(f"Fornite - {fornite_rate:.2f}%")
print(f"Overwatch - {overwatch_rate:.2f}%")
print(f"Others - {others_rate:.2f}%")