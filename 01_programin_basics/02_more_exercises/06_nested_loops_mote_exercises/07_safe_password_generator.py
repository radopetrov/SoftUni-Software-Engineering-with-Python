row_a = int(input())
row_b = int(input())
maximum_generated_passwords = int(input())
is_max_passwords_reached = False
count_loop = 0
for A in range(35, 55 + 1):
    for B in range(64, 96 + 1):
        for x in range(1, row_a + 1):
            for y in range(1, row_b + 1):
                if x + y == 2:
                    count_loop += 1
                    if count_loop > 1:
                        is_max_passwords_reached = True
                        break
                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end = "|")
                if A == 55:
                    A = 35
                else:
                    A += 1
                if B == 96:
                    B = 64
                else:
                    B += 1
                maximum_generated_passwords -= 1
                if maximum_generated_passwords <= 0:
                    is_max_passwords_reached = True
                    break
            if is_max_passwords_reached:
                break
        if is_max_passwords_reached:
            break
    if is_max_passwords_reached:
        break
