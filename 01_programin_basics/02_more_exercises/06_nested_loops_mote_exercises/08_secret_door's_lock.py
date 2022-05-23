first_digit_limit = int(input())
second_digit_limit = int(input())
third_digit_limit = int(input())

for first_digit in range(1, first_digit_limit + 1):
    if first_digit % 2 != 0:
        continue
    for second_digit in range(1, second_digit_limit + 1):
        if second_digit in [2, 3, 5, 7]:
            for third_digit in range(1, third_digit_limit + 1):
                if third_digit % 2 != 0:
                    continue
                print(f"{first_digit} {second_digit} {third_digit}")
