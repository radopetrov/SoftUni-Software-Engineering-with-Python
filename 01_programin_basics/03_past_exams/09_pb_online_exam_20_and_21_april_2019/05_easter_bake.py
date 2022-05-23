import math

easter_bred_number = int(input())
sugar_total = 0
flour_total = 0
sugar_max = 0
flour_max = 0
for current_bread in range(easter_bred_number):
    sugar = int(input())
    flour = int(input())
    sugar_total += sugar
    flour_total += flour
    if sugar > sugar_max:
        sugar_max = sugar
    if flour > flour_max:
        flour_max = flour
sugar_packs_number = sugar_total / 950
flour_packs_number = flour_total / 750
print(f"Sugar: {math.ceil(sugar_packs_number)}")
print(f"Flour: {math.ceil(flour_packs_number)}")
print(f"Max used flour is {flour_max} grams, max used sugar is {sugar_max} grams.")