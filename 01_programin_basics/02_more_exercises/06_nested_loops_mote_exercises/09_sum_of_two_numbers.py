first_number = int(input())
last_number = int(input())
magic_number = int(input())
combination = 0
is_magic_number = False
for current_first_number in range(first_number, last_number + 1):
    for current_second_number in range(first_number, last_number +1):
        combination += 1
        if current_first_number + current_second_number == magic_number:
            is_magic_number = True
            break
    if is_magic_number:
        break
if is_magic_number:
    print(f"Combination N:{combination} ({current_first_number} + {current_second_number} = {magic_number})")
else:
    print(f"{combination} combinations - neither equals {magic_number}")
