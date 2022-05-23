number = int(input())
combination = 0
for first_number in range(number + 1):
    for second_number in range(number + 1):
        for third_number in range(number + 1):
            sumed_number = first_number + second_number + third_number
            if sumed_number == number:
               combination += 1
print(combination)
