cargo_number = int(input())
minibus_cargo_number = 0
minibus_cargo_weight = 0
truck_cargo_number = 0
truck_cargo_weight = 0
train_cargo_number = 0
train_cargo_weight = 0
minibus_price_pre_tone = 200
truck_price_pre_tone = 175
train_price_pre_tone = 120
for number in range (cargo_number):
    cargo_weight = int(input())
    if cargo_weight <= 3:
        minibus_cargo_number += 1
        minibus_cargo_weight += cargo_weight
    elif cargo_weight <= 11:
        truck_cargo_number += 1
        truck_cargo_weight += cargo_weight
    else:
        train_cargo_number += 1
        train_cargo_weight += cargo_weight
minibus_total_price = minibus_price_pre_tone * minibus_cargo_weight
truck_total_price = truck_price_pre_tone * truck_cargo_weight
train_total_price = train_price_pre_tone * train_cargo_weight
total_cargo_weight = minibus_cargo_weight + truck_cargo_weight + train_cargo_weight
average_price_per_tone = (train_total_price + truck_total_price + minibus_total_price) / total_cargo_weight
minibus_percent_weight = minibus_cargo_weight / total_cargo_weight * 100
truck_percent_weight = truck_cargo_weight / total_cargo_weight * 100
train_percent_weight = train_cargo_weight / total_cargo_weight * 100
print(f"{average_price_per_tone:.02f}")
print(f"{minibus_percent_weight:.02f}%")
print(f"{truck_percent_weight:.02f}%")
print(f"{train_percent_weight:.02f}%")