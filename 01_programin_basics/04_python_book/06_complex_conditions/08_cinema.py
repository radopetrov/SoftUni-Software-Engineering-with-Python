type_of_screening = input()
rows = int(input())
columns = int(input())
ticket_price = 0
if type_of_screening == "Premiere":
    ticket_price = 12
elif type_of_screening == "Normal":
    ticket_price = 7.5
elif type_of_screening == "Discount":
    ticket_price = 5
total_income = rows * columns * ticket_price
print(f"{total_income:.2f} leva")