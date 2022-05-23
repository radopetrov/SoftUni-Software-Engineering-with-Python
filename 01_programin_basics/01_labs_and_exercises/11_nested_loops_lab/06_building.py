floors = int(input())
rooms = int(input())
room_type = ""
for current_floor in range(floors, 0, -1):
    if current_floor == floors:
        room_type = "L"
    elif current_floor % 2 == 0:
        room_type = "O"
    elif current_floor % 2 != 0:
        room_type = "A"
    for current_room in range(rooms):
        print(f"{room_type}{current_floor}{current_room}", end = " ")
    print()