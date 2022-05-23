charity_goal = int(input())
transaction_counter = 0
cash_counter = 0
cash_money = 0
credit_card_counter = 0
credit_card_money = 0
while charity_goal > 0:
    transaction = input()
    if transaction == "End":
        print("Failed to collect required money for charity.")
        break
    transaction = int(transaction)
    transaction_counter += 1
    if transaction_counter % 2 == 0 and transaction >= 10: #credid card
        credit_card_counter += 1
        credit_card_money += transaction
        charity_goal -= transaction
        print("Product sold!")
    elif transaction_counter % 2 != 0 and transaction <= 100: #cash
        cash_counter += 1
        cash_money += transaction
        charity_goal -= transaction
        print("Product sold!")
    else:
        print("Error in transaction!")
if charity_goal <= 0:
    print(f"Average CS: {cash_money / cash_counter:.2f}")
    print(f"Average CC: {credit_card_money / credit_card_counter:.2f}")