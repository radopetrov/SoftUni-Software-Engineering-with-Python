import math

project_hours = int(input())
project_days = int(input())
workers_overtime = int(input())

work_days = project_days * 0.9
overtime_hours = project_days * workers_overtime * 2
total_work_hours = math.floor(work_days * 8 + overtime_hours)
time_difference = abs(project_hours - total_work_hours)

if total_work_hours >= project_hours:
    print(f"Yes!{time_difference} hours left.")
else:
    print(f"Not enough time!{time_difference} hours needed.")