import math

magnolias_number = int(input()) #магнолии
hyacinths_number = int(input()) #зюмбюли
roses_number = int(input()) #рози
cactuses_number = int(input()) #кактуси
gift_prise = float(input())

magnolias_price_per_number = 3.25
hyacinths_price_per_number = 4
roses_price_per_number = 3.5
cactuses_price_per_number = 8

magnolias_total = magnolias_number * magnolias_price_per_number
hyacinths_total = hyacinths_number * hyacinths_price_per_number
roses_total = roses_number * roses_price_per_number
cactuses_total = cactuses_number * cactuses_price_per_number

total_sales = magnolias_total + hyacinths_total + roses_total + cactuses_total

total_sales *= 0.95
money_deference = abs(total_sales - gift_prise)

if total_sales >= gift_prise:
    print(f"She is left with {math.floor(money_deference)} leva.")
else:
    print(f"She will have to borrow {math.ceil(money_deference)} leva.")