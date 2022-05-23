vacation_cost = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzles_price = 2.60
dolls_price = 3
bears_price = 4.10
minions_price = 8.20
trucks_price = 2

total_price = puzzles * puzzles_price + dolls * dolls_price + bears * bears_price + minions * minions_price + trucks * trucks_price

toys_number = puzzles + dolls + bears + minions + trucks

if toys_number >= 50:
    total_price -= total_price * 25 / 100

total_price -= total_price * 10 / 100

left_money = abs(vacation_cost-total_price)

if total_price >= vacation_cost:
    print(f"Yes! {left_money:.2f} lv left.")
else:
    print(f"Not enough money! {left_money:.2f} lv needed.")
