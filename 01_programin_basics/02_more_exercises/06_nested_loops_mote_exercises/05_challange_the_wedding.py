men_number = int(input())
women_number = int(input())
maximum_tables = int(input())
counter = 0
for current_man in range(1, men_number + 1):
    for current_woman in range(1, women_number + 1):
        counter += 1
        if maximum_tables < counter:
            break
        else:
            print(f"({current_man} <-> {current_woman})", end = " ")
