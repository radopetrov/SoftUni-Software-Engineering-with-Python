first_number_upper_limit = int(input())
second_number_upper_limit = int(input())
third_number_upper_limit = int(input())
first_digit = 0
second_digit = 0
third_digit = 0
for first_number in range(1, first_number_upper_limit + 1):
    if first_number % 2 != 0:
        continue
    else:
        first_digit = first_number
    for second_number in range(2, second_number_upper_limit + 1):
            if second_number in [2, 3, 5, 7]:
                second_digit = second_number
            else:
                continue
            for third_number in range(1, third_number_upper_limit + 1):
                if third_number % 2 == 0:
                    third_digit = third_number
                else:
                    continue
                print(f"{first_digit} {second_digit} {third_digit}")
