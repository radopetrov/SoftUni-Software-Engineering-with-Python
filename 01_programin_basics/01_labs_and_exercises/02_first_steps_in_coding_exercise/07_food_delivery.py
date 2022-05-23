chicken = int(input())
fish = int(input())
vegetarian = int(input())

int_order = chicken * 10.35 + fish * 12.40 + vegetarian * 8.15
desert = int_order * 0.20
total_price = int_order + desert + 2.50
print(total_price)