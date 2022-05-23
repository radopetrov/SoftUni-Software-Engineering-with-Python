start = input()
end = input()
# for current_barcode in range(int(barcode_start), int(barcode_end) + 1):
#     is_odd = True
#     for current_digit in str(current_barcode):
#         if int(current_digit) % 2 == 0:
#             is_odd = False
#             break
#     if is_odd:
#         print(current_barcode, end = " ")
for first_digit in range(int(start[0]), int(end[0]) + 1):
    for second_digit in range(int(start[1]), int(end[1]) + 1):
        for third_digit in range(int(start[2]), int(end[2]) + 1):
            for fourth_digit in range(int(start[3]), int(end[3]) + 1):
                if first_digit % 2 != 0 and second_digit % 2 != 0 and third_digit % 2 != 0 and fourth_digit % 2 != 0:
                    print(f"{first_digit}{second_digit}{third_digit}{fourth_digit}", end = " ")
