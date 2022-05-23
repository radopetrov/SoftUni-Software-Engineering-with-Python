count_c = 0
count_o = 0
count_n = 0
letter = input()
firs_word = ""
second_word = ""
while True:
    if letter == "End":
        break
    elif count_n == 0 or count_o == 0 or count_c == 0:
        if letter == "c" and count_c == 0:
            count_c = 1
        elif letter == "o" and count_o == 0:
            count_o = 1
        elif letter == "n" and count_n == 0:
            count_n = 1
        else:
            firs_word += letter
    elif count_n == 1 or count_o == 1 or count_c == 1:
        if letter == "c" and count_c == 1:
            count_c = 2
        elif letter == "o" and count_o == 1:
            count_o = 2
        elif letter == "n" and count_n == 1:
            count_n = 2
        else:
            second_word += letter
    elif count_n == 2 and count_o == 2 and count_c == 2:
        print(f"{firs_word} {second_word}")
        break
    letter = input()

print(f"{firs_word} {second_word}")
