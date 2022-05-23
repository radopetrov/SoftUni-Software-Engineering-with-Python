import math

figure = input()
side = float(input())
area = 0
if figure == "square":
    area = side ** 2
elif figure == "rectangle":
    side_b = float(input())
    area = side * side_b
elif figure == "circle":
    area = math.pi * (side ** 2)
elif figure == "triangle":
    side_b = float(input())
    area = side * side_b / 2
print(f"{area:.3f}")