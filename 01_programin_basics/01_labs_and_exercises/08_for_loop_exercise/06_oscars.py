actor = input()
acadamy_points = float(input())
judges_number = int(input())
judge_name_points = 0

for i in range(judges_number):
    judge_name = input()
    judge_points = float(input())
    judge_name_points = len(judge_name)
    acadamy_points += (judge_points * judge_name_points / 2)
    if acadamy_points > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {acadamy_points:.1f}!")
        break
if acadamy_points < 1250.5:
    diff = abs(1250.5 - acadamy_points)
    print(f"Sorry, {actor} you need {diff:.1f} more!")
