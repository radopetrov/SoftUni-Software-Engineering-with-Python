charity_goal = int(input())
transaction = input()
transaction_counter = 0
cash_counter = 0
cash_money = 0
credit_card_counter = 0
credit_card_money = 0
is_charity_successful = False
while transaction != "End":
    transaction = int(transaction)
    transaction_counter += 1
    if transaction_counter % 2 == 0: #credit card
        if transaction < 10:
            print("Error in transaction!")
        else:
            credit_card_counter += 1
            credit_card_money += transaction
            print("Product sold!")
    else:                           #cash
        if transaction > 100:
            print("Error in transaction!")
        else:
            cash_counter += 1
            cash_money += transaction
            print("Product sold!")
    raised_money = cash_money + credit_card_money
    if raised_money >= charity_goal:
        is_charity_successful = True
        break
    transaction = input()
if cash_counter == 0:
    average_cash = 0
else:
    average_cash = cash_money / cash_counter
if credit_card_counter == 0:
    average_credit_card = 0
else:
    average_credit_card = credit_card_money / credit_card_counter
if is_charity_successful:
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_credit_card:.2f}")
else:
    print(f"Failed to collect required money for charity.")
