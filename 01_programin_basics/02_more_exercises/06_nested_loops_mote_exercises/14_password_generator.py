number_n = int(input())  # from [1 to 9]
number_l = int(input())  # from [1 to 9]
# symbol 1 - [1 to n]
# symbol 2 - [1 to n]
# symbol 3 - [the first lower letters to number l]
# symbol 4 - [the first lower letters to number l]
# symbol 5 - [1 to n bigger than the first 2 numbers]
# output format - 11aa2

for first_digit in range(1, number_n + 1):
    for second_digit in range(1, number_n + 1):
        for third_digit in range(ord("a"), ord("a") + number_l):
            for fourth_digit in range(ord("a"), ord("a") + number_l):
                for fifth_digit in range(1, number_n + 1):
                    if fifth_digit > first_digit and fifth_digit > second_digit:
                        print(f"{first_digit}{second_digit}{chr(third_digit)}{chr(fourth_digit)}{fifth_digit}", end = " ")
                    else:
                        continue
