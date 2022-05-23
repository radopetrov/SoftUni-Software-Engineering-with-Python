bitcoin = int(input())
chinese_yuans = float(input())
commision_fee = float(input())
bgn = 0
bgn += bitcoin * 1168
usd = chinese_yuans * 0.15
bgn += usd * 1.76
euro = bgn / 1.95
euro *= (100 - commision_fee) / 100
print(f"{euro:.2f}")
