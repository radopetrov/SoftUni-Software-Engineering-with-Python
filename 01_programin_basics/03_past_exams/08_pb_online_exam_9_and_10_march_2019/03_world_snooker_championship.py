championship_state = input()
ticket_type = input()
ticket_number = int(input())
photo = input()
photo_price = 40
ticket_price = 0
if championship_state == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.5
    elif ticket_type == "Premium":
        ticket_price = 105.20
    elif ticket_type == "VIP":
        ticket_price = 118.9
elif championship_state == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    elif ticket_type == "VIP":
        ticket_price = 300.4
elif championship_state=="Final":
    if ticket_type == "Standard":
        ticket_price = 110.1
    elif ticket_type == "Premium":
        ticket_price = 160.66
    elif ticket_type == "VIP":
        ticket_price = 400
total_price = ticket_price * ticket_number
if total_price > 4000:
    total_price *= 0.75
    photo_price = 0
elif total_price > 2500:
    total_price *= 0.9
if photo == "Y":
    total_price += photo_price * ticket_number
print(f"{total_price:.2f}")