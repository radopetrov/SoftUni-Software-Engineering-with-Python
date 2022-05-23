room_h = float(input())
room_w = float(input())

# desk_side_a = 70 / 100
# desk_side_b = 40 / 100
# chair_side_a = 70 / 100
# chair_side_b = 80 / 100
# coridor_width = 100 / 100
# workplace_side_a = 70 / 100
# woorplace_side_b = 120 / 100
# teacher_desk_side_a = 160 / 100
# teacher_desk_side_b = 120 / 100
#
# workplace_area = desk_side_a * desk_side_b + chair_side_a * chair_side_b
# coridor_area = coridor_width * room_w
# techer_desk_area = teacher_desk_side_a * teacher_desk_side_b
# door_area = workplace_area
#
# room_area = room_w * room_h
#
# all_worlplace_area = room_area - (coridor_area + techer_desk_area + door_area)
# workplace_number = all_worlplace_area // workplace_area
#
# print(workplace_number)
# count_width = ((room_w * 100) - 100) // 70
# count_height = (room_h * 100) // 120
# total_count = count_width * count_width - 300
# print(total_count)
room_h *= 100
room_w *= 100

room_w_count = (room_w - 100) // 70
room_h_count = (room_h // 120)
total_count = room_h_count * room_w_count - 3
print(total_count)