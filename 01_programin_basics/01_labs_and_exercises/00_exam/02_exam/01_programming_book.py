price_per_page = float(input())
cover_print_price = float(input())
discount_price = int(input())
designer_price = float(input())
team_share_percent = int(input())
pages_price = ((price_per_page * 899) + (2 * cover_print_price)) * ((100 - discount_price) / 100)
total_price = designer_price + pages_price
total_price *= (100 - team_share_percent) / 100
print(f"Avtonom should pay {total_price:.2f} BGN.")
