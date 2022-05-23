student_name = input()
year = 1
sum = 0
fail_count = 0
while year <= 12:
    if fail_count > 1:
        break
    grade = float(input())
    if grade < 4:
        fail_count += 1
        continue
    sum += grade
    year += 1
if fail_count > 1:
    print(f"{student_name} has been excluded at {year} grade")
else:
    average_grade = sum / year
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
