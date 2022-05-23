k = int(input())
l = int(input())
m = int(input())
n = int(input())
change_counter = 0
is_changes_limit_reached = False
for pl11 in range(k, 8 + 1):
    for pl12 in range(9, l - 1, -1):
        for pl21 in range(m, 8 + 1):
            for pl22 in range(9, n - 1, -1):
                if (pl11 % 2 == 0 and pl21 % 2 == 0 and pl12 % 2 != 0 and pl22 % 2 != 0) and int(f"{pl11}{pl12}") != int(f"{pl21}{pl22}"):
                    print(f"{pl11}{pl12} - {pl21}{pl22}")
                    change_counter += 1
                    if change_counter == 6:
                        is_changes_limit_reached = True
                        break
                elif pl11 % 2 == 0 and pl21 % 2 == 0 and pl12 % 2 != 0 and pl22 % 2 != 0 and int(f"{pl11}{pl12}") == int(f"{pl21}{pl22}"):
                    print("Cannot change the same player.")
            if is_changes_limit_reached:
                break
        if is_changes_limit_reached:
            break
    if is_changes_limit_reached:
        break
