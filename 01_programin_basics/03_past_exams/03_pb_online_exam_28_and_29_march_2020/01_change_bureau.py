bitcoin_number = int(input())
ch_yoan_number = float(input())
commition = float(input())

leva_1 = bitcoin_number * 1168
usd = ch_yoan_number * 0.15
leva_2 = usd * 1.76
euro = ((leva_1 + leva_2) / 1.95) * ((100 - commition) / 100)
print(f"{euro:.2f}")