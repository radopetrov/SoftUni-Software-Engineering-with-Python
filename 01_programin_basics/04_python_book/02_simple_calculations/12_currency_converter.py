sum = float(input())
inputted_currency = input()
outputted_currency = input()
# 1 BGN == 1.79549 USD == 1.95583	EUR == 2.53405 GBP
converted = 0
if inputted_currency == "USD":
    converted = sum * 1.79549   #in BGN
    if outputted_currency == "EUR":
        converted /= 1.95583
    elif outputted_currency == "GBP":
        converted /= 2.53405
elif inputted_currency == "BGN":
    if outputted_currency == "EUR":
        converted = sum / 1.95583
    elif outputted_currency == "GBP":
        converted = sum / 2.53405
    elif outputted_currency == "USD":
        converted = sum / 1.79549
elif inputted_currency == "EUR":
    converted = sum * 1.95583
    if outputted_currency == "GBP":
        converted /= 2.53405
    elif outputted_currency == "USD":
        converted /= 1.79549
elif inputted_currency == "GBP":
    converted = sum * 2.53405
    if outputted_currency == "EUR":
        converted /= 1.95583
    elif outputted_currency == "USD":
        converted /= 1.79549
print(f"{round(converted, 2)} {outputted_currency}")