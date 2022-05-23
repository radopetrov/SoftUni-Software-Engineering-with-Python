start_digit = int(input())
last_digit = int(input())

for first_digit in range(start_digit, last_digit + 1):
    for second_digit in range(start_digit, last_digit + 1):
        for third_digit in range(start_digit, last_digit + 1):
            for fourth_digit in range(start_digit, last_digit + 1):
                if (first_digit % 2 == 0 and fourth_digit % 2 != 0) or (first_digit % 2 != 0 and fourth_digit % 2 == 0):
                    if first_digit > fourth_digit:
                        if (second_digit + third_digit) % 2 == 0:
                            print(f""
                                  f"{first_digit}{second_digit}{third_digit}{fourth_digit}", end = " ")