n = int(input())
star = "*"
space = " "
for i in range(n):
    if i == 0 or i == n - 1:
        print(star * n)
    else:
        print(f"{star}{space * (n-2)}{star}")