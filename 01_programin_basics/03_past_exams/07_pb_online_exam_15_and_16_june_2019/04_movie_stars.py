budget = float(input())
actor_name = input()
budget_is_enough = True
while actor_name != "ACTION":
    if len(actor_name) > 15:
        actor_salary = budget * 0.2
    else:
        actor_salary = float(input())
    if budget >= actor_salary:
        budget -= actor_salary
    else:
        differance = abs(budget - actor_salary)
        budget_is_enough = False
        break
    actor_name = input()
if budget_is_enough:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {differance:.2f} leva for our actors.")