days = int(input())

total_wins = 0
total_losses = 0
total_money = 0
for current_day in range(1, days + 1):
    won_money_current_day = 0
    wins_current_day = 0
    losses_current_day = 0
    sport = input()
    while sport != "Finish":
        result = input()
        if result == "win":
            total_wins += 1
            wins_current_day += 1
            won_money_current_day += 20
        elif result == "lose":
            total_losses += 1
            losses_current_day += 1
        sport = input()
    if wins_current_day > losses_current_day:
        won_money_current_day *= 1.1
        total_money += won_money_current_day
    else:
        total_money += won_money_current_day

if total_wins > total_losses:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")