days = int(input())
treated = 0
untreated = 0
doctors = 7
for currunt_day in range (1, days + 1):
    patients = int(input())
    if currunt_day % 3==0:
        if untreated > treated:
            doctors += 1
    if patients > doctors:
        treated += doctors
        untreated += patients - doctors
    else:
        treated += patients
print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")