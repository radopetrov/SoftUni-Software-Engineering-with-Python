distance = int(input())
daytime = input()
total_price = 0
if distance < 20:  #taxi
    if daytime == "day":
        total_price = 0.7 + 0.79 * distance
    elif daytime == "night":
        total_price = 0.7 + 0.9 * distance
elif 20 <= distance < 100:  # bus
    total_price = distance * 0.09
else:  #train
    total_price = distance * 0.06
print(total_price)