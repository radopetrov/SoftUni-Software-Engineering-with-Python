voucher_value = int(input())
purchase = input()
product_cost = 0
tickets_number = 0
items_number = 0
while purchase != "End":
    if len(purchase) > 8:
        product_cost = ord(purchase[0]) + ord(purchase[1])
        if product_cost <= voucher_value:
            voucher_value -= product_cost
            tickets_number += 1
        else:
            break
    else:
        product_cost = ord(purchase[0])
        if product_cost <= voucher_value:
            voucher_value -= product_cost
            items_number += 1
        else:
            break
    purchase = input()
print(tickets_number)
print(items_number)