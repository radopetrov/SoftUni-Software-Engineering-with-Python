desired_profit = float(input())
cocktail_name = input()
daily_profit = 0
target_reached = False
while cocktail_name != "Party!":
    cocktail_number = int(input())
    cocktail_price = len(cocktail_name)
    total_bill = cocktail_price * cocktail_number
    if total_bill % 2 != 0:
        total_bill *= 0.75
    daily_profit += total_bill
    if daily_profit >= desired_profit:
        target_reached = True
        break
    cocktail_name = input()
if target_reached:
    print("Target acquired.")
else:
    differance = abs(desired_profit - daily_profit)
    print(f"We need {differance:.2f} leva more.")
print(f"Club income - {daily_profit:.2f} leva.")