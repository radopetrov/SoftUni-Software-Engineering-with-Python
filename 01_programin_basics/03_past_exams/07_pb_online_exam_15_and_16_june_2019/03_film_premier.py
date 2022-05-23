movie_title = input()
movie_package = input()
ticket_number = int(input())
ticket_price = 0
if movie_title=="John Wick":
    if movie_package=="Drink":
        ticket_price = 12
    elif movie_package=="Popcorn":
        ticket_price = 15
    elif movie_package=="Menu":
        ticket_price = 19
elif movie_title=="Star Wars":
    if movie_package=="Drink":
        ticket_price = 18
    elif movie_package=="Popcorn":
        ticket_price = 25
    elif movie_package=="Menu":
        ticket_price = 30
elif movie_title=="Jumanji":
    if movie_package=="Drink":
        ticket_price = 9
    elif movie_package=="Popcorn":
        ticket_price = 11
    elif movie_package=="Menu":
        ticket_price = 14
if movie_title=="Star Wars" and ticket_number >= 4:
    ticket_price *= 0.7
elif movie_title=="Jumanji" and ticket_number == 2:
    ticket_price *= 0.85
total_bill = ticket_price * ticket_number
print(f"Your bill is {total_bill:.02f} leva.")
