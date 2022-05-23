import math
tennis_racket_price = float(input())
tennis_racket_number = int(input())
sneakers_pairs_number = int(input())
sneakers_pairs_price = tennis_racket_price / 6
sneakers_total_price = sneakers_pairs_price * sneakers_pairs_number
tennis_racket_total_price = tennis_racket_number * tennis_racket_price
total_sum = sneakers_total_price + tennis_racket_total_price
other_equipment = total_sum * 0.2
total_price = total_sum + other_equipment
djokovic_costs = total_price / 8
sponsors_cost = total_price - djokovic_costs
print(f"Price to be paid by Djokovic {math.floor(djokovic_costs)}")
print(f"Price to be paid by sponsors {math.ceil(sponsors_cost)}")