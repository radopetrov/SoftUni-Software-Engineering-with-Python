eggs_available = int(input())
command = input()
is_no_more_eggs = False
sold_eggs = 0
while command != "Close":
    eggs_number = int(input())
    if command == "Buy":
        if eggs_number > eggs_available:
            is_no_more_eggs = True
            break
        else:
            eggs_available -= eggs_number
            sold_eggs += eggs_number
    elif command == "Fill":
        eggs_available += eggs_number
    command = input()
if is_no_more_eggs:
    print("Not enough eggs in store!")
    print(f"You can buy only {eggs_available}.")
else:
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")