students_number = int(input())
total_sum_marks = 0
top_students = 0 #above 5
between_4_499 = 0
between_3_399 = 0
faild_students = 0 # between 2 and 2.99
for number in range (students_number):
    mark = float(input())
    total_sum_marks += mark
    if 2 <= mark <= 2.99:
        faild_students += 1
    elif 3 <= mark <= 3.99:
        between_3_399 += 1
    elif 4 <= mark <= 4.99:
        between_4_499 += 1
    elif mark >= 5:
        top_students += 1
average_mark = total_sum_marks / students_number
top_students_rate = top_students / students_number * 100
between_4_499_rate = between_4_499 / students_number * 100
between_3_399_rate = between_3_399 / students_number * 100
faild_students_rate = faild_students / students_number * 100
print(f"Top students: {top_students_rate:.02f}%")
print(f"Between 4.00 and 4.99: {between_4_499_rate:.02f}%")
print(f"Between 3.00 and 3.99: {between_3_399_rate:.02f}%")
print(f"Fail: {faild_students_rate:.02f}%")
print(f"Average: {average_mark:.02f}")