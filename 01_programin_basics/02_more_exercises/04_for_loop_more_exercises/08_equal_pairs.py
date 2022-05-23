# n = int(input())
# previous = int(input()) + int(input())
# diff = 0
# for i in range(n -1):
#     curr = int(input()) + int(input())
#     if abs(previous - curr) > diff:
#         diff = abs(previous - curr)
#     previous = curr
# if diff == 0:
#     print(f"Yes, value={previous}")
# else:
#     print(f"No, maxdiff={diff}")

numbers_in_row = int(input())
difference_previous = 0
sum_previous = 0
for number in range(numbers_in_row):
    sum = int(input()) + int(input())
    difference = abs (sum - sum_previous)
    if difference > difference_previous:
        difference_previous = difference
    sum_previous = sum
if difference == 0:
    print(f"Yes, value = {sum}")
else:
    print(f"No, maxdiff = {difference_previous}")