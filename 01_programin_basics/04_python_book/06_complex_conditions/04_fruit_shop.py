fruit = input()
day_of_week = input()
fruit_quantity = float(input())
weekday = day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday"
weekend = day_of_week == "Saturday" or day_of_week == "Sunday"
fruits = fruit == "banana" or fruit == "apple" or fruit == "orange" or fruit == "grapefruit" or fruit == "kiwi" or fruit == "pineapple" or fruit == "grapes"
fruit_price = 0
is_error = False
if not fruits or (not weekday and not weekend):
    is_error = True
elif weekday:
    if fruit == "banana":
        fruit_price = 2.50
    elif fruit == "apple":
        fruit_price = 1.20
    elif fruit == "orange":
        fruit_price = 0.85
    elif fruit == "grapefruit":
        fruit_price = 1.45
    elif fruit == "kiwi":
        fruit_price = 2.70
    elif fruit == "pineapple":
        fruit_price = 5.50
    elif fruit == "grapes":
        fruit_price = 3.85
elif weekend:
    if fruit == "banana":
        fruit_price = 2.70
    elif fruit == "apple":
        fruit_price = 1.25
    elif fruit == "orange":
        fruit_price = 0.90
    elif fruit == "grapefruit":
        fruit_price = 1.60
    elif fruit == "kiwi":
        fruit_price = 3.00
    elif fruit == "pineapple":
        fruit_price = 5.60
    elif fruit == "grapes":
        fruit_price = 4.20
if is_error:
    print("error")
else:
    total_price = fruit_price * fruit_quantity
    print(f"{total_price:.2f}")