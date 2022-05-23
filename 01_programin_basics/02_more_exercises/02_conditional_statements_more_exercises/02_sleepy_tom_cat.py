vacation_days = int(input())

play_minutes = 30000
workday_play_minutes = 63
vacationday_play_minutes = 127

work_days = 365 - vacation_days

play_time = vacation_days * vacationday_play_minutes + work_days * workday_play_minutes
diference = abs(play_time - play_minutes)
h = diference // 60
m = diference % 60

if play_time > play_minutes:
    print("Tom will run away")
    print(f"{h} hours and {m} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{h} hours and {m} minutes less for play")