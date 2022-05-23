number = int(input())
p1 = 0
p2 = 0
p3 = 0
for numbers in range(number):
    num = int(input())
    if num % 2 == 0:
        p1 += 1
    if num % 3 == 0:
        p2 += 1
    if num % 4 == 0:
        p3 += 1
p1_rate = p1 / number * 100
p2_rate = p2 / number * 100
p3_rate = p3 / number * 100
print(f"{p1_rate:.02f}%\n{p2_rate:.02f}%\n{p3_rate:.02f}%")