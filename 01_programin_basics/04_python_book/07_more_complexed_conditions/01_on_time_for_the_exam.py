starting_hours = int(input())
starting_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

starting_time = starting_hours * 60 + starting_minutes
arrival_time = arrival_hours * 60 + arrival_minutes

minutes_diff = abs(starting_time - arrival_time) % 60
hours_diff = abs(arrival_time - starting_time) // 60

if 0 <= (starting_time - arrival_time) <= 30:
    print("On time")
    print(f"{minutes_diff} minutes before the start")
elif (starting_time - arrival_time) > 30:
    print("Early")
    if abs(arrival_time - starting_time) < 60:
        print(f"{minutes_diff} minutes before the start")
    else:
        print(f"{hours_diff}:{minutes_diff:02d} hours before the start")
else:
    print("Late")
    if abs(arrival_time - starting_time) < 60:
        print(f"{minutes_diff} minutes after the start")
    else:
        print(f"{hours_diff}:{minutes_diff:02d} hours after the start")