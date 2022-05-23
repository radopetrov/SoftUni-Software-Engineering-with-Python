import math

wall_height = int(input())
wall_width = int(input())
white_spaces_percentage = int(input())
command = input()
total_paint_area = math.ceil((wall_height * wall_width * 4) * ((100 - white_spaces_percentage) / 100))
paint_is_enough = False
while command != "Tired!":
    command = int(command)
    total_paint_area -= command
    if total_paint_area > 0:
        command = input()
        continue
    else:
        paint_is_enough = True
        break

if paint_is_enough:
    if total_paint_area == 0:
        print("All walls are painted! Great job, Pesho!")
    else:
        print(f"All walls are painted and you have {abs(total_paint_area)} l paint left!")
else:
    print(f"{abs(total_paint_area)} quadratic m left.")