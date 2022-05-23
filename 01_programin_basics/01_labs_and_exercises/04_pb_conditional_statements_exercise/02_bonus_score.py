starter_bonus = int(input())
bonus = 0
if starter_bonus <= 100:
    bonus += 5
elif starter_bonus <= 1000:
    bonus += starter_bonus * 20 / 100
elif starter_bonus > 1000:
    bonus += starter_bonus * 10 / 100
if starter_bonus % 2 == 0:
    bonus += 1
if starter_bonus % 10 == 5:
    bonus += 2


total_points = bonus + starter_bonus

print(bonus)
print(total_points)