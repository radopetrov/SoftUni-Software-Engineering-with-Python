egg_size = input()
egg_color = input()
pack_number = int(input())
pack_price = 0
if egg_color == "Red":
    if egg_size == "Large":
        pack_price = 16
    elif egg_size == "Medium":
        pack_price = 13
    elif egg_size == "Small":
        pack_price = 9
elif egg_color == "Green":
    if egg_size == "Large":
        pack_price = 12
    elif egg_size == "Medium":
        pack_price = 9
    elif egg_size == "Small":
        pack_price = 8
elif egg_color == "Yellow":
    if egg_size == "Large":
        pack_price = 9
    elif egg_size == "Medium":
        pack_price = 7
    elif egg_size == "Small":
        pack_price = 5
total_profit = (pack_price * pack_number) * 0.65
print(f"{total_profit:.2f} leva.")