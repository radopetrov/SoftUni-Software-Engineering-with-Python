total_eggs = int(input())
red_counter = 0
orange_counter = 0
blue_counter = 0
green_counter = 0
max_eggs_number = 0
max_eggs_color = ""
for current_egg in range(total_eggs):
    egg_color = input()
    if egg_color == "red":
        red_counter += 1
    elif egg_color == "orange":
        orange_counter += 1
    elif egg_color == "blue":
        blue_counter += 1
    elif egg_color == "green":
        green_counter += 1
if red_counter > orange_counter and red_counter > blue_counter and \
    red_counter > green_counter:
    max_eggs_number = red_counter
    max_eggs_color = "red"
elif orange_counter > red_counter and orange_counter > blue_counter and \
    orange_counter > green_counter:
    max_eggs_number = orange_counter
    max_eggs_color = "green"
elif blue_counter > red_counter and blue_counter > orange_counter and \
    blue_counter > green_counter:
    max_eggs_number = blue_counter
    max_eggs_color = "blue"
else:
    max_eggs_number = green_counter
    max_eggs_color = "green"
print(f"Red eggs: {red_counter}")
print(f"Orange eggs: {orange_counter}")
print(f"Blue eggs: {blue_counter}")
print(f"Green eggs: {green_counter}")
print(f"Max eggs: {max_eggs_number} -> {max_eggs_color}")