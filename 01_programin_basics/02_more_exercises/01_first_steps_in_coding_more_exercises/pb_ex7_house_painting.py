side_x = float(input())
side_y = float(input())
side_h = float(input())

door_side_a = 1.2
door_side_b = 2
window_side = 1.5
one_liter_green_paint = 3.4
one_liter_red_paint = 4.3

front_back_area = (side_x * side_x) * 2
side_area = (side_x * side_y) * 2
door_windows_area = door_side_a * door_side_b + (window_side * window_side) * 2

green_paint_area = front_back_area + side_area - door_windows_area

rooftop_front_back_area = (side_x * side_h / 2) * 2
rooftop_side_area = (side_x * side_y) * 2

red_paint_area = rooftop_side_area + rooftop_front_back_area

green_paint_liter = green_paint_area / one_liter_green_paint
red_paint_liter = red_paint_area / one_liter_red_paint

print(format(green_paint_liter, '.2f'))
print(format(red_paint_liter, '.2f'))
