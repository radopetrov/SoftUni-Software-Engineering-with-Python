old_record = float(input())
distance = float(input())
seconds_per_meter = float(input())
delay = (distance // 50) * 30
george_time = (seconds_per_meter * distance) + delay
time_diference = abs(george_time - old_record)
if george_time < old_record:
    print(f"Yes! The new record is {george_time:.2f} seconds.")
else:
    print(f"No! He was {time_diference:.2f} seconds slower.")
