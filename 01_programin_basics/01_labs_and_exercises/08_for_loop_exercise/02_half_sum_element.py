import sys

n = int(input())
max_number = -sys.maxsize #max_number = ""
sum_numbers = 0
for i in range(0,n):
    currunt_number = int(input())
    sum_numbers += currunt_number
    if currunt_number > max_number: #if i == 0:
        max_number = currunt_number #   max_number = current_number
sum_numbers -= max_number
if sum_numbers == max_number:
    print("Yes")
    print(f"Sum = {sum_numbers}")
else:
    dif = abs(sum_numbers - max_number)
    print("No")
    print(f"Diff = {dif}")