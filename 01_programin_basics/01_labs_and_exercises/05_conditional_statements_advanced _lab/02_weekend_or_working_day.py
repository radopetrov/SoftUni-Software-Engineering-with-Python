day = input()

work_day = day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday"
weekend = day == "Saturday" or day == "Sunday"

if work_day:
    print("Working day")
elif weekend:
    print("Weekend")
else:
    print("Error")