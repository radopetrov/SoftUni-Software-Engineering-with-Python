first = int(input())
second = int(input())
third = int(input())
total_time = first + second + third
minutes = total_time // 60
seconds = total_time % 60
print(f"{minutes}:{seconds:02d}")