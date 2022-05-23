locations_number = int(input())

for current_locations in range(locations_number):
    expected_average_gold = float(input())
    days_for_current_locations = int(input())
    mined_gold_per_location = 0
    for current_day in range(days_for_current_locations):
        gold_mined = float(input())
        mined_gold_per_location += gold_mined
    average_mined_gold = mined_gold_per_location / days_for_current_locations
    if average_mined_gold >= expected_average_gold:
        print(f"Good job! Average gold per day: {average_mined_gold:.2f}.")
    else:
        diff = abs(average_mined_gold - expected_average_gold)
        print(f"You need {diff:.2f} gold.")