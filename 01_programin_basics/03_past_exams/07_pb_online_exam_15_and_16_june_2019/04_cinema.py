hall_seats = int(input())
command = input()
total_income = 0
hall_is_full = False
while command != "Movie time!":
    command = int(command)
    if command <= hall_seats:
        hall_seats -= command
        if command % 3 == 0:
            total_income += (command * 5) - 5
        else:
            total_income += command * 5
    else:
        hall_is_full = True
        break
    command = input()
if hall_is_full:
    print("The cinema is full.")
else:
    print(f"There are {hall_seats} seats left in the cinema.")
print(f"Cinema income - {total_income} lv.")