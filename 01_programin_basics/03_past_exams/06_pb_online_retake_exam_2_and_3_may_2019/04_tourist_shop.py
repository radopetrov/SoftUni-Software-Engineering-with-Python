budget = float(input())
product_name = input()
bought_products_sum = 0
bought_products_count = 0
budget_is_enough = True
while product_name != "Stop":
    product_price = float(input())
    bought_products_count += 1
    if bought_products_count % 3 == 0:
        product_price /= 2
    if product_price <= budget:
        bought_products_sum += product_price
        budget -= product_price
    else:
        budget_is_enough = False
        break
    product_name = input()
if budget_is_enough:
    print(f"You bought {bought_products_count} products for {bought_products_sum:.2f} leva.")
else:
    difference = abs(budget - product_price)
    print(f"You don't have enough money!")
    print(f"You need {difference:.2f} leva!")