first_player_eggs = int(input())
second_player_eggs = int(input())
command = input()
is_first_player_winner = False
while command != "End of battle":
    if command == "one":
        second_player_eggs -= 1
    elif command == "two":
        first_player_eggs -= 1
    if first_player_eggs == 0:
        break
    elif second_player_eggs == 0:
        is_first_player_winner = True
        break
    command = input()
if command == "End of battle":
    print(f"Player one has {first_player_eggs} eggs left.")
    print(f"Player two has {second_player_eggs} eggs left.")
elif is_first_player_winner:
    print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
elif not is_first_player_winner:
    print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")

