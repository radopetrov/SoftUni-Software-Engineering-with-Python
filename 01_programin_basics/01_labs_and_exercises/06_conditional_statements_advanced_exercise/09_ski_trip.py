days = int(input())
room_type = input()
review = input()
room_price = 0
if room_type == "room for one person":
    room_price = 18
elif room_type == "apartment":
    if days < 10:
        room_price = 25 * 0.7
    elif days < 15:
        room_price = 25 * 0.65
    else:
        room_price = 25 * 0.5
elif room_type == "president apartment":
    if days < 10:
        room_price = 35 * 0.9
    elif days < 15:
        room_price = 35 * 0.85
    else:
        room_price = 35 * 0.8
total_prce = room_price * (days-1)
if review =="positive":
    total_prce *= 1.25
elif review == "negative":
    total_prce *= 0.9
print(f"{total_prce:.2f}")