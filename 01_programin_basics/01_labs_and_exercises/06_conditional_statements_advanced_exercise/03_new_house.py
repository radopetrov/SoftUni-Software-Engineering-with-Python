flowers_types = input()
flowers_number = int(input())
budget = int(input())

price_per_flower = 0

if flowers_types == "Roses":
    price_per_flower = 5
    if flowers_number > 80:
        price_per_flower = 5 * 0.9
elif flowers_types == "Dahlias":
    price_per_flower = 3.80
    if flowers_number > 90:
        price_per_flower = 3.80 * 0.85
elif flowers_types == "Tulips":
    price_per_flower = 2.8
    if flowers_number > 80:
         price_per_flower = 2.8 * 0.85
elif flowers_types == "Narcissus":
    price_per_flower = 3
    if flowers_number < 120:
        price_per_flower = 3 * 1.15
elif flowers_types == "Gladiolus":
    price_per_flower = 2.5
    if flowers_number < 80:
        price_per_flower = 2.5 *1.2

flowers_cost = price_per_flower * flowers_number
money_dif = abs(flowers_cost - budget)

if budget >= flowers_cost:
    print(f"Hey, you have a great garden with {flowers_number} {flowers_types} and {money_dif:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_dif:.2f} leva more.")