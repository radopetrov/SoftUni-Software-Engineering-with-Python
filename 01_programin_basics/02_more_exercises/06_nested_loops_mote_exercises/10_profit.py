one_leva_coins_number = int(input())
two_leva_coins_number = int(input())
five_leva_bill_number = int(input())
total_sum = int(input())
for one_lv in range(one_leva_coins_number + 1):
    for two_lv in range(two_leva_coins_number + 1):
        for five_lv in range(five_leva_bill_number + 1):
            if (one_lv * 1) + (two_lv * 2) + (five_lv * 5) == total_sum:
                print(f"{one_lv} * 1 lv. + {two_lv} * 2 lv. + {five_lv} * 5 lv. = {total_sum} lv.")
