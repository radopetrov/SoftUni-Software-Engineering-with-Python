kozunatsi_number = int(input())
eggs_pack_number = int(input())
bisquit_kg = int(input())
kozunatsi_price = kozunatsi_number * 3.2
eggs_pack_price = eggs_pack_number * 4.35
eggs_paint_price = eggs_pack_number * 12 * 0.15
bisquits_price = bisquit_kg * 5.40
total_costs = kozunatsi_price + eggs_pack_price + eggs_paint_price + bisquits_price
print(f"{total_costs:.2f}")
