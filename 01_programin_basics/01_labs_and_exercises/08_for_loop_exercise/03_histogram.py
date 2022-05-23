n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(0, n):
    number = int(input())
    if number < 200:
        p1 += 1
    elif number < 400:
        p2 += 1
    elif number < 600:
        p3 += 1
    elif number < 800:
        p4 += 1
    elif number >= 800:
        p5 += 1
p1_percent = p1 / n * 100
p2_percent = p2 / n * 100
p3_percent = p3 / n * 100
p4_percent = p4 / n * 100
p5_percent = p5 / n * 100
print(f"{p1_percent:.2f}%\n{p2_percent:.2f}%\n{p3_percent:.2f}%\n{p4_percent:.2f}%\n{p5_percent:.2f}%")
