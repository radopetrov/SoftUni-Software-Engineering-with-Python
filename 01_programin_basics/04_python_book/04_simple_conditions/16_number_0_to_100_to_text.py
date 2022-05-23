number = int(input())
if number < 20:
    if number == 0:
        print("zero")
    elif number == 1:
        print("one")
    elif number == 2:
        print("two")
    elif number == 3:
        print("three")
    elif number == 4:
        print("four")
    elif number == 5:
        print("five")
    elif number == 6:
        print("six")
    elif number == 7:
        print("seven")
    elif number == 8:
        print("eight")
    elif number == 9:
        print("nine")
    elif number == 10:
        print("ten")
    elif number == 11:
        print("eleven")
    elif number == 12:
        print("twelve")
    elif number == 13:
        print("thirteen")
    elif number == 14:
        print("fourteen")
    elif number == 15:
        print("fifteen")
    elif number == 16:
        print("sixteen")
    elif number == 17:
        print("seventeen")
    elif number == 18:
        print("eighteen")
    elif number == 19:
        print("nineteen")
elif number == 100:
    print("one hundred")
else:
    first_digit = number // 10
    second_digit = number % 10
    first_word = ""
    if first_digit == 2:
        first_word = "twenty"
    elif first_digit == 3:
        first_word = "thirty"
    elif first_digit == 4:
        first_word = "forty"
    elif first_digit == 5:
        first_word = "fifty"
    elif first_digit == 6:
        first_word = "sixty"
    elif first_digit == 7:
        first_word = "seventy"
    elif first_digit == 8:
        first_word = "eighty"
    elif first_digit == 9:
        first_word = "ninety"
    second_word = ""
    if second_digit == 1:
        second_word = "one"
    elif second_digit == 2:
        second_word = "two"
    elif second_digit == 3:
        second_word = "three"
    elif second_digit == 4:
        second_word = "four"
    elif second_digit == 5:
        second_word = "five"
    elif second_digit == 6:
        second_word = "six"
    elif second_digit == 7:
        second_word = "seven"
    elif second_digit == 8:
        second_word = "eight"
    elif second_digit == 9:
        second_word = "nine"
    if second_digit != 0:
        print(f"{first_word} {second_word}")
    else:
        print(first_word)