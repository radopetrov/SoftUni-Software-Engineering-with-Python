goal = 10000
steps = input()
total_steps = 0
while True:
    if total_steps < goal and steps != "Going home":
        current_steps = int(steps)
        total_steps += current_steps
        if total_steps >= goal:
            break
    elif steps == "Going home":
        current_steps = int(input())
        total_steps += current_steps
        break
    steps = input()
diff = abs(goal - total_steps)
if total_steps >= goal:
    print("Goal reached! Good job!" )
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")