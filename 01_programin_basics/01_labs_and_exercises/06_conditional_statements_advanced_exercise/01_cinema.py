screening_type = input()
rows = int(input())
columns = int(input())

ticket_price = 0

if screening_type == "Premiere":
    ticket_price = 12
elif screening_type == "Normal":
    ticket_price = 7.5
elif screening_type == "Discount":
    ticket_price = 5

cinema_sits = rows * columns
total_profit = ticket_price * cinema_sits

print(f"{total_profit:.2f} leva")