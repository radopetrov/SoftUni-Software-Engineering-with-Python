customers_number = int(input())
total_sum = 0
for current_customer in range(customers_number):
    purchase = input()
    current_customer_sum = 0
    items_counter = 0
    while purchase != "Finish":
        items_counter += 1
        if purchase == "basket":
            current_customer_sum += 1.5
        elif purchase == "wreath":
            current_customer_sum += 3.8
        elif purchase == "chocolate bunny":
            current_customer_sum += 7
        purchase = input()
    if items_counter % 2 == 0:
        current_customer_sum *= 0.8
    total_sum += current_customer_sum
    print(f"You purchased {items_counter} items for {current_customer_sum:.2f} leva.")
average_bill = total_sum / customers_number
print(f"Average bill per client is: {average_bill:.2f} leva.")