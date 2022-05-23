movie_title = input()
hall_type = input()
sold_tickets = int(input())
ticket_prise = 0
if hall_type == "normal":
    if movie_title =="A Star Is Born":
        ticket_prise = 7.5
    elif movie_title == "Bohemian Rhapsody":
        ticket_prise = 7.35
    elif movie_title == "Green Book":
        ticket_prise = 8.15
    elif movie_title == "The Favourite":
        ticket_prise = 8.75
elif hall_type == "luxury":
    if movie_title =="A Star Is Born":
        ticket_prise = 10.5
    elif movie_title == "Bohemian Rhapsody":
        ticket_prise = 9.45
    elif movie_title == "Green Book":
        ticket_prise = 10.25
    elif movie_title == "The Favourite":
        ticket_prise = 11.55
elif hall_type == "ultra luxury":
    if movie_title =="A Star Is Born":
        ticket_prise = 13.5
    elif movie_title == "Bohemian Rhapsody":
        ticket_prise = 12.75
    elif movie_title == "Green Book":
        ticket_prise = 13.25
    elif movie_title == "The Favourite":
        ticket_prise = 13.95
total_profit = ticket_prise * sold_tickets
print(f"{movie_title} -> {total_profit:.02f} lv.")