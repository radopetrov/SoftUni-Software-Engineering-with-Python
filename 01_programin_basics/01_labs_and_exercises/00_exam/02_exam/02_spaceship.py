import math

spaceship_width = float(input())
spaceship_length = float(input())
spaceship_height = float(input())
average_astronaut_height = float(input())
spaceship_volume = spaceship_height * spaceship_width * spaceship_length
one_cabin_volume = (average_astronaut_height + 0.4) * 2 * 2
cabins_number = math.floor(spaceship_volume / one_cabin_volume)
if 3 <= cabins_number <= 10:
    print(f"The spacecraft holds {cabins_number} astronauts." )
elif cabins_number < 3:
    print(f"The spacecraft is too small.")
else:
    print(f"The spacecraft is too big.")