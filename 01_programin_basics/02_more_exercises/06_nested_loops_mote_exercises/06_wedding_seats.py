last_section = input()
rows_firs_section = int(input())  # на всяка следваща секция се увеличават с 1
seats_odd_rows = int(input())  # четните редове са с 2 места повече
seats_counter = 0
for current_section in range(ord("A"), ord(last_section) + 1):
    for current_row in range(1, rows_firs_section + 1):
        if current_row % 2 != 0:  # нечетен ред
            for current_seat in range(ord("a"), ord("a") + seats_odd_rows):
                seats_counter += 1
                print(f"{chr(current_section)}{current_row}{chr(current_seat)}")
        else:  # четен ред
            for current_seat in range(ord("a"), ord("a") + seats_odd_rows + 2):
                seats_counter += 1
                print(f"{chr(current_section)}{current_row}{chr(current_seat)}")
    rows_firs_section += 1
print(seats_counter)