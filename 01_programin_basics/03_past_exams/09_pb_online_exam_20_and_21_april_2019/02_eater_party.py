guests_number = int(input())
coupon_price_per_guest = float(input())
budget = float(input())

if 10 <= guests_number <= 15:
    coupon_price_per_guest *= 0.85
elif 15 < guests_number <= 20:
    coupon_price_per_guest *= 0.8
elif 20 < guests_number:
    coupon_price_per_guest *= 0.75
cake_price = budget * 0.1
coupons_costs = guests_number * coupon_price_per_guest
total_costs = cake_price + coupons_costs
difference = abs(total_costs - budget)
if budget >= total_costs:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")