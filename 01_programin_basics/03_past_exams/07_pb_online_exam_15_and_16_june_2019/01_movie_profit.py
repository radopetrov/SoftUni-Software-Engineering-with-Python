movie_title = input()
days = int(input())
tickets_number = int(input())
ticket_price = float(input())
cinema_share_rate = int(input())
total_profit = (ticket_price * tickets_number * days) * ((100 - cinema_share_rate) / 100)
print(f"The profit from the movie {movie_title} is {total_profit:.02f} lv.")