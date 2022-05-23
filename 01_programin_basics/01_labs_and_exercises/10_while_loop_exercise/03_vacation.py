needed_money = float(input())
money_in_hand = float(input())
spending_counter = 0
total_days = 0
# while needed_money > money_in_hand:
#     action = input()
#     total_days += 1
#     if action == "save":
#         current_sum = float(input())
#         money_in_hand += current_sum
#         spending_counter = 0
#     elif action == "spend":
#         current_sum = float(input())
#         spending_counter += 1
#         if current_sum > money_in_hand:
#             money_in_hand = 0
#         else:
#             money_in_hand -= current_sum
#     if spending_counter == 5:
#         break
# if spending_counter == 5:
#     print(f"You can't save the money.")
#     print(f"{total_days}")
# else:
#     print(f"You saved the money for {total_days} days.")
spending_too_many_days = False
while money_in_hand < needed_money:
    action = input()
    current_sum = input()
    total_days += 1
    if action == "save":
        money_in_hand += current_sum
        spending_counter = 0
    else:
        spending_counter += 1
        money_in_hand -= current_sum
        if spending_counter == 5:
            spending_too_many_days = True
            break
        if money_in_hand < 0:
            money_in_hand = 0
if spending_too_many_days:
    print(f"You can't save the money.")
    print(f"{total_days}")
else:
    print(f"You saved the money for {total_days} days.")