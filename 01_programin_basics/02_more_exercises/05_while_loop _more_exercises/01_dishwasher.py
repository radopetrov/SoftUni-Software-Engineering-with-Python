detergent_bottles = int(input())
load = input()
load_time = 0
pots_number = 0
plates_number = 0
detergent_ml = detergent_bottles * 750
is_detergent_enough = True
while load != "End":
    load_time += 1
    load = int(load)
    if load_time % 3 == 0:
        pots_number += load
        detergent_ml -= load * 15
    else:
        plates_number += load
        detergent_ml -= load * 5
    if detergent_ml < 0:
        is_detergent_enough = False
        break
    load = input()
if is_detergent_enough:
    print(f"Detergent was enough!")
    print(f"{plates_number} dishes and {pots_number} pots were washed.")
    print(f"Leftover detergent {abs(detergent_ml)} ml.")
else:
    print(f"Not enough detergent, {abs(detergent_ml)} ml. more necessary!")