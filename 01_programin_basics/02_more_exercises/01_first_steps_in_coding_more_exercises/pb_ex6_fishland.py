skumriya_price = float(input())
caca_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

midi_price = 7.50

palamud_price = skumriya_price * 1.6
safrid_price = caca_price * 1.8

palamud_value = palamud_price * palamud_kg
safrid_value = safrid_price * safrid_kg
midi_value = midi_kg * midi_price

total_value = palamud_value + safrid_value + midi_value

print(format(total_value, '.2f'))