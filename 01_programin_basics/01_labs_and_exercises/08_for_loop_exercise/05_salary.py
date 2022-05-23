tabs = int(input())
salary = int(input())
facebook_number = 0
instagram_numbers = 0
reddit_numbers = 0
for i in range(tabs):
    tab_name = input()
    if tab_name == "Facebook":
        facebook_number += 1
    elif tab_name == "Instagram":
        instagram_numbers += 1
    elif tab_name == "Reddit":
        reddit_numbers += 1
total_charges = facebook_number * 150 + instagram_numbers * 100 + reddit_numbers * 50
dif = abs(total_charges - salary)
if salary <= total_charges:
    print("You have lost your salary.")
else:
    print(f"{dif:.0f}")