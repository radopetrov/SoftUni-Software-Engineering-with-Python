jury_number = int(input())
presentation_name = input()
grades_counter = 0
total_grades_sum = 0
while presentation_name != "Finish":
    current_presentation_grades_sum = 0
    for jury in range(jury_number):
        grade = float(input())
        grades_counter += 1
        current_presentation_grades_sum += grade
        total_grades_sum += grade
    average_grade_current_presentation = current_presentation_grades_sum / jury_number
    print(f"{presentation_name} - {average_grade_current_presentation:.2f}.")
    presentation_name = input()
average_total_grade = total_grades_sum / grades_counter
print(f"Student's final assessment is {average_total_grade:.2f}.")
