width = int(input())
lenght = int(input())
height = int(input())
total_volume = width * lenght * height
command = input()
moved_boxes = 0
while command !="Done":
    number_of_boxes = int(command)
    moved_boxes += number_of_boxes
    if moved_boxes > total_volume:
        break
    command = input()
diff = abs(moved_boxes - total_volume)
if moved_boxes > total_volume:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")