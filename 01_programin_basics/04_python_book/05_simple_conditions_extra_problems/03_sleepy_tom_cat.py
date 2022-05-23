holidays = int(input())
holidays_play_time = holidays * 127
workdays_play_time = (365 - holidays) * 63
total_play_time = workdays_play_time + holidays_play_time
diff = abs(total_play_time - 30000)
hours = diff // 60
minutes = diff % 60
if total_play_time > 30000:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
elif total_play_time < 30000:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")