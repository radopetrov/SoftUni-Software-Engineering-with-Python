budget = float(input())
ticket_type = input() #VIP or NORMAl
people_number = int(input())
if 1 <= people_number <= 4:
    budget *= 0.25
elif people_number <= 9:
    budget *= 0.4
elif people_number <= 24:
    budget *= 0.5
elif people_number <= 49:
    budget *= 0.6
elif people_number >= 50:
    budget *= 0.75
ticket_price = 0
if ticket_type == "VIP":
    ticket_price = 499.99
else:
    ticket_price = 249.99
total_ticket_price = ticket_price * people_number
money_diference = abs(total_ticket_price - budget)
if total_ticket_price <= budget:
    print(f"Yes! You have {money_diference:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_diference:.2f} leva.")