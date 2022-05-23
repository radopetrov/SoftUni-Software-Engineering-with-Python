import math
figure = str(input())
side_a = float(input())
figure_area = 0
if figure == "square":
    figure_area = side_a ** 2
elif figure == "rectangle":
    side_b = float(input())
    figure_area = side_a * side_b
elif figure == "circle":
    figure_area = math.pi * (side_a ** 2)
elif figure == "triangle":
    h = float(input())
    figure_area = side_a * h / 2
print(f"{figure_area:.3f}")
