n = int(input())
m = int(input())
s = int(input())

for current_address in range(m, n - 1, -1):
    if current_address % 2 == 0 and current_address % 3 == 0 and current_address != s:
        print(current_address, end = " ")
    elif current_address % 2 == 0 and current_address % 3 == 0 and current_address == s:
        break
