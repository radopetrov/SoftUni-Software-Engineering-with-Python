steps = int(input())
total_sum = 0
for numbers in range (steps):
    number = int(input())
    total_sum += number
average = total_sum / steps
print(f"{average:.2f}")