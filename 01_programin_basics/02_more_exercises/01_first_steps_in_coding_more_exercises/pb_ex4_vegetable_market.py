vegetables_price_per_kg = float(input())
fruits_price_per_kg = float(input())
vegetable_kg = int(input())
fruits_kg = int(input())
euro_rate = 1.94

income_vegetables = vegetable_kg * vegetables_price_per_kg
income_fruits = fruits_kg * fruits_price_per_kg
total_income_lv = income_fruits + income_vegetables
total_income_euro = total_income_lv / euro_rate
print(format(total_income_euro, '.2f'))
