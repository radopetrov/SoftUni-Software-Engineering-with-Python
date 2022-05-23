dancers_number = int(input())
points = float(input())
season = input()
location = input()
money_prize = 0
if location == "Bulgaria":
    money_prize = points * dancers_number
    if season == "summer":
        money_prize *= 0.95
    elif season == "winter":
        money_prize *= 0.92
elif location == "Abroad":
    money_prize = (dancers_number * points) * 1.5
    if season == "summer":
        money_prize *= 0.9
    elif season == "winter":
        money_prize *= 0.85
money_for_charity = money_prize * 0.75
money_per_dancer = (money_prize - money_for_charity) / dancers_number
print(f"Charity - {money_for_charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")