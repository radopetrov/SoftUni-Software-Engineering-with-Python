budget = int(input())
season = input()
fisherman_number = int(input())

ship_rent = 0

if season == "Spring":
    ship_rent = 3000
elif season == "Summer" or season == "Autumn":
    ship_rent = 4200
elif season == "Winter":
    ship_rent = 2600

if fisherman_number <= 6:
    ship_rent *= 0.9
elif fisherman_number >= 7 and fisherman_number <= 11:
    ship_rent *= 0.85
elif fisherman_number >= 12:
    ship_rent *= 0.75

if fisherman_number % 2 == 0 and season != "Autumn":
    ship_rent *= 0.95

money_dif = abs(budget - ship_rent)

if budget >= ship_rent:
    print(f"Yes! You have {money_dif:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_dif:.2f} leva.")