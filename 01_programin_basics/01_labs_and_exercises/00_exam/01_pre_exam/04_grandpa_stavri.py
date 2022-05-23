days = int(input())
rakia_total_qty = 0
rakia_total_degrees = 0
for current_day in range(days):
    rakia_qty = float(input())
    degrees = float(input())
    rakia_total_qty += rakia_qty
    rakia_total_degrees += (rakia_qty * degrees)
average_degrees = rakia_total_degrees / rakia_total_qty
print(f"Liter: {rakia_total_qty:.2f}")
print(f"Degrees: {average_degrees:.2f}")
if average_degrees < 38:
    print(f"Not good, you should baking!")
elif average_degrees <= 42:
    print(f"Super!")
elif average_degrees > 42:
    print(f"Dilution with distilled water!")