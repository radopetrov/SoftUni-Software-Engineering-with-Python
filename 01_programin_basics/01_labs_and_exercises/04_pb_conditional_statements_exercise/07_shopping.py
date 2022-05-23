budget = float(input())
video_cards_number = int(input())
processors_number = int(input())
ram_number = int(input())
video_cards_price_per_num = 250
video_cards_total_cost = video_cards_number * video_cards_price_per_num

processors_price_per_number = video_cards_total_cost * 35 / 100
ram_price_per_num  = video_cards_total_cost * 10 / 100

processors_total_cost = processors_number * processors_price_per_number
ram_total_cost = ram_number * ram_price_per_num

total_cost = video_cards_total_cost + processors_total_cost + ram_total_cost

if video_cards_number > processors_number:
    total_cost *= 0.85

money_difference = abs(total_cost - budget)

if budget >= total_cost:
    print(f"You have {money_difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {money_difference:.2f} leva more!")