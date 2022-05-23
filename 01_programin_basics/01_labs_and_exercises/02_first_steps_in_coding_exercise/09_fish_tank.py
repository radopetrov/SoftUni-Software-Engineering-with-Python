lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

aquarium = (lenght * width * height) * 0.001
water = aquarium - (aquarium * (percent / 100))
print(water)
