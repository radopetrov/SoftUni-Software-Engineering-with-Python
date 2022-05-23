age = int(input())
washing_machine_price = float(input())
toy_price_per_number = int(input())
toys_number = 0
money = 0
stolen_money = 0
for current_age in range(1, age + 1):
    if current_age % 2 == 0:
        money += 10 * (current_age // 2)
        stolen_money += 1
    else:
        toys_number += 1

money -= stolen_money
toys_profit = toys_number * toy_price_per_number
total_money = money + toys_profit
dif = abs(total_money - washing_machine_price)
if total_money >= washing_machine_price:
    print(f"Yes! {dif:.2f}")
else:
    print(f"No! {dif:.2f}")