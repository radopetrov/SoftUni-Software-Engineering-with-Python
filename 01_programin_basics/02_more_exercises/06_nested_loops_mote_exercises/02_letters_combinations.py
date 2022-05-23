start_letter = input()
last_letter = input()
missing_letter = input()
start_number = ord(start_letter)
last_number = ord(last_letter)
missing_number = ord(missing_letter)
counter = 0
letter_one = ""
letter_two = ""
letter_three = ""
for first_digit in range(start_number, last_number + 1):
    if first_digit != missing_number:
        letter_one = chr(first_digit)
    else:
        continue
    for second_digit in range(start_number, last_number +1):
        if second_digit != missing_number:
            letter_two = chr(second_digit)
        else:
            continue
        for third_digit in range(start_number, last_number + 1):
            if third_digit != missing_number:
                letter_three = chr(third_digit)
            else:
                continue
            counter += 1
            print(f"{letter_one}{letter_two}{letter_three}", end = " ")
print(counter)