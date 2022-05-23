daily_target = int(input())
command = input()
daily_profits = 0
is_target_reached = False
while command != "closed":
    command_type = input()
    price = 0
    if command == "haircut":
        if command_type == "mens":
            price = 15
        elif command_type == "ladies":
            price = 20
        elif command_type == "kids":
            price = 10
    elif command == "color":
        if command_type == "touch up":
            price = 20
        elif command_type == "full color":
            price = 30
    daily_profits += price
    if daily_profits >= daily_target:
        is_target_reached = True
        break
    command = input()
if is_target_reached:
    print(f"You have reached your target for the day!")
else:
    difference = abs(daily_profits - daily_target)
    print(f"Target not reached! You need {difference}lv. more.")
print(f"Earned money: {daily_profits}lv.")