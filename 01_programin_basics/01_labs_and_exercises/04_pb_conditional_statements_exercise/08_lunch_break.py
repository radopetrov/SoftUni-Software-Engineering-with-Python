import math

tv_show_name = str(input())
tv_show_lenght = int(input())
break_time = int(input())

lunch_time = break_time /8
resting_time = break_time / 4

time_for_tv_show = break_time - (lunch_time + resting_time)

time_differance = abs(time_for_tv_show - tv_show_lenght)
time_differance = math.ceil(time_differance)

if time_for_tv_show >= tv_show_lenght:
    print(f"You have enough time to watch {tv_show_name} and left with {time_differance} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_show_name}, you need {time_differance} more minutes.")