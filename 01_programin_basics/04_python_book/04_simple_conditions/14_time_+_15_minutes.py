old_hour = int(input())
old_minutes = int(input())
total_minutes = old_hour * 60 + old_minutes + 15
hour = total_minutes // 60
if hour == 24:
    hour = 0
minutes = total_minutes % 60
print(f"{hour}:{minutes:02d}")