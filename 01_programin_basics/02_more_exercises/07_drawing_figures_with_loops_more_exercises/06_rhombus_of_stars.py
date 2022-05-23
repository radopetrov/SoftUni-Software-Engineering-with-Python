n = int(input())
for row in range(1, n + 1):
    print((n - row) * " " + row * "* ", end = "")
    print()
for col in range(n - 1, 0, -1):
    print((n - col) * " " + col * "* ", end = "")
    print()
