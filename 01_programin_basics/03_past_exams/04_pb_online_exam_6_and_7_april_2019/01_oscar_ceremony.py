hall_rent = int(input())
statues = hall_rent * 0.7
catering = statues * 0.85
sound = catering / 2
total_expences = hall_rent + statues + catering + sound
print(f"{total_expences:.02f}")