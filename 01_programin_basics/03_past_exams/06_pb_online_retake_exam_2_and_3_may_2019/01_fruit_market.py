strawberry_price = float(input())
banаnаs_kg = float(input())
oranges_kg = float(input())
raspberry_kg = float(input())
strawberry_kg = float(input())
raspberry_price = strawberry_price / 2
oranges_price = raspberry_price * 0.6
bananas_price = raspberry_price * 0.2
needed_money = bananas_price * banаnаs_kg + \
               oranges_price * oranges_kg + \
               raspberry_price * raspberry_kg + \
               strawberry_kg * strawberry_price
print(f"{needed_money:.02f}")