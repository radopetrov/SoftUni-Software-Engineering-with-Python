strawberry_price = float(input())
banana_qty = float(input())
orange_qty = float(input())
raspberry_qty = float(input())
strawberry_qty_ = float(input())
raspberry_price = strawberry_price * 0.5
oranges_price = raspberry_price * 0.6
banana_price = raspberry_price * 0.2
total_costs = strawberry_qty_ * strawberry_price + raspberry_qty * raspberry_price + oranges_price * orange_qty + banana_price * banana_qty
print(f"{total_costs:.2f}")