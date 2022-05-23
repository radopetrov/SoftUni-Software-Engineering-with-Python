start = int(input())
finish = int(input())
magic_number = int(input())
combination = 0
is_sum = False
for firs_number in range(start, finish + 1):
    for second_number in range(start, finish + 1):
        sumed_numbers = firs_number + second_number
        combination += 1
        if sumed_numbers == magic_number:
            print(f"Combination N:{combination} ({firs_number} + {second_number} = {magic_number})")
            is_sum = True
            break
    if is_sum:
            break
if not is_sum:
    print(f"{combination} combinations - neither equals {magic_number}")