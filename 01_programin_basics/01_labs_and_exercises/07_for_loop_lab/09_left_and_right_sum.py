n = int(input())
left_sum = 0
for i in range (n):
    current_num = int(input())
    left_sum += current_num

right_sum = 0
for i in range (n):
    current_num = int(input())
    right_sum += current_num

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    dif = abs(left_sum - right_sum)
    print(f"No, diff = {dif}")