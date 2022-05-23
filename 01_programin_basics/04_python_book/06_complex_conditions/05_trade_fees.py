city = input()
sales = float(input())
cities = city == "Sofia" or city == "Varna" or city == "Plovdiv"
commission = 0
if sales < 0 or (not cities):
    print("error")
else:
    if city == "Sofia":
        if 0 <= sales <= 500:
            commission = 5
        elif sales <= 1000:
            commission = 7
        elif sales <= 10000:
            commission = 8
        elif sales > 10000:
            commission = 12
    elif city == "Varna":
        if 0 <= sales <= 500:
            commission = 4.5
        elif sales <= 1000:
            commission = 7.5
        elif sales <= 10000:
            commission = 10
        elif sales > 10000:
            commission = 13
    elif city == "Plovdiv":
        if 0 <= sales <= 500:
            commission = 5.5
        elif sales <= 1000:
            commission = 8
        elif sales <= 10000:
            commission = 12
        elif sales > 10000:
            commission = 14.5
    total_commission = sales * (commission / 100)
    print(f"{total_commission:.2f}")
