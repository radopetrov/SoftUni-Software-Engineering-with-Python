import math

words = input()
most_powerful_word = ""
max_points = 0

while words != "End of words":
    total_sum = 0
    for current_letter in words:
        total_sum += ord(current_letter)
    if words[0] in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']:
        total_sum *= len(words)
    else:
        total_sum = math.floor(total_sum / len(words))
    if total_sum > max_points:
        max_points = total_sum
        most_powerful_word = words
    words = input()
print(f"The most powerful word is {most_powerful_word} - {max_points}")
