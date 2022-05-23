control_minutes = int(input())
control_seconds = int(input())
beehive_lenght = float(input())
seconds_per_100m = int(input())
control_time = control_seconds + (control_minutes * 60)
delay = (beehive_lenght / 120) * 2.5
bangiev_time = (seconds_per_100m * beehive_lenght / 100) - delay
if bangiev_time <= control_time:
    print(f"Marin Bangiev won an Olympic quota!\nHis time is {bangiev_time:.3f}.")
else:
    diference = abs(bangiev_time - control_time)
    print(f"No, Marin failed! He was {diference:.3f} second slower.")