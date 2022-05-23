from math import pi

radiuis = float(input())

diameter = radiuis * 2

circle_perimeter = diameter * pi
circle_area = pi * (radiuis * radiuis)

#"<calculated area>" "<calculated parameter>".

print(format(circle_area, '.2f'))
print(format(circle_perimeter, '.2f'))
