poor_grades_number = int(input())
problem_name = input()
total_sum_grades = 0
problem_number = 0
faild_problems = 0
is_succeeded = True
while problem_name != "Enough":
    problem_grade = int(input())
    total_sum_grades += problem_grade
    problem_number += 1
    if problem_grade <= 4:
        faild_problems += 1
        if faild_problems >= poor_grades_number:
            is_succeeded = False
            break
    last_problem = problem_name
    problem_name = input()
if is_succeeded == True:
    average_grade = total_sum_grades / problem_number
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {problem_number}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {faild_problems} poor grades.")