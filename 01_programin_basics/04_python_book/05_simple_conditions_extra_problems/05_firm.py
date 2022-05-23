import math

needed_hours = int(input())
days = int(input())
workers = int(input())
hours = math.floor((days * 8 * 0.9 + days * 2) * workers)
diff = abs(needed_hours - hours)
if hours <= needed_hours:
    print(f"Yes!{math.floor(diff)} hours left.")
else:
    print(f"Not enough time!{math.floor(diff)} hours needed.")