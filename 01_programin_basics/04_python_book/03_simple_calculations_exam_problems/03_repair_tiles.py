n = int(input())  # side of the ground in meters
w = float(input())  # width of the tile in meters
l = float(input())  # length of the tile in meters
m = int(input())  # width of the bench in meters
o = int(input())  # length of the bench in meters
ground_area = (n ** 2) - (m * o)
tile_area = w * l
tile_number = ground_area / tile_area
time = tile_number * 0.2
# output
# 1.number of tiles
# 2.total time for placing them
print(tile_number)
print(time)